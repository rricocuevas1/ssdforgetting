import random
import csv
import os
import dask.dataframe as dd


def generate_synthetic_data(n_rows, n_queries):
    n_tuples_per_query = 10
    n_components_per_tuple = 100
    
    # Generate datasets
    with open(f"sample_data/synthetic/data_{n_rows}_{n_queries}.csv", 'w', newline='') as file:
        counter = 0
        writer = csv.writer(file)
        writer.writerow([f'c{i}' for i in range(n_components_per_tuple)]) # 100 columns
        for i in range(n_rows//n_tuples_per_query):
            for j in range(n_tuples_per_query):
                random.seed(i * j + i + j)
                writer.writerow([counter] + [random.random() for _ in range(n_components_per_tuple - 1)])
            counter = counter + 1
    file.close()
    print(f"Generated: sample_data/synthetic/data_{n_rows}_{n_queries}.csv")
    
    # Generate query_logs
    with open(f"sample_data/synthetic/queries_{n_rows}_{n_queries}.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(n_queries):
            random.seed(i)
            counter = random.choice(range(0, n_rows, 10))
            writer.writerow([i for i in range(counter, counter + n_tuples_per_query)])
    file.close()
    print(f"Generated: sample_data/synthetic/queries_{n_rows}_{n_queries}.csv")


def convert_files_to_parquet(directory_path, csv_list):
    for filename in csv_list:
        csv_filepath = os.path.join(directory_path, filename)
        parquet_filename = os.path.splitext(filename)[0] + ".parquet"
        parquet_filepath = os.path.join(directory_path, parquet_filename)

        ddf = dd.read_csv(csv_filepath, header=None)
        ddf.columns = [str(col) for col in ddf.columns]
        ddf.to_parquet(parquet_filepath)

        print(f"Successfully converted '{csv_filepath}' to single Parquet file '{parquet_filepath}'")


# Synthetic data (Generate datasets and logs)
#os.makedirs("sample_data/synthetic", exist_ok=True)
#generate_synthetic_data(n_rows=1000000,   n_queries=10000000)
#generate_synthetic_data(n_rows=10000000,  n_queries=10000000)
#generate_synthetic_data(n_rows=100000000, n_queries=10000000)
#generate_synthetic_data(n_rows=100000000, n_queries=1000000)
#generate_synthetic_data(n_rows=100000000, n_queries=100000)