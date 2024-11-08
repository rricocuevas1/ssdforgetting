import matplotlib.pyplot as plt
import numpy as np


def draw_plots_experiments():
    # FIGURE 2A: QUALITY PERFORMANCE for changing budget Flights data
    # Data for x-axis and y-axis (mean and standard deviation)
    x = [0.1, 0.25, 0.5]
    y_means = {
        'DepDF': [0.756291117379689, 0.8958379223015223, 0.9644257050715419],
        'IndepDF': [0.831837735925193, 0.9334995163230462, 0.9789635349635353],
        'QB-Amnesia': [0.37674033856952194, 0.6431243994763717, 0.8709434808519834],
        'LAZY GREEDY + FAST NN': [0.8323337801421676, 0.932794138676492, 0.9787284427284432],
        'LAZY GREEDY': [0.8333490674638844, 0.937642651054416, 0.9810604890604896]
    }
    y_stdevs = {
        'DepDF': [0.010029722175809854, 0.010034358044083687, 0.0032836134848875684],
        'IndepDF': [0, 0, 0],
        'QB-Amnesia': [0.058990085943771274, 0.040889401269470375, 0.017915962148619277],
        'LAZY GREEDY + FAST NN': [0, 0, 0],
        'LAZY GREEDY': [0, 0, 0]
    }

    # Colors for the bars
    colors = {
        'DepDF': '#1E90FF',  # Dark Blue
        'IndepDF': '#87CEFA',  # Light Blue
        'QB-Amnesia': '#FFD700',  # Softer Yellow (Amber)
        'LAZY GREEDY + FAST NN': '#B22222',  # Dark Burgundy Red
        'LAZY GREEDY': '#FF8C00'  # Orange
    }

    # Bar width and position settings
    width = 0.15
    x_pos = np.arange(len(x))

    # Create figure and axis
    fig, ax = plt.subplots()

    # Plot each bar group using a loop to avoid repetition
    for i, (label, color) in enumerate(colors.items()):
        ax.bar(x_pos + (i - 2) * width, y_means[label], width,
            yerr=y_stdevs[label], capsize=5, label=label, color=color)

    # Axis labels and ticks
    ax.set_xlabel("Budget (percentage of database)")
    ax.set_ylabel("Quality percentage")
    ax.set_xticks(x_pos)
    xtick_labels = ['0.1', '0.25', '0.5']
    ax.set_xticklabels(xtick_labels)

    # Legend with ordered labels
    handles, labels = ax.get_legend_handles_labels()
    ordered_labels = ['DepDF', 'IndepDF', 'QB-Amnesia', 'LAZY GREEDY + FAST NN', 'LAZY GREEDY']
    ordered_handles = [handles[labels.index(label)] for label in ordered_labels]
    ax.legend(ordered_handles, ordered_labels, loc='best')

    # Save the figure
    plt.savefig('budget_size_vs_quality_flights.png')
    plt.close(fig)
    

    # FIGURE 2D: TIME PERFORMANCE for changing budget Flights data
    # Data
    x = [0.1, 0.25, 0.5]
    y_means = {
        'DepDF': [5.726467895507812, 7.405186295509338, 7.631312584877014],
        'IndepDF': [0.00073032379150387, 0.0007942676544188899, 0.00075559616088861],
        'QB-Amnesia': [0.00119578838348384, 0.0019113302230834499, 0.00200409889221186],
        'LAZY GREEDY + FAST NN': [301.4856743335724, 618.0088408470153, 1132.1897844076157],
        'LAZY GREEDY': [1060.9508843183517, 4922.1659584283825, 12750.733463954926]
    }
    y_stdevs = {
        'DepDF': [1.780144507090582, 1.1557413791327562, 1.120771075070531],
        'IndepDF': [0.00014232285864291066, 6.690719949385502e-05, 6.907072146464752e-05],
        'QB-Amnesia': [0.0003873814568475775, 0.0002685314676366417, 0.00024659478924008235],
        'LAZY GREEDY + FAST NN': [111.99027104942178, 87.0868825770274, 430.08769839285344],
        'LAZY GREEDY': [309.2995539981396, 792.6504212799819, 1748.5249800101983]

    }
    colors = {
        'DepDF': '#1E90FF',  # Dark Blue
        'IndepDF': '#87CEFA',  # Light Blue
        'QB-Amnesia': '#FFD700',  # Softer Yellow (Amber)
        'LAZY GREEDY': '#FF8C00',  # Orange
        'LAZY GREEDY + FAST NN': '#B22222'  # Dark Burgundy Red
    }

    # Plot configuration
    width = 0.15
    x_pos = np.arange(len(x))
    fig, ax = plt.subplots()

    # Plot each bar group
    for i, label in enumerate(y_means.keys()):
        ax.bar(x_pos + (i - len(y_means) // 2) * width, y_means[label], width,
            yerr=y_stdevs[label], capsize=5, label=label, color=colors[label])

    # Logarithmic y-axis
    ax.set_yscale('log')

    # Add horizontal lines for 1 second, 1 minute, 1 hour, 1 day
    seconds_in_second = 1
    seconds_in_minute = 60 
    seconds_in_hour = 60 * 60
    seconds_in_day = 60 * 60 * 24

    ax.axhline(seconds_in_second, color='gray', linestyle='--', linewidth=1)
    ax.text(len(x) - 0.5, seconds_in_second, '1 second', color='gray', va='bottom', ha='right')

    ax.axhline(seconds_in_minute, color='gray', linestyle='--', linewidth=1)
    ax.text(len(x) - 0.5, seconds_in_minute, '1 minute', color='gray', va='bottom', ha='right')

    ax.axhline(seconds_in_hour, color='gray', linestyle='--', linewidth=1)
    ax.text(len(x) - 0.5, seconds_in_hour, '1 hour', color='gray', va='bottom', ha='right')

    ax.axhline(seconds_in_day, color='gray', linestyle='--', linewidth=1)
    ax.text(len(x) - 0.5, seconds_in_day, '1 day', color='gray', va='bottom', ha='right')


    # Labels and ticks
    ax.set_xlabel("Budget (percentage of database)")
    ax.set_ylabel("Computation time (seconds)")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(['0.1', '0.25', '0.5'])

    # Legend handling
    handles, labels = ax.get_legend_handles_labels()
    ordered_handles = [handles[labels.index(label)] for label in labels]
    ax.legend(ordered_handles, labels, loc='best')

    # Save the figure
    plt.savefig('budget_size_vs_time_flights.png')
    plt.close(fig)
    

    # FIGURE 2B: QUALITY PERFORMANCE for changing budget Photo data
    
    x = [0.02, 0.05, 0.1]
    y_means = {
        'DepDF': [0.7529144067416605, 0.8592212239455334, 0.9141553299669113],
        'IndepDF': [0.6222263616367543, 0.8339073127319698, 0.9246819972204507],
        'QB-Amnesia': [0.6345710530474259, 0.7728529206380468, 0.8668758855501959],
        'LAZY GREEDY + FAST NN': [0.6815134829784272, 0.8604175109884135, 0.9402255571659849],
        'LAZY GREEDY': [np.nan, np.nan, np.nan]
    }
    y_stdevs = {
        'DepDF': [0.00587044106978651, 0.004721395393394939, 0.004593613848662287],
        'IndepDF': [0, 0, 0],
        'QB-Amnesia': [0.009714436331491333, 0.007787575957518025, 0.004333412157248837],
        'LAZY GREEDY + FAST NN': [0.00883673280028652, 0.0047320173892094605, 0.002435500599698396],
        'LAZY GREEDY': [np.nan, np.nan, np.nan]
    }

    # Colors for the bars
    colors = {
        'DepDF': '#1E90FF',  # Dark Blue
        'IndepDF': '#87CEFA',  # Light Blue
        'QB-Amnesia': '#FFD700',  # Softer Yellow (Amber)
        'LAZY GREEDY': '#FF8C00',  # Orange
        'LAZY GREEDY + FAST NN': '#B22222'  # Dark Burgundy Red
    }

    # Define an explicit ordered list of labels
    ordered_labels = ['DepDF', 'IndepDF', 'QB-Amnesia', 'LAZY GREEDY + FAST NN', 'LAZY GREEDY']

    # Bar width and position settings
    width = 0.15
    x_pos = np.arange(len(x))

    # Create figure and axis
    fig, ax = plt.subplots()

    # Plot each bar group using a loop with an explicit order
    for i, label in enumerate(ordered_labels):
        ax.bar(x_pos + (i - (len(ordered_labels) // 2)) * width, y_means[label], width,
            yerr=y_stdevs[label], capsize=5, label=label, color=colors[label])

    # Axis labels and ticks
    ax.set_xlabel("Budget (percentage of database)")
    ax.set_ylabel("Quality percentage")
    ax.set_xticks(x_pos)
    xtick_labels = ['0.02', '0.05', '0.1']
    ax.set_xticklabels(xtick_labels)

    # Legend with ordered labels
    handles, labels = ax.get_legend_handles_labels()
    ordered_handles = [handles[labels.index(label)] for label in ordered_labels]
    ax.legend(ordered_handles, ordered_labels, loc='best')

    # Save the figure
    plt.savefig('budget_size_vs_quality_photos.png')
    plt.close(fig)
    

    # FIGURE 2E: TIME PERFORMANCE for changing budget Photo data
    
    # Data for x-axis and y-axis (mean and standard deviation)
    x = [0.02, 0.05, 0.1]
    y_means = {
        'DepDF': [399.5396808385849, 357.94043333530425, 225.50409071445466],
        'IndepDF': [0.00436940193176263, 0.00381395816802974, 0.00425946712493892],
        'QB-Amnesia': [0.015866589546203562, 0.0084659099578857, 0.01798729896545405],
        'LAZY GREEDY + FAST NN': [158610.49799060822, 187100.0584590435, 213926.5086236795],
        'LAZY GREEDY': [np.nan, np.nan, np.nan]
    }
    y_stdevs = {
        'DepDF': [15.536409458869402, 19.097708278238215, 33.736453526933644],
        'IndepDF': [0.0011964165966327864, 0.0006129152981777414, 0.0007949028003025106],
        'QB-Amnesia': [0.009763948556346299, 0.0014060564159351055, 0.013015877021395898],
        'LAZY GREEDY + FAST NN': [70118.95527826565, 53983.850338683915, 10060.51381531734],
        'LAZY GREEDY': [np.nan, np.nan, np.nan]
    }

    # Colors for the bars
    colors = {
        'DepDF': '#1E90FF',  # Dark Blue
        'IndepDF': '#87CEFA',  # Light Blue
        'QB-Amnesia': '#FFD700',  # Softer Yellow (Amber)
        'LAZY GREEDY': '#FF8C00',  # Orange
        'LAZY GREEDY + FAST NN': '#B22222'  # Dark Burgundy Red
    }

    # Define an explicit ordered list of labels
    ordered_labels = ['DepDF', 'IndepDF', 'QB-Amnesia', 'LAZY GREEDY + FAST NN', 'LAZY GREEDY']

    # Bar width and position settings
    width = 0.15
    x_pos = np.arange(len(x))

    # Create figure and axis
    fig, ax = plt.subplots()

    # Plot each bar group using a loop with an explicit order
    for i, label in enumerate(ordered_labels):
        ax.bar(x_pos + (i - (len(ordered_labels) // 2)) * width, y_means[label], width,
            yerr=y_stdevs[label], capsize=5, label=label, color=colors[label])

    # Logarithmic y-axis
    ax.set_yscale('log')

    # Add horizontal lines for key time markers (1 second, 1 minute, 1 hour, 1 day)
    seconds_in_second = 1
    seconds_in_minute = 60
    seconds_in_hour = 60 * 60
    seconds_in_day = 60 * 60 * 24

    ax.axhline(seconds_in_second, color='gray', linestyle='--', linewidth=1)
    ax.text(len(x) - 0.5, seconds_in_second, '1 second', color='gray', va='bottom', ha='right')

    ax.axhline(seconds_in_minute, color='gray', linestyle='--', linewidth=1)
    ax.text(len(x) - 0.5, seconds_in_minute, '1 minute', color='gray', va='bottom', ha='right')

    ax.axhline(seconds_in_hour, color='gray', linestyle='--', linewidth=1)
    ax.text(len(x) - 0.5, seconds_in_hour, '1 hour', color='gray', va='bottom', ha='right')

    ax.axhline(seconds_in_day, color='gray', linestyle='--', linewidth=1)
    ax.text(len(x) - 0.5, seconds_in_day, '1 day', color='gray', va='bottom', ha='right')

    # Axis labels and ticks
    ax.set_xlabel("Budget (percentage of database)")
    ax.set_ylabel("Computation time (seconds)")
    ax.set_xticks(x_pos)
    xtick_labels = ['0.02', '0.05', '0.1']
    ax.set_xticklabels(xtick_labels)

    # Legend with ordered labels
    handles, labels = ax.get_legend_handles_labels()
    ordered_handles = [handles[labels.index(label)] for label in ordered_labels]
    ax.legend(ordered_handles, ordered_labels, loc='best')

    # Save the figure
    plt.savefig('budget_size_vs_time_photos.png')
    plt.close(fig)
    

    # FIGURE 2C: QUALITY PERFORMANCE for changing budget Wiki data
    # Data for x-axis and y-axis (mean and standard deviation)
    x = [0.1, 0.25, 0.5]
    y_means = {
        'DepDF': [0.6967402485053181, 0.8350008318515467, 0.9118017865415355],
        'IndepDF': [0.8548548681719849, 0.9368025250538364, 0.9802769684440538],
        'QB-Amnesia': [0.6797316315571285, 0.8169441370623195, 0.9122563170717986],
        'LAZY GREEDY + FAST NN': [np.nan, np.nan, np.nan],
        'LAZY GREEDY': [np.nan, np.nan, np.nan]
    }
    y_stdevs = {
        'DepDF': [0.004836356339030948, 0.007121330633450144, 0.003401627587109086],
        'IndepDF': [0, 0, 0],
        'QB-Amnesia': [0.0048742497798597555, 0.0039578153732793275, 0.0015658540977650745],
        'LAZY GREEDY + FAST NN': [np.nan, np.nan, np.nan],
        'LAZY GREEDY': [np.nan, np.nan, np.nan]
    }

    # Colors for the bars
    colors = {
        'DepDF': '#1E90FF',  # Dark Blue
        'IndepDF': '#87CEFA',  # Light Blue
        'QB-Amnesia': '#FFD700',  # Softer Yellow (Amber)
        'LAZY GREEDY': '#FF8C00',  # Orange
        'LAZY GREEDY + FAST NN': '#B22222'  # Dark Burgundy Red
    }

    # Define an explicit ordered list of labels
    ordered_labels = ['DepDF', 'IndepDF', 'QB-Amnesia', 'LAZY GREEDY + FAST NN', 'LAZY GREEDY']

    # Bar width and position settings
    width = 0.15
    x_pos = np.arange(len(x))

    # Create figure and axis
    fig, ax = plt.subplots()

    # Plot each bar group using a loop with an explicit order
    for i, label in enumerate(ordered_labels):
        ax.bar(x_pos + (i - (len(ordered_labels) // 2)) * width, y_means[label], width,
            yerr=y_stdevs[label], capsize=5, label=label, color=colors[label])

    # Axis labels and ticks
    ax.set_xlabel("Budget (percentage of database)")
    ax.set_ylabel("Quality percentage")
    ax.set_xticks(x_pos)
    xtick_labels = ['0.1', '0.25', '0.5']
    ax.set_xticklabels(xtick_labels)

    # Legend with ordered labels
    handles, labels = ax.get_legend_handles_labels()
    ordered_handles = [handles[labels.index(label)] for label in ordered_labels]
    ax.legend(ordered_handles, ordered_labels, loc='best')

    # Save the figure
    plt.savefig('budget_size_vs_quality_wiki.png')
    plt.close(fig)

    
    # FIGURE 2F: TIME PERFORMANCE for changing budget Wiki data
   
    # Data for x-axis and y-axis (mean and standard deviation)
    x = [0.1, 0.25, 0.5]
    y_means = {
        'DepDF': [232.3884106874466, 222.2639479637146, 236.57969160079955],
        'IndepDF': [0.12318415641784666, 0.11725423071119516, 0.1418429851531982],
        'QB-Amnesia': [0.1029222965240478, 0.11834051873948834, 0.11749706268310542],
        'LAZY GREEDY + FAST NN': [np.nan, np.nan, np.nan],
        'LAZY GREEDY': [np.nan, np.nan, np.nan]
    }
    y_stdevs = {
        'DepDF': [29.395251893480108, 38.511094584452756, 18.891902310301017],
        'IndepDF': [0.03401127613615488, 0.03322741287814581, 0.02245917594596426],
        'QB-Amnesia': [0.03357951757009398, 0.0351685105186319, 0.026333783868162562],
        'LAZY GREEDY + FAST NN': [np.nan, np.nan, np.nan],
        'LAZY GREEDY': [np.nan, np.nan, np.nan]
    }

    # Colors for the bars
    colors = {
        'DepDF': '#1E90FF',  # Dark Blue
        'IndepDF': '#87CEFA',  # Light Blue
        'QB-Amnesia': '#FFD700',  # Softer Yellow (Amber)
        'LAZY GREEDY': '#FF8C00',  # Orange
        'LAZY GREEDY + FAST NN': '#B22222'  # Dark Burgundy Red
    }

    # Define an explicit ordered list of labels
    ordered_labels = ['DepDF', 'IndepDF', 'QB-Amnesia', 'LAZY GREEDY + FAST NN', 'LAZY GREEDY']

    # Bar width and position settings
    width = 0.15
    x_pos = np.arange(len(x))

    # Create figure and axis
    fig, ax = plt.subplots()

    # Plot each bar group using a loop with an explicit order
    for i, label in enumerate(ordered_labels):
        ax.bar(x_pos + (i - (len(ordered_labels) // 2)) * width, y_means[label], width,
            yerr=y_stdevs[label], capsize=5, label=label, color=colors[label])

    # Logarithmic y-axis
    ax.set_yscale('log')

    # Add horizontal lines for key time markers (1 second, 1 minute, 1 hour, 1 day)
    seconds_in_second = 1
    seconds_in_minute = 60
    seconds_in_hour = 60 * 60
    seconds_in_day = 60 * 60 * 24

    ax.axhline(seconds_in_second, color='gray', linestyle='--', linewidth=1)
    ax.text(len(x) - 0.5, seconds_in_second, '1 second', color='gray', va='bottom', ha='right')

    ax.axhline(seconds_in_minute, color='gray', linestyle='--', linewidth=1)
    ax.text(len(x) - 0.5, seconds_in_minute, '1 minute', color='gray', va='bottom', ha='right')

    ax.axhline(seconds_in_hour, color='gray', linestyle='--', linewidth=1)
    ax.text(len(x) - 0.5, seconds_in_hour, '1 hour', color='gray', va='bottom', ha='right')

    ax.axhline(seconds_in_day, color='gray', linestyle='--', linewidth=1)
    ax.text(len(x) - 0.5, seconds_in_day, '1 day', color='gray', va='bottom', ha='right')

    # Axis labels and ticks
    ax.set_xlabel("Budget (percentage of database)")
    ax.set_ylabel("Computation time (seconds)")
    ax.set_xticks(x_pos)
    xtick_labels = ['0.1', '0.25', '0.5']
    ax.set_xticklabels(xtick_labels)

    # Legend with ordered labels
    handles, labels = ax.get_legend_handles_labels()
    ordered_handles = [handles[labels.index(label)] for label in ordered_labels]
    ax.legend(ordered_handles, ordered_labels, loc='best')

    # Save the figure
    plt.savefig('budget_size_vs_time_wikidata.png')
    plt.close(fig)
    







    
    


    # FIGURE 1I: QUALITY PERFORMANCE for changing answer set diversity flights
    """
    x = [0.05757007029485365, 0.04869947495850181, 0.04445579754164265, 0.03708746644665503]
    y_indepdf_mean = [0.4918871252204585, 0.3459151649016848, 0.2829237140306155, 0.3226167498192457]
    y_lazy_greedy_mean = [0.5310405643738977, 0.3729346299094648, 0.3031722532956105, 0.332064183917135]
    y_indep = [lg - knap for lg, knap in zip(y_lazy_greedy_mean, y_indepdf_mean)]
    plt.plot(x, y_indep, color='k', marker='o', lw=1, label='Quality difference (LAZZY GREEDY vs IndepDF)', linestyle='solid')
    plt.xlabel("Answer set diversity")
    plt.ylabel("Quality percentage")
    custom_labels = ["25%", "50%", "75%", "100%"]
    for i, txt in enumerate(custom_labels):
        plt.text(x[i] - 0.001, y_indep[i], txt, ha='left', va='bottom')
    plt.gca().invert_xaxis()
    plt.legend()
    plt.savefig('answer_set_diversity_flights.png')
    """
    """
    x = [0.05757007029485365, 0.04869947495850181, 0.04445579754164265, 0.03708746644665503]
    y_indepdf_mean = [0.4918871252204585, 0.3459151649016848, 0.2829237140306155, 0.3226167498192457]
    y_lazy_greedy_mean = [0.5310405643738977, 0.3729346299094648, 0.3031722532956105, 0.332064183917135]

    # Both standard deviations are zero
    y_indepdf_stdev = [0, 0, 0, 0]
    y_lazy_greedy_stdev = [0, 0, 0, 0]

    # Calculate the quality difference
    y_indep = [lg - knap for lg, knap in zip(y_lazy_greedy_mean, y_indepdf_mean)]

    # Calculate the standard deviation of the differences
    y_indep_stdev = [np.sqrt(indepdf_stdev ** 2 + lazy_greedy_stdev ** 2)
                     for indepdf_stdev, lazy_greedy_stdev in zip(y_indepdf_stdev, y_lazy_greedy_stdev)]

    # Plot the quality difference
    fig, ax = plt.subplots()
    ax.plot(x, y_indep, color='k', marker='o', lw=1, label='Quality difference (LAZY GREEDY vs IndepDF)',
            linestyle='solid')

    # Add standard deviation bands around the differences
    y_indep_upper = [mean_diff + stdev for mean_diff, stdev in zip(y_indep, y_indep_stdev)]
    y_indep_lower = [mean_diff - stdev for mean_diff, stdev in zip(y_indep, y_indep_stdev)]

    # Plot the standard deviation bands as shaded areas
    ax.fill_between(x, y_indep_lower, y_indep_upper, color='gray', alpha=0.3, label='±1 Stdev around difference')

    # Add labels and legend
    ax.set_xlabel("Answer set diversity")
    ax.set_ylabel("Quality percentage")
    custom_labels = ["25%", "50%", "75%", "100%"]
    for i, txt in enumerate(custom_labels):
        ax.text(x[i] - 0.001, y_indep[i], txt, ha='left', va='bottom')
    ax.invert_xaxis()
    ax.legend()

    # Save the figure
    plt.savefig('answer_set_diversity_flights.png')
    """
    # Time:
    """
    x = [0.05757007029485365, 0.04869947495850181, 0.04445579754164265, 0.03708746644665503]
    y_indepdf_mean = [0.020146632194519, 0.09436266422271725, 0.1130238533020019, 0.28652322292327875]
    y_indepdf_stdev = [0.01810025577836352, 0.034847092791935826, 0.030844582430277635, 0.14615016357596305]
    y_lazy_greedy_mean = [25.36024193763733, 178.26411006450653, 386.23613221645354, 6918.408770227432]
    y_lazy_greedy_stdev = [2.933120082433946, 33.82403836354893, 100.11832662634187, 2908.460126168839]
    colors = {
        'DepDF': '#1E90FF',
        'IndepDF': '#87CEFA',
        'QB-Amnesia': '#FFD700',
        'LAZY GREEDY': '#FFA500'
    }
    width = 0.15

    # Create a list of tuples and sort based on x in the order you provided
    data = list(zip(x, y_indepdf_mean, y_indepdf_stdev, y_lazy_greedy_mean, y_lazy_greedy_stdev))
    data_sorted = sorted(data, key=lambda d: x.index(d[0]))

    # Unpack sorted data
    x_sorted, y_indepdf_mean_sorted, y_indepdf_stdev_sorted, y_lazy_greedy_mean_sorted, y_lazy_greedy_stdev_sorted = zip(
        *data_sorted)

    x_pos = np.arange(len(x_sorted))

    fig, ax = plt.subplots()
    ax.bar(x_pos - 0.5 * width, y_indepdf_mean_sorted, width, yerr=y_indepdf_stdev_sorted, capsize=5, label='IndepDF',
           color=colors['IndepDF'])
    ax.bar(x_pos + 0.5 * width, y_lazy_greedy_mean_sorted, width, yerr=y_lazy_greedy_stdev_sorted, capsize=5,
           label='LAZY GREEDY', color=colors['LAZY GREEDY'])

    # Add labels and legend
    ax.set_xlabel("Answer set diversity")
    ax.set_ylabel("Computation time (seconds)")
    ax.legend()
    ax.set_yscale('log')

    # Set x-axis tick labels to the original order
    ax.set_xticks(x_pos)
    ax.set_xticklabels(["0.057", "0.048", "0.044", "0.037"])  # Customize as needed

    plt.savefig('answer_set_diversity_flights_time.png')
    """

    # FIGURE 1H : QUALITY PERFORMANCE for changing answer set diversity photos
    """
    x = [0.10315621108423553, 0.09224688219124286, 0.08163194847127428, 0.07476247710140864, 0.0648838516706814]
    y_indepdf_mean = [0.1755818782416476, 0.1262003812271152, 0.1256306949466847, 0.1291627163092294, 0.11050876970271531]
    y_lazy_greedy_mean = [0.8223959313561867, 0.5137888907383809, 0.41156350597581615, 0.3333430159890074, 0.2760813254114178]
    y_indep = [lg - knap for lg, knap in zip(y_lazy_greedy_mean, y_indepdf_mean)]
    plt.plot(x, y_indep, color='k', marker='o', lw=1, label='Quality difference (LAZZY GREEDY vs IndepDF)',
             linestyle='solid')
    plt.xlabel("Answer set diversity")
    plt.ylabel("Quality percentage")
    custom_labels = ["10%", "25%", "50%", "75%", "100%"]
    for i, txt in enumerate(custom_labels):
        plt.text(x[i] - 0.001, y_indep[i], txt, ha='left', va='bottom')
    plt.gca().invert_xaxis()
    plt.legend()
    plt.savefig('answer_set_diversity_photos.png')
    """
    """
    x = [0.10315621108423553, 0.09224688219124286, 0.08163194847127428, 0.07476247710140864, 0.0648838516706814]
    y_indepdf_mean = [0.1755818782416476, 0.1262003812271152, 0.1256306949466847, 0.1291627163092294,
                      0.11050876970271531]
    y_lazy_greedy_mean = [0.8223959313561867, 0.5137888907383809, 0.41156350597581615, 0.3333430159890074,
                          0.2760813254114178]

    # Both standard deviations are zero
    y_indepdf_stdev = [0, 0, 0, 0, 0]
    y_lazy_greedy_stdev = [0, 0, 0, 0, 0]

    # Calculate the quality difference
    y_indep = [lg - knap for lg, knap in zip(y_lazy_greedy_mean, y_indepdf_mean)]

    # Calculate the standard deviation of the differences
    y_indep_stdev = [np.sqrt(indepdf_stdev ** 2 + lazy_greedy_stdev ** 2)
                     for indepdf_stdev, lazy_greedy_stdev in zip(y_indepdf_stdev, y_lazy_greedy_stdev)]

    # Plot the quality difference
    fig, ax = plt.subplots()
    ax.plot(x, y_indep, color='k', marker='o', lw=1, label='Quality difference (LAZY GREEDY vs IndepDF)',
            linestyle='solid')

    # Add standard deviation bands around the differences
    y_indep_upper = [mean_diff + stdev for mean_diff, stdev in zip(y_indep, y_indep_stdev)]
    y_indep_lower = [mean_diff - stdev for mean_diff, stdev in zip(y_indep, y_indep_stdev)]

    # Plot the standard deviation bands as shaded areas
    ax.fill_between(x, y_indep_lower, y_indep_upper, color='gray', alpha=0.3, label='±1 Stdev around difference')

    # Add labels and legend
    ax.set_xlabel("Answer set diversity")
    ax.set_ylabel("Quality percentage")
    custom_labels = ["10%", "25%", "50%", "75%", "100%"]
    for i, txt in enumerate(custom_labels):
        ax.text(x[i] - 0.001, y_indep[i], txt, ha='left', va='bottom')
    ax.invert_xaxis()
    ax.legend()

    # Save the figure
    plt.savefig('answer_set_diversity_photos.png')
    """
    # Time
    """
    x = [0.10315621108423553, 0.09224688219124286, 0.08163194847127428, 0.07476247710140864, 0.0648838516706814]
    y_indepdf_mean = [6.387770509719848, 15.572385334968567, 29.031080269813536, 62.13201577663422, 61.32027413845062]
    y_indepdf_stdev = [2.5974972435427977, 9.855898583892946, 20.10098484158, 27.52234817301281, 39.284658231277916]
    y_lazy_greedy_mean = [16731.49803445339, 18799.882577729226, 50024.369872665404, 56877.436311006546, 59309.16498684883]
    y_lazy_greedy_stdev = [7742.579054962955, 8734.130794839888, 12939.769360817243, 12292.97972166445, 14430.072265553837]
    colors = {
        'DepDF': '#1E90FF',
        'IndepDF': '#87CEFA',
        'QB-Amnesia': '#FFD700',
        'LAZY GREEDY': '#FFA500'
    }
    width = 0.15

    # Create a list of tuples and sort based on x in the order you provided
    data = list(zip(x, y_indepdf_mean, y_indepdf_stdev, y_lazy_greedy_mean, y_lazy_greedy_stdev))
    data_sorted = sorted(data, key=lambda d: x.index(d[0]))

    # Unpack sorted data
    x_sorted, y_indepdf_mean_sorted, y_indepdf_stdev_sorted, y_lazy_greedy_mean_sorted, y_lazy_greedy_stdev_sorted = zip(
        *data_sorted)

    x_pos = np.arange(len(x_sorted))

    fig, ax = plt.subplots()
    ax.bar(x_pos - 0.5 * width, y_indepdf_mean_sorted, width, yerr=y_indepdf_stdev_sorted, capsize=5, label='IndepDF',
           color=colors['IndepDF'])
    ax.bar(x_pos + 0.5 * width, y_lazy_greedy_mean_sorted, width, yerr=y_lazy_greedy_stdev_sorted, capsize=5,
           label='LAZY GREEDY', color=colors['LAZY GREEDY'])

    # Add labels and legend
    ax.set_xlabel("Answer set diversity")
    ax.set_ylabel("Computation time (seconds)")
    ax.legend()
    ax.set_yscale('log')

    # Set x-axis tick labels to the original order
    ax.set_xticks(x_pos)
    ax.set_xticklabels(["0.103", "0.092", "0.081", "0.074", "0.064"])  # Customize as needed

    plt.savefig('answer_set_diversity_photos_time.png')
    """
    # FIGURE 1B: QUALITY PERFORMANCE for changing T
    # Flights (quality) difference representation
    """
    x = [2000, 10000, 50000, 100000]
    y_dep_df_mean = [0.7512452094599877, 0.7945709845180791, 0.8185961482998743, 0.8232129643503902]
    y_dep_df_stdev = [0.014696250234060874, 0.007391106064155793, 0.0025277435610194187, 0.002895342248182652]
    y_lazy_greedy = [0.8333490674638844, 0.8333490674638844, 0.8333490674638844, 0.8333490674638844]
    y_lazy_greedy_stdev = [0,0,0,0]
    y = [lg - knap for lg, knap in zip(y_lazy_greedy, y_dep_df_mean)]
    # Calculate the quality difference
    y_diff = [lg - knap for lg, knap in zip(y_lazy_greedy, y_dep_df_mean)]
    # Calculate the standard deviation of the differences
    y_diff_stdev = [np.sqrt(dep_df_stdev ** 2 + lazy_greedy_stdev ** 2)
                    for dep_df_stdev, lazy_greedy_stdev in zip(y_dep_df_stdev, y_lazy_greedy_stdev)]
    # Plot the quality difference
    fig, ax = plt.subplots()
    ax.plot(x, y_diff, color='black', marker='o', lw=1, label='Quality difference (LAZY GREEDY vs DepDF)',
            linestyle='solid')
    # Add standard deviation bands around the differences
    y_diff_upper = [mean_diff + stdev for mean_diff, stdev in zip(y_diff, y_diff_stdev)]
    y_diff_lower = [mean_diff - stdev for mean_diff, stdev in zip(y_diff, y_diff_stdev)]
    # Plot the standard deviation bands as shaded areas
    ax.fill_between(x, y_diff_lower, y_diff_upper, color='gray', alpha=0.3, label='±1 Stdev around difference')
    # Add labels and legend
    ax.set_xlabel("Number of DepDF iterations (T)")
    ax.set_ylabel("Quality percentage")
    custom_labels = ["T = 2K", "T = 10K", "T = 50K", "T = 100K"]
    for i, txt in enumerate(custom_labels):
        ax.text(x[i] + 1000, y_diff[i], txt, ha='left', va='bottom')
    ax.legend()
    plt.savefig('T_vs_quality_flights_difference.png')
    """
    # Flights data (time)
    """
    x = [2000, 10000, 50000, 100000]
    y_depdf_mean = [137.93595974445344, 756.7366755962372, 2633.746732544899, 6918.149991583824]
    y_depdf_stdev = [11.208084904702167, 12.224917040446192, 1010.6487461223672, 1333.1855009605583]
    #y_indepdf_mean = [0.1463512659072876, 0.1463512659072876,0.1463512659072876,0.1463512659072876]
    #y_indepdf_stdev = [0.054629057581267786, 0.054629057581267786,0.054629057581267786,0.054629057581267786]
    y_lazy_greedy_mean = [98975.70789148807, 98975.70789148807,98975.70789148807,98975.70789148807]
    y_lazy_greedy_stdev = [20483.671334775605, 20483.671334775605,20483.671334775605,20483.671334775605]
    #y_query_based_amnesia_mean = [0.3688062906265258,0.3688062906265258,0.3688062906265258,0.3688062906265258]
    #y_query_based_amnesia_stdev = [0.03263305540945669, 0.03263305540945669,0.03263305540945669,0.03263305540945669]
    colors = {
        'DepDF': '#1E90FF',
        'IndepDF': '#87CEFA',
        'QB-Amnesia': '#FFD700',
        'LAZY GREEDY': '#FFA500'
    }
    width = 0.15
    x_pos = np.arange(len(x))
    fig, ax = plt.subplots()
    ax.bar(x_pos - 0.5 * width, y_depdf_mean, width, yerr=y_depdf_stdev, capsize=5, label='DepDF',
           color=colors['DepDF'])
    #ax.bar(x_pos - 0.5 * width, y_indepdf_mean, width, yerr=y_indepdf_stdev, capsize=5, label='IndepDF',
    #       color=colors['IndepDF'])
    #ax.bar(x_pos + 0.5 * width, y_query_based_amnesia_mean, width, yerr=y_query_based_amnesia_stdev, capsize=5,
    #       label='QB-Amnesia', color=colors['QB-Amnesia'])
    ax.bar(x_pos + 0.5 * width, y_lazy_greedy_mean, width, yerr=y_lazy_greedy_stdev, capsize=5, label='LAZY GREEDY',
           color=colors['LAZY GREEDY'])
    ax.set_xlabel("Number of DepDF iterations (T)")
    ax.set_ylabel("Computation time (seconds)")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(["2000", "10000", "50000", "100000"])
    ax.legend()
    ax.set_yscale('log')
    plt.savefig('T_vs_quality_flights_time_bars.png')
    """
    # FIGURE 1F: QUALITY PERFORMANCE for changing T
    # Photos (quality) difference representation
    """
    x = [2000, 10000, 50000, 100000]
    y_dep_df_mean = [0.8738944322300177, 0.883406257805729, 0.8875091237012829, 0.8917735107707889]
    y_dep_df_stdev = [0.009530904418520603, 0.005558769563712488, 0.005013066554644355, 0.002885870473602826]
    y_lazy_greedy = [0.919123780112853, 0.919123780112853, 0.919123780112853, 0.919123780112853]
    y_lazy_greedy_stdev = [0, 0, 0, 0]
    # Calculate the quality difference
    y_diff = [lg - knap for lg, knap in zip(y_lazy_greedy, y_dep_df_mean)]
    # Calculate the standard deviation of the differences
    y_diff_stdev = [np.sqrt(dep_df_stdev ** 2 + lazy_greedy_stdev ** 2)
                    for dep_df_stdev, lazy_greedy_stdev in zip(y_dep_df_stdev, y_lazy_greedy_stdev)]
    # Plot the quality difference
    fig, ax = plt.subplots()
    ax.plot(x, y_diff, color='black', marker='o', lw=1, label='Quality difference (LAZY GREEDY vs DepDF)',
            linestyle='solid')
    # Add standard deviation bands around the differences
    y_diff_upper = [mean_diff + stdev for mean_diff, stdev in zip(y_diff, y_diff_stdev)]
    y_diff_lower = [mean_diff - stdev for mean_diff, stdev in zip(y_diff, y_diff_stdev)]
    # Plot the standard deviation bands as shaded areas
    ax.fill_between(x, y_diff_lower, y_diff_upper, color='gray', alpha=0.3, label='±1 Stdev around difference')
    # Add labels and legend
    ax.set_xlabel("Number of DepDF iterations (T)")
    ax.set_ylabel("Quality percentage")
    custom_labels = ["T = 2K", "T = 10K", "T = 50K", "T = 100K"]
    for i, txt in enumerate(custom_labels):
        ax.text(x[i] + 1000, y_diff[i], txt, ha='left', va='bottom')
    ax.legend()
    # Save the figure
    plt.savefig('T_vs_quality_photo_difference.png')
    """
    # Photo data (time)
    """
    x = [2000, 10000, 50000, 100000]
    y_depdf_mean = [1778.4869385957718, 9021.142050409317, 35098.20047278404, 56311.96686296463]
    y_depdf_stdev = [182.9736340945551, 996.7125144782416, 9365.874032419686, 14441.907247252424]
    #y_indepdf_mean = [5.743219161033631, 5.743219161033631, 5.743219161033631, 5.743219161033631]
    #y_indepdf_stdev = [0.8493934619048614, 0.8493934619048614, 0.8493934619048614, 0.8493934619048614]
    y_lazy_greedy_mean = [49850.32142627239, 49850.32142627239, 49850.32142627239, 49850.32142627239]
    y_lazy_greedy_stdev = [16070.593493545975, 16070.593493545975, 16070.593493545975, 16070.593493545975]
    #y_query_based_amnesia_mean = [6.416448640823364, 6.416448640823364, 6.416448640823364, 6.416448640823364]
    #y_query_based_amnesia_stdev = [1.93153631758539, 1.93153631758539, 1.93153631758539, 1.93153631758539]
    colors = {
        'DepDF': '#1E90FF',
        'IndepDF': '#87CEFA',
        'QB-Amnesia': '#FFD700',
        'LAZY GREEDY': '#FFA500'
    }
    width = 0.15
    x_pos = np.arange(len(x))
    fig, ax = plt.subplots()
    ax.bar(x_pos - 0.5 * width, y_depdf_mean, width, yerr=y_depdf_stdev, capsize=5, label='DepDF',
           color=colors['DepDF'])
    #ax.bar(x_pos - 0.5 * width, y_indepdf_mean, width, yerr=y_indepdf_stdev, capsize=5, label='IndepDF',
    #       color=colors['IndepDF'])
    #ax.bar(x_pos + 0.5 * width, y_query_based_amnesia_mean, width, yerr=y_query_based_amnesia_stdev, capsize=5,
    #       label='QB-Amnesia', color=colors['QB-Amnesia'])
    ax.bar(x_pos + 0.5 * width, y_lazy_greedy_mean, width, yerr=y_lazy_greedy_stdev, capsize=5, label='LAZY GREEDY',
           color=colors['LAZY GREEDY'])
    ax.set_xlabel("Number of DepDF iterations (T)")
    ax.set_ylabel("Computation time (seconds)")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(["2000", "10000", "50000", "100000"])
    ax.legend()
    ax.set_yscale('log')
    plt.savefig('T_vs_quality_photos_time_bars.png')
    """
    # Plot the time ones the same way as the ones for T.

    # FIGURE 2D: DBSize vs Time Flights
    """
    x = [0.25, 0.5, 0.75, 1]
    y_depdf_mean = [41.914007449150084, 73.69742274284363, 106.21293354034424, 125.77569205760956]
    y_depdf_stdev = [2.84688061709408, 6.227227074612631, 10.058518823939668, 23.79062954377069]
    y_indepdf_mean = [0.03414433002471921, 0.09644238948822018, 0.24050359725952145, 0.3865506649017334]
    y_indepdf_stdev = [0.01880614434201971, 0.04096470538832867, 0.03957663901172304, 0.0992556670791878]
    y_lazy_greedy_mean = [31222.46051039696, 86111.2414845705, 166827.38196954728, 90875.0760051012]
    y_lazy_greedy_stdev = [7850.919077630195, 21609.082627173684, 34336.39311047808, 19995.680130219902]
    y_query_based_amnesia_mean = [0.02460925579071041, 0.0956179857254028, 0.2292472124099731, 0.3008124709129333]
    y_query_based_amnesia_stdev = [0.01925525483634983, 0.02508703939357587, 0.0440808805878439, 0.10404407450190399]
    colors = {
        'DepDF': '#1E90FF',
        'IndepDF': '#87CEFA',
        'QB-Amnesia': '#FFD700',
        'LAZY GREEDY': '#FFA500'
    }

    # Plot
    fig, ax = plt.subplots()

    # Plot lines with shaded areas for standard deviation
    ax.plot(x, y_depdf_mean, marker='o', linestyle='-', color=colors['DepDF'], label='DepDF')
    ax.fill_between(x, np.array(y_depdf_mean) - np.array(y_depdf_stdev),
                    np.array(y_depdf_mean) + np.array(y_depdf_stdev),
                    color=colors['DepDF'], alpha=0.3)

    ax.plot(x, y_indepdf_mean, marker='o', linestyle='-', color=colors['IndepDF'], label='IndepDF')
    ax.fill_between(x, np.array(y_indepdf_mean) - np.array(y_indepdf_stdev),
                    np.array(y_indepdf_mean) + np.array(y_indepdf_stdev),
                    color=colors['IndepDF'], alpha=0.3)

    ax.plot(x, y_query_based_amnesia_mean, marker='o', linestyle='-', color=colors['QB-Amnesia'], label='QB-Amnesia')
    ax.fill_between(x, np.array(y_query_based_amnesia_mean) - np.array(y_query_based_amnesia_stdev),
                    np.array(y_query_based_amnesia_mean) + np.array(y_query_based_amnesia_stdev),
                    color=colors['QB-Amnesia'], alpha=0.3)

    ax.plot(x, y_lazy_greedy_mean, marker='o', linestyle='-', color=colors['LAZY GREEDY'], label='LAZY GREEDY')
    ax.fill_between(x, np.array(y_lazy_greedy_mean) - np.array(y_lazy_greedy_stdev),
                    np.array(y_lazy_greedy_mean) + np.array(y_lazy_greedy_stdev),
                    color=colors['LAZY GREEDY'], alpha=0.3)

    # Labels and legend
    ax.set_xlabel("Database size (percentage of database)")
    ax.set_ylabel("Computation time (seconds)")
    ax.set_xticks(x)
    ax.set_xticklabels(['0.25', '0.5', '0.75', '1'])
    ax.legend()
    ax.set_yscale('log')
    ax.legend(loc='upper right')
    # Save the figure
    plt.savefig('db_size_vs_time_flights.png')
    """
    # FIGURE 2E: DBSize vs Time Photos
    """
    x = [0.25, 0.5, 0.75, 1]
    y_depdf_mean = [506.18480107784274, 979.3147410154343, 1530.6172698259354, 2044.5436949133873]
    y_depdf_stdev = [15.735263350881173, 17.83042730568131, 50.1883557899518, 35.399569734720146]
    y_indepdf_mean = [7.000373125076294, 23.082317614555357, 45.42250292301178, 75.98391342163086]
    y_indepdf_stdev = [1.0674870330430863, 1.0403146085981372, 1.8468292301927764, 2.202158811468894]
    y_lazy_greedy_mean = [6594.963008618355, 18996.46968421936, 41344.56243515015, 63793.37896515131]
    y_lazy_greedy_stdev = [871.349976680102, 1250.8261880506593, 2795.994169257299, 10925.849942469305]
    y_query_based_amnesia_mean = [9.32683868408203, 27.8151584148407, 54.07002768516541, 91.12799270153046]
    y_query_based_amnesia_stdev = [0.516811131570311, 0.8234440491293104, 3.6681036101572757, 5.71988047529699]
    colors = {
        'DepDF': '#1E90FF',
        'IndepDF': '#87CEFA',
        'QB-Amnesia': '#FFD700',
        'LAZY GREEDY': '#FFA500'
    }

    # Plot
    fig, ax = plt.subplots()

    # Plot lines with shaded areas for standard deviation
    ax.plot(x, y_depdf_mean, marker='o', linestyle='-', color=colors['DepDF'], label='DepDF')
    ax.fill_between(x, np.array(y_depdf_mean) - np.array(y_depdf_stdev),
                    np.array(y_depdf_mean) + np.array(y_depdf_stdev),
                    color=colors['DepDF'], alpha=0.3)

    ax.plot(x, y_indepdf_mean, marker='o', linestyle='-', color=colors['IndepDF'], label='IndepDF')
    ax.fill_between(x, np.array(y_indepdf_mean) - np.array(y_indepdf_stdev),
                    np.array(y_indepdf_mean) + np.array(y_indepdf_stdev),
                    color=colors['IndepDF'], alpha=0.3)

    ax.plot(x, y_query_based_amnesia_mean, marker='o', linestyle='-', color=colors['QB-Amnesia'], label='QB-Amnesia')
    ax.fill_between(x, np.array(y_query_based_amnesia_mean) - np.array(y_query_based_amnesia_stdev),
                    np.array(y_query_based_amnesia_mean) + np.array(y_query_based_amnesia_stdev),
                    color=colors['QB-Amnesia'], alpha=0.3)

    ax.plot(x, y_lazy_greedy_mean, marker='o', linestyle='-', color=colors['LAZY GREEDY'], label='LAZY GREEDY')
    ax.fill_between(x, np.array(y_lazy_greedy_mean) - np.array(y_lazy_greedy_stdev),
                    np.array(y_lazy_greedy_mean) + np.array(y_lazy_greedy_stdev),
                    color=colors['LAZY GREEDY'], alpha=0.3)

    # Labels and legend
    ax.set_xlabel("Database size (percentage of database)")
    ax.set_ylabel("Computation time (seconds)")
    ax.set_xticks(x)
    ax.set_xticklabels(['0.25', '0.5', '0.75', '1'])
    ax.legend()
    ax.set_yscale('log')
    #ax.legend(loc='upper right')
    # Save the figure
    plt.savefig('db_size_vs_time_photos.png')
    """
    # FIGURE 2F: DBSize vs Time Wiki
    """
    x = [0.25, 0.5, 0.75, 1]
    y_depdf_mean = [1035.7842601299285, 1952.524259710312, 2307.736645531654, 2617.4983919501306]
    y_depdf_stdev = [438.33834856151003, 454.3261170527982, 947.2551496262843, 1226.4101397268144]
    y_indepdf_mean = [889.4138356208801, 2784.639080739021, 4806.949127316475, 7084.912663316727]
    y_indepdf_stdev = [271.7905911127889, 750.443779925341, 1714.912073007241, 2987.6228594236445]
    y_lazy_greedy_mean = [np.nan,np.nan,np.nan,np.nan]
    y_lazy_greedy_stdev = [np.nan,np.nan,np.nan,np.nan]
    y_query_based_amnesia_mean = [841.4147781848908, 2533.7599668741227, 3850.720554637909, 5390.1332888841625]
    y_query_based_amnesia_stdev = [388.40476449424375, 502.14202442691857, 1224.4262827623036, 2714.876459836766]
    colors = {
        'DepDF': '#1E90FF',
        'IndepDF': '#87CEFA',
        'QB-Amnesia': '#FFD700',
        'LAZY GREEDY': '#FFA500'
    }

    # Plot
    fig, ax = plt.subplots()

    # Plot lines with shaded areas for standard deviation
    ax.plot(x, y_depdf_mean, marker='o', linestyle='-', color=colors['DepDF'], label='DepDF')
    ax.fill_between(x, np.array(y_depdf_mean) - np.array(y_depdf_stdev),
                    np.array(y_depdf_mean) + np.array(y_depdf_stdev),
                    color=colors['DepDF'], alpha=0.3)

    ax.plot(x, y_indepdf_mean, marker='o', linestyle='-', color=colors['IndepDF'], label='IndepDF')
    ax.fill_between(x, np.array(y_indepdf_mean) - np.array(y_indepdf_stdev),
                    np.array(y_indepdf_mean) + np.array(y_indepdf_stdev),
                    color=colors['IndepDF'], alpha=0.3)

    ax.plot(x, y_query_based_amnesia_mean, marker='o', linestyle='-', color=colors['QB-Amnesia'], label='QB-Amnesia')
    ax.fill_between(x, np.array(y_query_based_amnesia_mean) - np.array(y_query_based_amnesia_stdev),
                    np.array(y_query_based_amnesia_mean) + np.array(y_query_based_amnesia_stdev),
                    color=colors['QB-Amnesia'], alpha=0.3)

    ax.plot(x, y_lazy_greedy_mean, marker='o', linestyle='-', color=colors['LAZY GREEDY'], label='LAZY GREEDY')
    ax.fill_between(x, np.array(y_lazy_greedy_mean) - np.array(y_lazy_greedy_stdev),
                    np.array(y_lazy_greedy_mean) + np.array(y_lazy_greedy_stdev),
                    color=colors['LAZY GREEDY'], alpha=0.3)

    # Labels and legend
    ax.set_xlabel("Database size (percentage of database)")
    ax.set_ylabel("Computation time (seconds)")
    ax.set_xticks(x)
    ax.set_xticklabels(['0.25', '0.5', '0.75', '1'])
    ax.legend()
    ax.set_yscale('log')
    ax.set_ylim(1, 100000)
    # ax.legend(loc='upper right')
    # Save the figure
    plt.savefig('db_size_vs_time_wikidata.png')
    """
    # FIGURE 2G: QLSize vs Time Flights
    """
    x = [0.25, 0.5, 0.75, 1]
    y_depdf_mean = [41.48504498004913, 57.70405642986297, 66.01546893119811, 125.77569205760956]
    y_depdf_stdev = [4.837794717191879, 7.575501687612435, 7.611607890403706, 23.79062954377069]
    y_indepdf_mean = [0.01439788341522212, 0.0732218503952026, 0.18764317035675043, 0.3865506649017334]
    y_indepdf_stdev = [0.013129500345253162, 0.035410478367865185, 0.04350476301675958, 0.0992556670791878]
    y_lazy_greedy_mean = [239.0100821018219, 5478.785101723671, 12335.429132556916, 90875.0760051012]
    y_lazy_greedy_stdev = [19.46673630372711, 1531.5231688476697, 4306.849230320801, 19995.680130219902]
    y_query_based_amnesia_mean = [0.015162587165832481, 0.05420556068420405, 0.11759419441223137, 0.3008124709129333]
    y_query_based_amnesia_stdev = [0.01321685569844777, 0.01642244546032924, 0.04062009811137236, 0.10404407450190399]
    colors = {
        'DepDF': '#1E90FF',
        'IndepDF': '#87CEFA',
        'QB-Amnesia': '#FFD700',
        'LAZY GREEDY': '#FFA500'
    }

    # Plot
    fig, ax = plt.subplots()

    # Plot lines with shaded areas for standard deviation
    ax.plot(x, y_depdf_mean, marker='o', linestyle='-', color=colors['DepDF'], label='DepDF')
    ax.fill_between(x, np.array(y_depdf_mean) - np.array(y_depdf_stdev),
                    np.array(y_depdf_mean) + np.array(y_depdf_stdev),
                    color=colors['DepDF'], alpha=0.3)

    ax.plot(x, y_indepdf_mean, marker='o', linestyle='-', color=colors['IndepDF'], label='IndepDF')
    ax.fill_between(x, np.array(y_indepdf_mean) - np.array(y_indepdf_stdev),
                    np.array(y_indepdf_mean) + np.array(y_indepdf_stdev),
                    color=colors['IndepDF'], alpha=0.3)

    ax.plot(x, y_query_based_amnesia_mean, marker='o', linestyle='-', color=colors['QB-Amnesia'], label='QB-Amnesia')
    ax.fill_between(x, np.array(y_query_based_amnesia_mean) - np.array(y_query_based_amnesia_stdev),
                    np.array(y_query_based_amnesia_mean) + np.array(y_query_based_amnesia_stdev),
                    color=colors['QB-Amnesia'], alpha=0.3)

    ax.plot(x, y_lazy_greedy_mean, marker='o', linestyle='-', color=colors['LAZY GREEDY'], label='LAZY GREEDY')
    ax.fill_between(x, np.array(y_lazy_greedy_mean) - np.array(y_lazy_greedy_stdev),
                    np.array(y_lazy_greedy_mean) + np.array(y_lazy_greedy_stdev),
                    color=colors['LAZY GREEDY'], alpha=0.3)

    # Labels and legend
    ax.set_xlabel("Query-log size (percentage of query-log)")
    ax.set_ylabel("Computation time (seconds)")
    ax.set_xticks(x)
    ax.set_xticklabels(['0.25', '0.5', '0.75', '1'])
    ax.legend()
    ax.set_yscale('log')
    #ax.legend(loc='upper right')
    # Save the figure
    plt.savefig('ql_size_vs_time_flights.png')
    """
    # FIGURE 2H: QLSize vs Time Photos
    """
    x = [0.25, 0.5, 0.75, 1]
    y_depdf_mean = [1580.9770628213882, 1836.3586746692658, 2097.7391048192976, 2044.5436949133873]
    y_depdf_stdev = [541.8886138777636, 474.6589307999016, 297.7346000656538, 35.399569734720146]
    y_indepdf_mean = [20.961467599868776, 35.69446055889129, 56.81217908859253, 75.98391342163086]
    y_indepdf_stdev = [6.060799317706409, 13.495793890186814, 16.27281646287173, 2.202158811468894]
    y_lazy_greedy_mean = [25938.65417728424, 51329.850188541415, 62576.092749118805, 63793.37896515131]
    y_lazy_greedy_stdev = [5235.132296228709, 15786.097371564598, 12270.516156060636, 10925.849942469305]
    y_query_based_amnesia_mean = [17.52496681213379, 35.91296696662903, 76.12742369174957, 91.12799270153046]
    y_query_based_amnesia_stdev = [9.324592592250701, 16.031869670570387, 2.771473074235508, 5.71988047529699]
    colors = {
        'DepDF': '#1E90FF',
        'IndepDF': '#87CEFA',
        'QB-Amnesia': '#FFD700',
        'LAZY GREEDY': '#FFA500'
    }

    # Plot
    fig, ax = plt.subplots()

    # Plot lines with shaded areas for standard deviation
    ax.plot(x, y_depdf_mean, marker='o', linestyle='-', color=colors['DepDF'], label='DepDF')
    ax.fill_between(x, np.array(y_depdf_mean) - np.array(y_depdf_stdev),
                    np.array(y_depdf_mean) + np.array(y_depdf_stdev),
                    color=colors['DepDF'], alpha=0.3)

    ax.plot(x, y_indepdf_mean, marker='o', linestyle='-', color=colors['IndepDF'], label='IndepDF')
    ax.fill_between(x, np.array(y_indepdf_mean) - np.array(y_indepdf_stdev),
                    np.array(y_indepdf_mean) + np.array(y_indepdf_stdev),
                    color=colors['IndepDF'], alpha=0.3)

    ax.plot(x, y_query_based_amnesia_mean, marker='o', linestyle='-', color=colors['QB-Amnesia'], label='QB-Amnesia')
    ax.fill_between(x, np.array(y_query_based_amnesia_mean) - np.array(y_query_based_amnesia_stdev),
                    np.array(y_query_based_amnesia_mean) + np.array(y_query_based_amnesia_stdev),
                    color=colors['QB-Amnesia'], alpha=0.3)

    ax.plot(x, y_lazy_greedy_mean, marker='o', linestyle='-', color=colors['LAZY GREEDY'], label='LAZY GREEDY')
    ax.fill_between(x, np.array(y_lazy_greedy_mean) - np.array(y_lazy_greedy_stdev),
                    np.array(y_lazy_greedy_mean) + np.array(y_lazy_greedy_stdev),
                    color=colors['LAZY GREEDY'], alpha=0.3)

    # Labels and legend
    ax.set_xlabel("Query-log size (percentage of query-log)")
    ax.set_ylabel("Computation time (seconds)")
    ax.set_xticks(x)
    ax.set_xticklabels(['0.25', '0.5', '0.75', '1'])
    ax.legend()
    ax.set_yscale('log')
    # ax.legend(loc='upper right')
    # Save the figure
    plt.savefig('ql_size_vs_time_photos.png')
    """
    # FIGURE 2I: QLSize vs Time Wiki
    """
    x = [0.25, 0.5, 0.75, 1]
    y_depdf_mean = [4121.574303650856, 3183.8366461515425, 2882.0532037973403, 2617.4983919501306]
    y_depdf_stdev = [986.1644895934041, 1333.1427647770033, 1450.8924266845886, 1226.4101397268144]
    y_indepdf_mean = [2255.0696374177933, 5026.276557660103, 6077.636962723732, 7084.912663316727]
    y_indepdf_stdev = [565.5328453627928, 592.0744662749489, 2321.341586869395, 2987.6228594236445]
    y_lazy_greedy_mean = [np.nan, np.nan,np.nan,np.nan]
    y_lazy_greedy_stdev = [np.nan, np.nan,np.nan,np.nan]
    y_query_based_amnesia_mean = [1995.4875269412994, 2996.2401889801026, 4708.835130953788, 5390.1332888841625]
    y_query_based_amnesia_stdev = [592.6888687818587, 1536.0575345911427, 2482.3306446284137, 2714.876459836766]
    colors = {
        'DepDF': '#1E90FF',
        'IndepDF': '#87CEFA',
        'QB-Amnesia': '#FFD700',
        'LAZY GREEDY': '#FFA500'
    }

    # Plot
    fig, ax = plt.subplots()

    # Plot lines with shaded areas for standard deviation
    ax.plot(x, y_depdf_mean, marker='o', linestyle='-', color=colors['DepDF'], label='DepDF')
    ax.fill_between(x, np.array(y_depdf_mean) - np.array(y_depdf_stdev),
                    np.array(y_depdf_mean) + np.array(y_depdf_stdev),
                    color=colors['DepDF'], alpha=0.3)

    ax.plot(x, y_indepdf_mean, marker='o', linestyle='-', color=colors['IndepDF'], label='IndepDF')
    ax.fill_between(x, np.array(y_indepdf_mean) - np.array(y_indepdf_stdev),
                    np.array(y_indepdf_mean) + np.array(y_indepdf_stdev),
                    color=colors['IndepDF'], alpha=0.3)

    ax.plot(x, y_query_based_amnesia_mean, marker='o', linestyle='-', color=colors['QB-Amnesia'], label='QB-Amnesia')
    ax.fill_between(x, np.array(y_query_based_amnesia_mean) - np.array(y_query_based_amnesia_stdev),
                    np.array(y_query_based_amnesia_mean) + np.array(y_query_based_amnesia_stdev),
                    color=colors['QB-Amnesia'], alpha=0.3)

    ax.plot(x, y_lazy_greedy_mean, marker='o', linestyle='-', color=colors['LAZY GREEDY'], label='LAZY GREEDY')
    ax.fill_between(x, np.array(y_lazy_greedy_mean) - np.array(y_lazy_greedy_stdev),
                    np.array(y_lazy_greedy_mean) + np.array(y_lazy_greedy_stdev),
                    color=colors['LAZY GREEDY'], alpha=0.3)

    # Labels and legend
    ax.set_xlabel("Query-log size (percentage of query-log)")
    ax.set_ylabel("Computation time (seconds)")
    ax.set_xticks(x)
    ax.set_xticklabels(['0.25', '0.5', '0.75', '1'])
    ax.legend()
    ax.set_yscale('log')
    ax.set_ylim(1, 100000)
    ax.legend(loc='lower left')
    # Save the figure
    plt.savefig('ql_size_vs_time_wikidata.png')
    """


draw_plots_experiments()