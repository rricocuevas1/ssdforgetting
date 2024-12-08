# Stochastic Submodular Data Forgetting
This repository contains the code and data of the paper Stochastic Submodular Data Forgetting.

## Requirements
```
pip install scikit-learn
pip install pandas
pip install statistics
pip install numpy
```
## Data Download
REAL DATASETS: The 3 real datatasets are hosted on Google Drive. You can download it using the following link: 
- [Download Data](https://drive.google.com/file/d/1YjCt-RZUyEHslqmA3yJHJi-Tk6SNFlbP/view?usp=sharing)

Once you download it please un-zip it and place it in the same directory as the source files.

SYNTHETIC DATASETS: To generate the 5 synthetic datasets please run:
```
python3 synthetic_data_generation.py
```

## Experiment reproducibility
In order to replicate our experiments please run the following command: 
```
chmod +x run_tmux_sessions.sh
./run_tmux_sessions.sh
```
This will run every experiment 10 times. To integrate the results, please run the following command:
```
python process_results.py
```
This will create the final solution files for each one of the experiments. Each file containins the standard deviation and average of the quality and runtime for IndepDF, DepDF, LAZY GREEDY, and QUERY-BASED-AMNESIA for the corresponding experiment described by each one of the file names.
## General Usage
In order to run `IndepDF` and `DepDF` (this paper) vs `LAZY GREEDY` and `QUERY-BASED-AMNESIA` (baselines) please execute the following command:
```
python main.py [dataset_choice] [percentage_of_db] [percentage_of_ql] [budget] [n_iterations] [av_stdevs_calculation] [only_time]
```
The command line arguments correspond to:
- `[dataset_choice]`: The desired dataset $D$ inside the `sample_data` folder. Select one from the list [flight, photo, wiki].
- `[percentage_of_db]`: The percentage of $D$ to use as input data. Select a number inside the continuous interval [0, 1].
- `[percentage_of_ql]`: The percentage of queries from the corresponding query-log $Q$ to use as input log. Select a number inside the continuous interval [0, 1].
- `[budget]`: The budget $B$ is the percentage of $D$ to be kept. Select a number inside the continuous interval [0,1].
- `[n_iterations]`: The number of gradient ascent iterations $T$ the `DepDF` routine will perform. Select a number from the list [2000, 10000, 50000, 100000].
- `[av_stdevs_calculation]`: Whether the average answer set diversity is computed or not. Select `0` (False) not to perform the calculation, and `1` (True) to perform it.
- `[only_time]`: Whether $f(D*)$ is evaluated or not for solution $D*$ or only the time taken to build $D*$ is reported. Select `0` (False) to return both the time and function evaluation and `1` (True) to just return the time.

An example is given in the code snippet below,
```
python3 main.py flight 1 0.25 0.01 2000 0 0
```
In this example $D$ equals the full flights dataset, $Q$ is the 25% of the query-log, $B$ is 1% of $|D|$, $T= 2000$, the average answer set diversity is not computed, and both the time taken to build $D*$ and $f(D*)$ are reported.
