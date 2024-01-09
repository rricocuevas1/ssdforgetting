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
    """
    # Toy example
    dataset = [['James', 'Smith', 25, 'Amsterdam','Teacher','Yes',2]
        , ['Wade', 'Brown', 25, 'Paris','Firefighter','No',0]
        , ['Olivia', 'Smith', 25, 'Amsterdam','Teacher','Yes',2]]
    dataset = pd.DataFrame(dataset, columns=['Name', 'Last Name', 'Age', 'City','Job','Married','Children'])
    n_rows = dataset.shape[0]
    budget = 2
    queries = {
        0: ([0, 1, 2], 1/3),
        1: ([0, 2], 1/3),
        2: ([2], 1/3),
    }
    n_queries = len(queries)
    prob_queries = []
    for i in range(n_queries):
        prob_queries.append(queries[i][1])
    # Start computations
    print("Optimum", objective(dataset, [1,2], queries))
    # KNAPSACK
    lasttime = time.time()
    answer_knapsack = knapsack_solver(n_rows, budget, queries)
    currtime = time.time()
    laptime = (currtime - lasttime)
    print("KNAPSACK time:", laptime)
    print("f(answer):", objective(dataset, answer_knapsack, queries))
    print("\n")
    # KNAPSACK + PRank
    lasttime = time.time()
    answer_knapsack_pr = pagerank_spread_linear(dataset, compute_weight(n_rows, queries), budget)
    currtime = time.time()
    laptime = (currtime - lasttime)
    print("KNAPSACK + PageRank time:", laptime)
    print("f(answer):", objective(dataset, answer_knapsack_pr, queries))
    print("\n")
    f_answers = []
    times = []
    # SCG (100 times)
    for i in range(100):
        print(f'iteration {i}')
        lasttime = time.time()
        x_star = scg(n_rows, budget, queries, prob_queries, n_queries, dataset, T=100, K=1)
        currtime = time.time()
        laptime = (currtime - lasttime)
        times.append(laptime)
        print(f'SCG took {laptime}')
        answer_SCG = pipage_rounding(x_star, n_rows, budget)
        f_answers.append(objective(dataset, answer_SCG, queries))
        print(f'Utility {f_answers[i]}')
    print(f"SCG time: best = {min(times)}, average = {mean(times)}, standard deviation:{stdev(times)}")
    print(f"f(best answer): {max(f_answers)}, f(average answer):{mean(f_answers)}, standard deviation:{stdev(f_answers)}")
    print("\n")
    # LAZY GREEDY
    lasttime = time.time()
    answer_lazy_greedy_q = lazy_greedy(dataset, queries, budget)
    currtime = time.time()
    laptime = (currtime - lasttime)
    print("LAZY GREEDY time:", laptime)
    print("f(answer):", objective(dataset, answer_lazy_greedy_q, queries))
    print("\n")
    # Toy example plot
    mpl.style.use("seaborn-notebook")
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for i in range(100):
        points = [[]] * 101
        with open(f"sample_data/synthetic/toy_example{i}.csv", 'r') as file:
            csvreader = csv.reader(file)
            j = 0
            for row in csvreader:
                points[j] = [float(w) for w in row]
                j = j + 1
        file.close()
        for point in points:
            x = point[0]
            y = point[1]
            z = point[2]
            ax.scatter(x, y, z, s=1, c='tab:orange')
    ax.grid(False)
    ax.set_zlim(0, 1)
    plt.xlim([0,1])
    plt.ylim([0,1])
    # draw cube
    r = [0, 1]
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s - e)) == r[1] - r[0]:
            ax.plot3D(*zip(s, e), color="black", linewidth=0.5,linestyle="dashed")
    ax.view_init(30, 20)
    ax.scatter(0, 0, 0, c='black', s=10)
    ax.scatter(1, 0, 0, c='black', s=10)
    ax.scatter(0, 1, 0, c='black', s=10)
    ax.scatter(0, 0, 1, c='black', s=10)
    ax.scatter(1, 1, 0, c='black', s=10)
    ax.scatter(1, 0, 1, c='black', s=10)
    ax.scatter(0, 1, 1, c='black', s=10)
    ax.scatter(1, 1, 1, c='black', s=10)
    #ax.set_xlabel('d_1')
    #ax.set_ylabel('d_2')
    #ax.set_zlabel('d_3')
    plt.show()
     """

    # Experiments synthetic data:
    """
    def read_data_synthetic_data_db_size(file_no):
        # Read data and queries
        dataset = pd.read_csv(f"sample_data/synthetic/data{file_no}.csv", delimiter=",")
        n_rows = dataset.shape[0]
        n_queries = 1
        budget = 20
        queries = {}
        with open("sample_data/synthetic/queries1.csv", 'r') as file:
            csvreader = csv.reader(file)
            i = 0
            for row in csvreader:
                queries[i] = ([int(w) for w in row], 1/n_queries)
                i = i + 1
        file.close()
        prob_queries = []
        for i in range(n_queries):
            prob_queries.append(queries[i][1])
        results_filename = f"sample_data/synthetic/results_db_size{file_no}"
        return dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename

    def read_data_synthetic_data_ql_size(file_no):
        # Read data and queries
        dataset = pd.read_csv("sample_data/synthetic/data1000.csv", delimiter=",")
        n_rows = dataset.shape[0]
        n_queries = int(file_no)
        budget = 20
        queries = {}
        with open(f"sample_data/synthetic/queries{file_no}.csv", 'r') as file:
            csvreader = csv.reader(file)
            i = 0
            for row in csvreader:
                if i == 0:
                    queries[i] = ([int(w) for w in row], 1)
                else:
                    queries[i] = ([int(w) for w in row], 0)
                i = i + 1
        file.close()
        prob_queries = []
        for i in range(n_queries):
            prob_queries.append(queries[i][1])
        results_filename = f"sample_data/synthetic/results_ql_size{file_no}"
        return dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename

    def read_data_synthetic_data_budget_size(percentage_of_db):
        # Read data and queries
        dataset = pd.read_csv("sample_data/synthetic/data1000.csv", delimiter=",")
        n_rows = dataset.shape[0]
        n_queries = 1
        budget = int(round(n_rows * percentage_of_db))
        queries = {}
        with open(f"sample_data/synthetic/queries1.csv", 'r') as file:
            csvreader = csv.reader(file)
            i = 0
            for row in csvreader:
                queries[i] = ([int(w) for w in row], 1 / n_queries)
                i = i + 1
        file.close()
        prob_queries = []
        for i in range(n_queries):
            prob_queries.append(queries[i][1])
        results_filename = f"sample_data/synthetic/results_budget{percentage_of_db}"
        return dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename
    """

    def execute_computations(dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename, jaccard_sim=True , n_iterations = 2000):
        print(f'Tuples: {n_rows}, Queries: {n_queries}, Budget: {budget}')
        # Start computations
        # KNAPSACK
        lasttime = time.time()
        answer_knapsack = knapsack_solver(n_rows, budget, queries)
        currtime = time.time()
        knapsak_time = (currtime - lasttime)
        print(f"KNAPSACK time: {knapsak_time}")
        knapsack_utility = objective(dataset, answer_knapsack, queries, jaccard_sim)
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
            print(f'SCG took {laptime}')
            answer_SCG = pipage_rounding(x_star, n_rows, budget)
            f_answers.append(objective(dataset, answer_SCG, queries, jaccard_sim))
            print(f'Utility {f_answers[i]}')
        scg_best_time = min(times)
        scg_average_time = mean(times)
        scg_stddev = pstdev(times)
        print(f"SCG time: best = {scg_best_time}, average = {scg_average_time}, standard deviation = {scg_stddev}")
        scg_best_ans = max(f_answers)
        scg_average_ans = mean(f_answers)
        scg_stddev_ans = pstdev(f_answers)
        print(f"SCG utility: best = {scg_best_ans}, average = {scg_average_ans}, standard deviation = {scg_stddev_ans}")
        print("\n")
        # Objective computation best case LAZY GREEDY
        #lasttime = time.time()
        #obj = objective(dataset, [random.randint(0, n_rows - 1)], queries, jaccard_sim)
        #currtime = time.time()
        #single_function_computation_time = (currtime - lasttime)
        #print(f'{obj}')
        #print(f'One objective best case evaluation took {single_function_computation_time}')
        #print(f'LAZY GREEDY time will be at least: {single_function_computation_time * n_rows}')
        #print('\n')
        # KNAPSACK + PRank
        #lasttime = time.time()
        #answer_knapsack_pr = pagerank_spread_linear(dataset, compute_weight(n_rows, queries), budget)
        #currtime = time.time()
        #knapsack_pr_time = (currtime - lasttime)
        #print(f"KNAPSACK + PageRank time: {knapsack_pr_time}")
        #knapsack_pr_utility = objective(dataset, answer_knapsack_pr, queries, jaccard_sim)
        #print(f"KNAPSACK + PageRank utility: {knapsack_pr_utility}")
        #print("\n")
        # LAZY GREEDY
        lasttime = time.time()
        answer_lazy_greedy_q = lazy_greedy(dataset, queries, budget,jaccard_sim)
        currtime = time.time()
        l_greedy_time = (currtime - lasttime)
        print("LAZY GREEDY time:", l_greedy_time)
        utility_l_greedy = objective(dataset, answer_lazy_greedy_q, queries,jaccard_sim)
        print("LAZY GREEDY utility:", utility_l_greedy)
        print("\n")
        with open(results_filename, 'w') as file:
            file.write(f'Tuples: {n_rows}, Queries: {n_queries}, Budget: {budget}\n')
            file.write("\n")
            file.write(f"KNAPSACK time: {knapsak_time}\n")
            file.write(f"KNAPSACK utility: {knapsack_utility}\n")
            file.write("\n")
            #file.write(f"KNAPSACK + PageRank time: {knapsack_pr_time}\n")
            #file.write(f"KNAPSACK + PageRank utility: {knapsack_pr_utility}\n")
            #file.write("\n")
            file.write(f"SCG time: best = {scg_best_time}, average = {scg_average_time}, standard deviation = {scg_stddev}\n")
            file.write(f"SCG utility: best = {scg_best_ans}, average = {scg_average_ans}, standard deviation = {scg_stddev_ans}\n")
            #file.write("\n")
            #file.write(f'One objective best case evaluation took {single_function_computation_time}\n')
            #file.write(f'LAZY GREEDY time will be at least: {single_function_computation_time * n_rows}\n')
            file.write("\n")
            file.write(f"LAZY GREEDY time: {l_greedy_time}\n")
            file.write(f"LAZY GREEDY utility: {utility_l_greedy}\n")
            file.write("\n")
        file.close()

    # Experiments real data:
    """
    # Flights data
    def read_flights_data(percentage_of_db, percentage_of_ql, budget, n_iterations):
        # Read data and queries
        dataset = pd.read_csv("sample_data/real/flight data/flights.csv", delimiter=",")
        n_rows = dataset.shape[0]
        n_rows = int(round(n_rows * percentage_of_db))
        dataset = dataset.head(n_rows)
        if budget < 1:
            budget = int(round(n_rows * budget))
        else:
            budget = int(budget)
        n_queries = 37
        n_queries = int(round(n_queries*percentage_of_ql))
        queries = {}
        random.seed(1998)
        rows = random.sample(range(37), n_queries)
        with open("sample_data/real/flight data/flights_queries.csv", 'r') as file:
            csvreader = csv.reader(file)
            i = 0
            counter = 0
            for row in csvreader:
                if i in rows:
                    queries[counter] = (list(set([int(w) for w in row]).intersection(set([j for j in range(n_rows)]))), 1 / n_queries)
                    i = i + 1
                    counter = counter + 1
                else:
                    i = i + 1
                    continue
        file.close()
        prob_queries = []
        for i in range(n_queries):
            prob_queries.append(queries[i][1])
        results_filename = f"sample_data/real/results_flights_data_%db{percentage_of_db}_%ql{percentage_of_ql}_budget{budget}_iterationsSCG{n_iterations}"
        return dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename

    # Photo data
    def read_photo_data(percentage_of_db, percentage_of_ql, budget, n_iterations):
        # Read data and queries
        dataset = pd.read_csv("sample_data/real/open photo data/photos.csv", delimiter=",", header=None)
        n_rows = dataset.shape[0]
        n_rows = int(round(n_rows * percentage_of_db))
        dataset = dataset.head(n_rows)
        if budget < 1:
            budget = int(round(n_rows * budget))
        else:
            budget = int(budget)
        n_queries = 0
        with open("sample_data/real/open photo data/photos_queries_less100_ordered.csv") as fp:
            for _ in fp:
                n_queries += 1
        fp.close()
        n_queries = int(round(n_queries*percentage_of_ql))
        queries = {}
        with open("sample_data/real/open photo data/photos_queries_less100_ordered.csv", 'r') as file:
            csvreader = csv.reader(file)
            i = 0
            for row in csvreader:
                if i <= n_queries:
                    queries[i] = (list(set([int(w) for w in row]).intersection(set([j for j in range(n_rows)]))), 1 / n_queries)
                    i = i + 1
                else:
                    break
        file.close()
        prob_queries = []
        for i in range(n_queries):
            prob_queries.append(queries[i][1])
        results_filename = f"sample_data/real/results_open_photo_data_%db{percentage_of_db}_%ql{percentage_of_ql}_budget{budget}_iterationsSCG{n_iterations}"
        return dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename

    # Wikidata
    def read_wiki_data(percentage_of_db, percentage_of_ql, budget, n_iterations):
        # Read Wikidata
        dataset = pd.read_csv("sample_data/real/Wikidata/wikidata.csv", delimiter=",", header=None)
        dataset.columns = ["id"]+[f'Value{i}' for i in range(1, 385)]
        dataset.drop('id', inplace=True, axis=1)
        n_rows = dataset.shape[0]
        n_rows = int(round(n_rows * percentage_of_db))
        dataset = dataset.head(n_rows)
        if budget < 1:
            budget = int(round(n_rows * budget))
        else:
            budget = int(budget)
        # Read queries
        n_queries = 14081
        n_queries = int(round(n_queries * percentage_of_ql))
        query_list = []
        with open("sample_data/real/Wikidata/wikiqueries_final.csv", 'r') as file:
            csvreader = csv.reader(file)
            i = 0
            for row in csvreader:
                if row == []:
                    continue
                if i >= n_queries:
                    i = i + 1
                    continue
                answer_s = list(set([int(w) for w in row]).intersection(set([j for j in range(n_rows)])))
                if answer_s == []:
                    i = i + 1
                    continue
                else:
                    query_list.append(answer_s)
                    i = i + 1
        file.close()
        n_queries = len(query_list)
        queries = {}
        prob_queries = []
        for i in range(n_queries):
            queries[i] = (query_list[i], 1 / n_queries)
            prob_queries.append(queries[i][1])
        results_filename = f"sample_data/real/results_wikidata%db{percentage_of_db}_%ql{percentage_of_ql}_budget{budget}_iterationsSCG{n_iterations}"
        return dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename
    """

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
    """
    def compute_average_stdevs(dataset_choice, percentage_of_db, percentage_of_ql, budget, n_iterations):
        dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename = read_data(dataset_choice, percentage_of_db, percentage_of_ql, budget, n_iterations)
        if dataset_choice == "flight":
            jaccard_sim = True
        else:
            jaccard_sim = False
        stdevs = []
        for i in range(n_queries):
            print(f"iteration {i}/{n_queries}")
            query = list(set(queries[i][0]))
            if len(query) < 2:
                stdevs.append(0)
            else:
                stdevs.append(pstdev(compute_pairwise_sims(query, dataset, jaccard_sim=jaccard_sim)))
        return mean(stdevs)
    """
    # Average of standard deviations between pairwise sims:
    """
    text = input('flights or photos or wiki (f/p/w)')
    if text == 'f':
        dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename = read_flights_data(1, 1, 0.01, 2000)
        stdevs = []
        n_samples = n_queries #int(n_queries*0.1)
        for i in range(n_samples):
            q_index = i #np.random.choice(n_queries, 1, p=prob_queries)[0]
            print(f"iteration {i}/{n_samples}")
            query = list(set(queries[q_index][0]))
            #if len(query) > 100:
            #    print(f"iteration {i}/{n_samples} Skipped")
            #    continue
            if len(query) <= 2:
                stdevs.append(0)
            else:
                stdevs.append(pstdev(compute_pairwise_sims(query, dataset, jaccard_sim=True)))
        print(f"Standard deviation of pairwise sims in flight data: {mean(stdevs)}")
    elif text == 'p':
        dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename = read_photo_data(1,0.75,0.01, 2000)
        stdevs = []
        n_samples = n_queries
        for i in range(n_samples):
            q_index = i
            print(f"iteration {i}/{n_samples}")
            query = list(set(queries[q_index][0]))
            if len(query) > 100:
                print(f"iteration {i}/{n_samples} Skipped")
                continue
            if len(query) <= 2:
                stdevs.append(0)
            else:
                stdevs.append(pstdev(compute_pairwise_sims(query, dataset, jaccard_sim=False)))
        print(f"Standard deviation of parwise sims in photo data: {mean(stdevs)}")
    elif text == 'w':
        dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename = read_wiki_data(1,1,0.01, 2000)
        stdevs = []
        n_samples = n_queries #int(n_queries*0.1)
        for i in range(n_samples):
            q_index = i #np.random.choice(n_queries, 1, p=prob_queries)[0]
            print(f"iteration {i}/{n_samples}")
            query = list(set(queries[q_index][0]))
            if len(query) <= 2:
                stdevs.append(0)
            else:
                stdevs.append(pstdev(compute_pairwise_sims(query, dataset, jaccard_sim=False)))
        print(f"Standard deviation of parwise sims in wiki data: {mean(stdevs)}")
    else:
        print('Exit program')
        sys.exit(0)
    """
    # Run the experiments
    """
    text = input("Do you want to go for syntehtic data? (y/n): ")
    if text == "y":
        # Synthetic data experiments
        text = input("Do you want to generate datasets? (y/n): ")
        if text == "y":
            # Synthetic data:
            # Generate the datasets
            print("Start generating datasets")
            for size in [1000, 10000, 50000, 100000]:
                generate_synthetic_data_pt2(size)
            print("Finished generating datasets")
            # Generate the query-logs
            print("Start generating logs")
            for size in [1, 1000, 5000, 10000]:
                generate_synthetic_query_pt2(size)
            print("Finished generating logs")
        else:
            text = input("Do you want to run experiment on db_size? (y/n): ")
            if text == "y":
                text = input("Give file_no [1000, 10000, 50000, 100000]: ")
                # Run the first group of experiments
                file_no = int(text)
                dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename = read_data_synthetic_data_db_size(file_no)
                execute_computations(dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename)
            else:
                text = input("Do you want to run experiment on ql_size? (y/n): ")
                if text == "y":
                    text = input("Give file_no [1, 1000, 5000, 10000]: ")
                    # Run the second group of experiments:
                    file_no = int(text)
                    dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename = read_data_synthetic_data_ql_size(file_no)
                    execute_computations(dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename)
                else:
                    text = input("Do you want to run experiment on budget_size? (y/n): ")
                    if text == "y":
                        text = input("Provide percentage: (0.1,0.25,0.5,0.75): ")
                        percentage_of_db = float(text)
                        dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename = read_data_synthetic_data_budget_size(percentage_of_db)
                        execute_computations(dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename)
                    else:
                        print('Exit program')
                        sys.exit(0)
    else:
        # Real data experiments
        text = input("Run experiments on Flights data, Photo data, Wikidata (1,2,3): ")
        if text == "1":
            percentage_of_db = float(input("db percentage: (0.25,0.5,0.75,1): "))
            percentage_of_ql = float(input("ql percentage: (0.25,0.5,0.75,1): "))
            budget = float(input("budget: (0.1,0.25,0.5,0.75) or in absolute terms: "))
            n_iterations = int(input("Number of SCG iterations (2000, 10000, 50000, 100000): "))
            dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename = read_flights_data(percentage_of_db, percentage_of_ql, budget, n_iterations)
            execute_computations(dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename, n_iterations=n_iterations)
        elif text == "2":
            percentage_of_db = float(input("db percentage: (0.25,0.5,0.75,1): "))
            percentage_of_ql = float(input("ql percentage: (0.25,0.5,0.75,1): "))
            budget = float(input("budget: (0.1,0.25,0.5,0.75) or in absolute terms: "))
            n_iterations = int(input("Number of SCG iterations (2000, 10000, 50000, 100000): "))
            dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename = read_photo_data(percentage_of_db, percentage_of_ql, budget, n_iterations)
            execute_computations(dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename, jaccard_sim=False, n_iterations=n_iterations)
        elif text == "3":
            percentage_of_db = float(input("db percentage: (0.25,0.5,0.75,1): "))
            percentage_of_ql = float(input("ql percentage: (0.25,0.5,0.75,1): "))
            budget = float(input("budget: (0.1,0.25,0.5,0.75) or in absolute terms: "))
            n_iterations = int(input("Number of SCG iterations (2000, 10000, 50000, 100000): "))
            dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename = read_wiki_data(percentage_of_db, percentage_of_ql, budget, n_iterations)
            execute_computations(dataset, n_rows, n_queries, queries, prob_queries, budget, results_filename, jaccard_sim=False, n_iterations=n_iterations)
        else:
            print('Exit program')
            sys.exit(0)
    #draw_plots_experiments()
    """

    # dataset_choice in [flight, photo, wiki]
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
    av_stdevs_calculation = bool(int(sys.argv[6]))
    # See query-log diversity
    #print(f"Standard deviation of pairwise sims in {dataset_choice} data: {compute_average_stdevs(dataset_choice, percentage_of_db, percentage_of_ql, budget, n_iterations)}")

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
