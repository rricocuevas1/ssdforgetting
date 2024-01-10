import time
import pandas as pd
from statistics import mean
from statistics import pstdev
from greedy import *
from pipagerounding import *
from scgreedy import *
from knapsack_indep import *
from sklearn.metrics.pairwise import cosine_similarity
import sys


def main():
    def execute_computations(dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename, jaccard_sim=True , n_iterations = 2000):
        print(f'Tuples: {n_rows}, Queries: {n_queries}, Budget: {budget}')
        # Start computations
        # KNAPSACK
        lasttime = time.time()
        answer_knapsack = knapsack_solver(n_rows, budget, queries)
        currtime = time.time()
        knapsak_time = (currtime - lasttime)
        knapsack_utility = objective(dataset, answer_knapsack, queries, jaccard_sim)
        print(f"KNAPSACK time: {knapsak_time}")
        print(f"KNAPSACK utility: {knapsack_utility}")
        print("\n")
        # SCG (100 times)
        f_answers = []
        times = []
        for i in range(100):
            print(f'iteration {i}')
            lasttime = time.time()
            x_star = scg(n_rows, budget, queries, prob_queries, n_queries, dataset, T=n_iterations, K=1, jaccard_sim=jaccard_sim)
            currtime = time.time()
            laptime = (currtime - lasttime)
            times.append(laptime)
            answer_SCG = pipage_rounding(x_star, n_rows, budget)
            f_answers.append(objective(dataset, answer_SCG, queries, jaccard_sim))
            print(f'SCG time: {laptime}')
            print(f'SCG utility: {f_answers[i]}')
        scg_best_time = min(times)
        scg_average_time = mean(times)
        scg_stddev = pstdev(times)
        print(f"SCG time: best = {scg_best_time}, average = {scg_average_time}, standard deviation = {scg_stddev}")
        scg_best_ans = max(f_answers)
        scg_average_ans = mean(f_answers)
        scg_stddev_ans = pstdev(f_answers)
        print(f"SCG utility: best = {scg_best_ans}, average = {scg_average_ans}, standard deviation = {scg_stddev_ans}")
        print("\n")
        # LAZY GREEDY
        lasttime = time.time()
        answer_lazy_greedy_q = lazy_greedy(dataset, queries, budget,jaccard_sim)
        currtime = time.time()
        l_greedy_time = (currtime - lasttime)
        utility_l_greedy = objective(dataset, answer_lazy_greedy_q, queries,jaccard_sim)
        print("LAZY GREEDY time:", l_greedy_time)
        print("LAZY GREEDY utility:", utility_l_greedy)
        print("\n")
        with open(results_filename, 'w') as file:
            file.write(f'Tuples: {n_rows}, Queries: {n_queries}, Budget: {budget}\n')
            file.write("\n")
            file.write(f"KNAPSACK time: {knapsak_time}\n")
            file.write(f"KNAPSACK utility: {knapsack_utility}\n")
            file.write("\n")
            file.write(f"SCG time: best = {scg_best_time}, average = {scg_average_time}, standard deviation = {scg_stddev}\n")
            file.write(f"SCG utility: best = {scg_best_ans}, average = {scg_average_ans}, standard deviation = {scg_stddev_ans}\n")
            file.write("\n")
            file.write(f"LAZY GREEDY time: {l_greedy_time}\n")
            file.write(f"LAZY GREEDY utility: {utility_l_greedy}\n")
            file.write("\n")
        file.close()

    def compute_pairwise_sims(points, dataset, jaccard_sim):
        n = len(points)
        sims = []
        for i in range(n):
            for j in range(i + 1, n):
                d_i = dataset.loc[points[i]].values.flatten().tolist()
                d_j = dataset.loc[points[j]].values.flatten().tolist()
                if jaccard_sim:
                    s = jaccard(d_i, d_j)
                    if s != 0:
                        sims.append(jaccard(d_i, d_j))
                else:
                    s = cosine_similarity([d_i], [d_j])[0][0]
                    if s != 0:
                        sims.append(cosine_similarity([d_i], [d_j])[0][0])
        return sims

    def read_data(dataset_choice, percentage_of_db, percentage_of_ql, budget, n_iterations):
        dataset_paths = ["sample_data/real/flight data/flights.csv",
                         "sample_data/real/open photo data/photos.csv",
                         "sample_data/real/Wikidata/wikidata.csv"]
        querylogs_paths = ["sample_data/real/flight data/flights_queries_ordered.csv", #flights_queries
                           "sample_data/real/open photo data/photos_queries_less100_ordered.csv",
                           "sample_data/real/Wikidata/wikiqueries_final.csv"]

        def load_data(dataset_choice):
            if dataset_choice == 'flight':
                dataset = pd.read_csv(dataset_paths[0], delimiter=",")
                n_queries = 37
                querylog_path = querylogs_paths[0]
            elif dataset_choice == 'photo':
                dataset = pd.read_csv(dataset_paths[1], delimiter=",", header=None)
                n_queries = 443
                querylog_path = querylogs_paths[1]
            elif dataset_choice == 'wiki':
                dataset = pd.read_csv(dataset_paths[2], delimiter=",", header=None)
                dataset.columns = ["id"] + [f'Value{i}' for i in range(1, 385)]
                dataset.drop('id', inplace=True, axis=1)
                n_queries = 14081
                querylog_path = querylogs_paths[2]
            return dataset, n_queries, querylog_path

        # Load the data
        dataset, n_queries, querylog_path = load_data(dataset_choice)
        # Select the corresponding percentage of the database
        n_rows = dataset.shape[0]
        n_rows = int(round(n_rows * percentage_of_db))
        dataset = dataset.head(n_rows)
        # Calculate the budget
        if budget < 1:
            budget = int(round(n_rows * budget))
        else:
            budget = int(budget)
        # Select the queries
        n_queries = int(round(n_queries * percentage_of_ql))
        query_list = []
        with open(querylog_path, 'r') as file:
            csvreader = csv.reader(file)
            i = 0
            for row in csvreader:
                if row == []:
                    continue
                elif i < n_queries:
                    answer_s = list(set([int(w) for w in row]).intersection(set([j for j in range(n_rows)])))
                    if answer_s == []:
                        i = i + 1
                        continue
                    else:
                        query_list.append(answer_s)
                        i = i + 1
                else:
                    break
        file.close()
        n_queries = len(query_list)
        queries = {}
        prob_queries = []
        for i in range(n_queries):
            queries[i] = (query_list[i], 1 / n_queries)
            prob_queries.append(queries[i][1])
        results_filename = f"sample_data/real/results_{dataset_choice}%db{percentage_of_db}_%ql{percentage_of_ql}_budget{budget}_iterationsSCG{n_iterations}"
        return dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename

    # Run the experiments
    dataset_choice = sys.argv[1]  # dataset_choice in [flight, photo, wiki]
    percentage_of_db = float(sys.argv[2])
    percentage_of_ql = float(sys.argv[3])
    budget = float(sys.argv[4])
    n_iterations = int(sys.argv[5])
    av_stdevs_calculation = bool(int(sys.argv[6]))  # 0/1

    if dataset_choice == 'flight':
        jaccard_sim = True
    else:
        jaccard_sim = False
    dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename = read_data(dataset_choice,
        percentage_of_db, percentage_of_ql, budget, n_iterations)

    if av_stdevs_calculation:
        stdevs = []
        for i in range(n_queries):
            print(f"iteration {i}/{n_queries}")
            query = list(set(queries[i][0]))
            if len(query) < 2:
                stdevs.append(0)
            else:
                stdevs.append(pstdev(compute_pairwise_sims(query, dataset, jaccard_sim=jaccard_sim)))
        print(f"The average standard deviation is: {mean(stdevs)}")
        avstdevs = mean(stdevs)
    execute_computations(dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename,
                         jaccard_sim=jaccard_sim, n_iterations=n_iterations)
    if av_stdevs_calculation:
        f = open(f'{results_filename}', 'a')
        f.write(f"The average standard deviation is: {avstdevs}")
        f.close()


if __name__ == '__main__':
    main()
