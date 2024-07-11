import time
import pandas as pd
from statistics import mean
from statistics import pstdev
from query_based_amnesia import *
from lazy_greedy import *
from pipagerounding import *
from dep_df import *
from indep_df import *
from sklearn.metrics.pairwise import cosine_similarity
import sys
import signal
import uuid
from datetime import datetime
# chmod +x run_tmux_sessions.sh

def main():
    def execute_computations(dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename, jaccard_sim=True , n_iterations = 2000, only_time=False):
        print(f'Tuples: {n_rows}, Queries: {n_queries}, Budget: {budget}')
        # Start computations
        # INDEP_DF
        lasttime = time.time()
        answer_indep_df = indep_df(n_rows, budget, queries)
        currtime = time.time()
        indep_df_time = (currtime - lasttime)
        if not only_time:
            indep_df_utility = objective(dataset, answer_indep_df, queries, jaccard_sim)
            print(f"Indep_df utility: {indep_df_utility}")
        print(f"Indep_df time: {indep_df_time}")
        print("\n")

        # DEP_DF
        lasttime = time.time()
        x_star = scg(n_rows, budget, queries, prob_queries, n_queries, dataset, T=n_iterations, K=1, jaccard_sim=jaccard_sim)
        answer_dep_df = pipage_rounding(x_star, n_rows, budget)
        currtime = time.time()
        dep_df_time = (currtime - lasttime)
        if not only_time:
            dep_df_utility = objective(dataset, answer_dep_df, queries, jaccard_sim)
            print(f"Dep_df utility: {dep_df_utility}")
        print(f"Dep_df time: {dep_df_time}")
        print("\n")

        # QUERY-BASED AMNESIA
        lasttime = time.time()
        answer_query_based_amnesia = query_based_amnesia(n_rows, budget, queries)
        currtime = time.time()
        query_based_amnesia_time = (currtime - lasttime)
        if not only_time:
            query_based_amnesia_utility = objective(dataset, answer_query_based_amnesia, queries, jaccard_sim)
            print(f"QUERY-BASED AMNESIA utility: {query_based_amnesia_utility}")
        print(f"QUERY-BASED AMNESIA time: {query_based_amnesia_time}")
        print("\n")

        # LAZY GREEDY
        # Define a handler for the alarm signal
        def handler(signum, frame):
            raise TimeoutError("LAZY GREEDY computation exceeded the time limit.")
        # Register the handler for the SIGALRM signal
        signal.signal(signal.SIGALRM, handler)
        # Set an alarm for 3 days (3*24*60*60 seconds)
        signal.alarm(3 * 24 * 60 * 60)
        try:
            lasttime = time.time()
            answer_lazy_greedy = lazy_greedy(dataset, queries, budget, jaccard_sim)
            currtime = time.time()
            lazy_greedy_time = (currtime - lasttime)
            if not only_time:
                utility_lazy_greedy = objective(dataset, answer_lazy_greedy, queries, jaccard_sim)
                print("LAZY GREEDY utility:", utility_lazy_greedy)
            print("LAZY GREEDY time:", lazy_greedy_time)
        except TimeoutError as e:
            print(e)
            utility_lazy_greedy = -1
            lazy_greedy_time = -1
            print("LAZY GREEDY computation exceeded 3 days and was terminated.")
            print("LAZY GREEDY utility could not be calculated because the computation was terminated.")
        finally:
            # Cancel the alarm
            signal.alarm(0)

        # Write the results into a file
        with open(results_filename, 'w') as file:
            if not only_time:
                file.write(f'Algorithm, Time, Utility\n')
                file.write(f"INDEP_DF, {indep_df_time}, {indep_df_utility}\n")
                file.write(f"DEP_DF, {dep_df_time}, {dep_df_utility}\n")
                file.write(f"QUERY_BASED_AMNESIA, {query_based_amnesia_time}, {query_based_amnesia_utility}\n")
                file.write(f"LAZY GREEDY, {lazy_greedy_time}, {utility_lazy_greedy}\n")
            else:
                file.write(f'Algorithm, Time\n')
                file.write(f"INDEP_DF, {indep_df_time}\n")
                file.write(f"DEP_DF, {dep_df_time}\n")
                file.write(f"QUERY_BASED_AMNESIA, {query_based_amnesia_time}\n")
                file.write(f"LAZY GREEDY, {lazy_greedy_time}\n")
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
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
        unique_id = uuid.uuid4()
        results_filename = f"sample_data/real/results_{dataset_choice}%db{percentage_of_db}_%ql{percentage_of_ql}_budget{budget}_iterationsSCG{n_iterations}_onlytime{only_time}_{timestamp}_{unique_id}"
        return dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename

    # Run the experiments
    dataset_choice = sys.argv[1]  # dataset_choice in [flight, photo, wiki]
    percentage_of_db = float(sys.argv[2])  # percentage of the database
    percentage_of_ql = float(sys.argv[3])  # percentage of the query-log
    budget = float(sys.argv[4])  # budget
    n_iterations = int(sys.argv[5])  # number of SCG iterations
    av_stdevs_calculation = bool(int(sys.argv[6]))  # 0/1
    only_time = bool(int(sys.argv[7]))  # 0/1

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
                         jaccard_sim=jaccard_sim, n_iterations=n_iterations, only_time=only_time)
    if av_stdevs_calculation:
        f = open(f'{results_filename}', 'a')
        f.write(f"The average standard deviation is: {avstdevs}")
        f.close()


if __name__ == '__main__':
    main()
