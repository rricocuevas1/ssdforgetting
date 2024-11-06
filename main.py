import csv
import signal
import sys
import time
import uuid
from datetime import datetime
from statistics import mean
from statistics import pstdev

import pandas as pd

from dep_df import *
from indep_df import *
from lazy_greedy import *
from lazy_greedy_plus_fast_nn import *
from pipage_rounding import *
from query_based_amnesia import *


def main():
    def execute_computations(dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename,
                             jaccard_sim=True, n_iterations=2000, only_time=False):
        def handler(signum, frame):
            raise TimeoutError("Computation exceeded the time limit.")

        def run_with_timeout(func, *args):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(3 * 24 * 60 * 60)  # Set an alarm for 3 days
            try:
                lasttime = time.time()
                result = func(*args)
                currtime = time.time()
                elapsed_time = (currtime - lasttime)
                return result, elapsed_time
            except TimeoutError as e:
                print(e)
                return None, -1
            finally:
                signal.alarm(0)  # Cancel the alarm

        def print_results(method_name, result, elapsed_time):
            if result is not None and not only_time:
                utility = objective(dataset, result, queries, jaccard_sim)
                print(f"{method_name} utility: {utility}")
            else:
                utility = -1
            print(f"{method_name} time: {elapsed_time}")
            return elapsed_time, utility

        print(f'Tuples: {n_rows}, Queries: {n_queries}, Budget: {budget}')

        ##
        av_size_answer_sets = 0
        for i in range(len(queries)):
            av_size_answer_sets += len(queries[i][0])
        av_size_answer_sets = av_size_answer_sets / len(queries)
        print(f"The average size of the answer sets is {av_size_answer_sets}")
        ##
        # INDEP_DF
        answer_indep_df, indep_df_time = run_with_timeout(indep_df, n_rows, budget, queries)
        indep_df_time, indep_df_utility = print_results("Indep_df", answer_indep_df, indep_df_time)

        # DEP_DF
        def dep_df_computation():
            x_star = scg(n_rows, budget, queries, prob_queries, n_queries, dataset, T=n_iterations, K=1,
                         jaccard_sim=jaccard_sim)
            return pipage_rounding(x_star, n_rows, budget)

        answer_dep_df, dep_df_time = run_with_timeout(dep_df_computation)
        dep_df_time, dep_df_utility = print_results("Dep_df", answer_dep_df, dep_df_time)

        # QUERY-BASED AMNESIA
        answer_query_based_amnesia, query_based_amnesia_time = run_with_timeout(query_based_amnesia, n_rows, budget,
                                                                                queries)
        query_based_amnesia_time, query_based_amnesia_utility = print_results("QUERY-BASED AMNESIA",
                                                                              answer_query_based_amnesia,
                                                                              query_based_amnesia_time)

        # LAZY GREEDY
        answer_lazy_greedy, lazy_greedy_time = run_with_timeout(lazy_greedy, dataset, queries, budget, jaccard_sim)
        lazy_greedy_time, utility_lazy_greedy = print_results("LAZY GREEDY", answer_lazy_greedy, lazy_greedy_time)

        # LAZY GREEDY + fast NN
        threshold_acceptance = 0.95
        num_neighbors = 10
        answer_lazy_greedy_fast, lazy_greedy_time_fast = run_with_timeout(lazy_greedy_lsh, dataset, queries, budget,
                                                                          threshold_acceptance, num_neighbors,
                                                                          jaccard_sim)
        lazy_greedy_fast_time, utility_lazy_greedy_fast = print_results("LAZY GREEDY + fast NN",
                                                                        answer_lazy_greedy_fast, lazy_greedy_time_fast)

        # Write the results into a file
        with open(results_filename, 'w') as file:
            if not only_time:
                file.write(f'Algorithm, Time, Utility\n')
                file.write(f"INDEP_DF, {indep_df_time}, {indep_df_utility}\n")
                file.write(f"DEP_DF, {dep_df_time}, {dep_df_utility}\n")
                file.write(f"QUERY_BASED_AMNESIA, {query_based_amnesia_time}, {query_based_amnesia_utility}\n")
                file.write(f"LAZY GREEDY, {lazy_greedy_time}, {utility_lazy_greedy}\n")
                file.write(f"LAZY GREEDY + fast NN , {lazy_greedy_fast_time}, {utility_lazy_greedy_fast}\n")
            else:
                file.write(f'Algorithm, Time\n')
                file.write(f"INDEP_DF, {indep_df_time}\n")
                file.write(f"DEP_DF, {dep_df_time}\n")
                file.write(f"QUERY_BASED_AMNESIA, {query_based_amnesia_time}\n")
                file.write(f"LAZY GREEDY, {lazy_greedy_time}\n")
                file.write(f"LAZY GREEDY + fast NN , {lazy_greedy_fast_time}\n")

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
                        sims.append(s)
                else:
                    s = cosine_similarity([d_i], [d_j])[0][0]
                    s = (s + 1) / 2
                    if s != 0:
                        sims.append(s)
        return sims

    def read_data(dataset_choice, percentage_of_db, percentage_of_ql, budget, n_iterations, av_stdevs_calculation):
        dataset_paths = ["sample_data/real/flight data/flights.csv",
                         "sample_data/real/open photo data/photos.csv",
                         "sample_data/real/Wikidata/wikidata.csv"]
        querylogs_paths = ["sample_data/real/flight data/flights_queries_ordered.csv",  # flights_queries
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
        results_filename = f"sample_data/real/results_{dataset_choice}%db{percentage_of_db}_%ql{percentage_of_ql}_budget{budget}_iterations{n_iterations}_av{av_stdevs_calculation}_onlytime{only_time}_{timestamp}_{unique_id}"
        return dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename

    # Run the experiments
    dataset_choice = sys.argv[1]  # dataset_choice in [flight, photo, wiki]
    percentage_of_db = float(sys.argv[2])  # percentage of the database
    percentage_of_ql = float(sys.argv[3])  # percentage of the query-log
    budget = float(sys.argv[4])  # budget
    n_iterations = int(sys.argv[5])  # number of iterations
    av_stdevs_calculation = bool(int(sys.argv[6]))  # 0/1
    only_time = bool(int(sys.argv[7]))  # 0/1

    if dataset_choice == 'flight':
        jaccard_sim = True
    else:
        jaccard_sim = False
    dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename = read_data(dataset_choice,
                                                                                            percentage_of_db,
                                                                                            percentage_of_ql, budget,
                                                                                            n_iterations,
                                                                                            av_stdevs_calculation)

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
    dataset = dataset.values  # Convert dataset to NumPy array
    execute_computations(dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename,
                         jaccard_sim=jaccard_sim, n_iterations=n_iterations, only_time=only_time)
    if av_stdevs_calculation:
        f = open(f'{results_filename}', 'a')
        f.write(f"\nThe average standard deviation is: {avstdevs}")
        f.close()


if __name__ == '__main__':
    main()
