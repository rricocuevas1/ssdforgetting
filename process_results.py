import glob
import pandas as pd
import numpy as np
import os


n_rows = {
    'flight': 1200,
    'photo': 41620,
    'wiki': 131148
}

combinations = [
    "flight 1 1 0.1 10000 False False",
    "flight 1 1 0.25 10000 False False",
    "flight 1 1 0.25 25000 False False",
    "flight 1 1 0.25 50000 False False",
    "flight 1 1 0.25 100000 False False",
    "flight 1 1 0.5 10000 False False",
    "photo 1 1 0.01 10000 False False",
    "photo 1 1 0.02 10000 False False",
    "photo 1 1 0.05 10000 False False",
    "photo 1 1 0.1 10000 False False",
    "photo 1 1 0.25 10000 False False",
    "photo 1 1 0.5 10000 False False",
    "wiki 1 1 0.1 10000 False False",
    "wiki 1 1 0.25 10000 False False",
    "wiki 1 1 0.5 10000 False False"
]

base_dir = './sample_data/real'

def generate_pattern(combination):
    parts = combination.split()
    dataset_type, db, ql, budget, iterations, av, onlytime = parts
    pattern = os.path.join(base_dir, f"results_{dataset_type}%db{db}_%ql{ql}_budget{budget}_iterations{iterations}_av{av}_onlytime{onlytime}_*")
    return pattern


def find_matching_files(pattern):
    return glob.glob(pattern)


def process_files(files, onlytime):
    data_frames = []

    for file in files:
        df = pd.read_csv(file)
        # Replace -1 with NaN
        df.replace(-1, np.nan, inplace=True)
        data_frames.append(df)

    combined_df = pd.concat(data_frames)

    if onlytime:
        # Aggregate Time only
        aggregated_df = combined_df.groupby('Algorithm')[' Time'].agg(['mean', 'std']).reset_index()
        aggregated_df.columns = ['Algorithm', 'Time_mean', 'Time_std']
    else:
        # Aggregate both Time and Utility
        aggregated_df = combined_df.groupby('Algorithm')[[' Time', ' Utility']].agg(['mean', 'std']).reset_index()
        aggregated_df.columns = ['Algorithm', 'Time_mean', 'Time_std', 'Utility_mean', 'Utility_std']

    return aggregated_df


for i, combination in enumerate(combinations):
    parts = combination.split()
    dataset_type = parts[0]
    budget = float(parts[3])
    if budget < 1:
        new_budget = int(round(n_rows[dataset_type] * budget))
    else:
        new_budget = int(budget)

    # Replace '1' with '1.0'
    updated_parts = [part if part != '1' else '1.0' for part in parts]

    # Update budget with new value
    updated_parts[3] = str(new_budget)

    # Update the combination in the list
    combinations[i] = ' '.join(updated_parts)
for combination in combinations:
    pattern = generate_pattern(combination)
    matching_files = find_matching_files(pattern)
    if not matching_files:
        continue
    parts = combination.split()
    onlytime = parts[-1] == 'True'
    aggregated_df = process_files(matching_files, onlytime)
    output_filename = f"results_{pattern.replace('*', '').replace('results_', '').replace(base_dir + '/', '')}.csv"
    aggregated_df.to_csv(os.path.join(base_dir, output_filename), index=False)
    print(f"Created {output_filename}")


