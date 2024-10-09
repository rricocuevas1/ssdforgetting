def draw_plots_experiments():
    # QUALITY PERFORMANCE for changing answer set diversity photos (DONE!)
    """
    x = [0.10315621108423553, 0.09224688219124286, 0.08163194847127428, 0.07476247710140864, 0.0648838516706814]
    y_indepdf_mean = [0.1936410310852782, 0.1245443701662763, 0.1260273705000385, 0.1291601781916979, 0.1105087697027153]
    y_lazy_greedy_mean = [0.8223959313561867, 0.5137888907383809, 0.4115635059758161, 0.33334301598900734, 0.2760813254114178]
    y_indep = [lg - knap for lg, knap in zip(y_lazy_greedy_mean, y_indepdf_mean)]
    plt.plot(x, y_indep, color='k', marker='o', lw=1, label='Quality difference (LAZZY GREEDY vs IndepDF)', linestyle='solid')
    plt.xlabel("Answer set diversity")
    plt.ylabel("Quality percentage")
    custom_labels = ["10%", "25%", "50%", "75%", "100%"]
    for i, txt in enumerate(custom_labels):
        plt.text(x[i] - 0.001, y_indep[i], txt, ha='left', va='bottom')
    plt.gca().invert_xaxis()
    plt.legend()
    plt.savefig('answer_set_diversity_photos.png')
    """
    # QUALITY PERFORMANCE for changing answer set diversity flights
    """
    x = [0.05757007029485365, 0.04869947495850181, 0.04445579754164265, 0.03708746644665503]
    y_indepdf_mean = [0.48924162257495596, 0.3510040221500105, 0.2847315892663502, 0.3226167498192457]
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

    # QUALITY PERFORMANCE for changing query-log diversity
    # Photos 10%
    """
    s = pd.Series(
        [0.19932988913200952, 0.4832054800554152, 0.6595726615356589],
        index=["IndepDF", "DepDF", "LAZY GREEDY"]
    )
    # Set descriptions:
    plt.ylabel('Quality percentage')

    # Plot the data:
    my_colors = list(['coral', 'black', 'teal'])

    s.plot(
        kind='bar',
        color=my_colors,
        rot = 0
    )
    plt.savefig('quality_vs_log_10percent.png')
    """
    # Photos 25%
    """
    s = pd.Series(
        [0.19263852873258236,0.4588458391187194 , 0.6420882379088511],
        index=["IndepDF", "DepDF", "LAZY GREEDY"]
    )
    # Set descriptions:
    plt.ylabel('Quality percentage')

    # Plot the data:
    my_colors = list(['coral', 'black', 'teal'])

    s.plot(
        kind='bar',
        color=my_colors,
        rot=0
    )
    plt.savefig('quality_vs_log_25percent.png')
    """
    # Flight data
    """
    s = pd.Series(
        [0.510673827485099, 0.5062845490272324, 0.5309716267982495],
        index=["IndepDF", "DepDF", "LAZY GREEDY"]
    )
    # Set descriptions:
    plt.ylabel('Quality percentage')

    # Plot the data:
    my_colors = list(['coral', 'black', 'teal'])

    s.plot(
        kind='bar',
        color=my_colors,
        rot=0
    )
    #plt.show()
    plt.savefig('quality_vs_log_flights.png')
    """
    # QUALITY PERFORMANCE for changing budget
    # Photo data
    """
    x = [0.001, 0.005, 0.01, 0.02]
    y_knapsack = [0.182736607625102, 0.48356294780266945, 0.6907967307063827,0.919815671569535]
    y_scg_best = [0.4613660492299406, 0.7711509921601285, 0.8619560772493505,0.9595225077804348]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_best, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    y_lazy_greedy = [0.644791862712373, 0.8382475602257057, 0.9132339703626257,0.9844470897279535]
    plt.plot(x, y_lazy_greedy, color='teal', marker='x', lw=1, label='LAZZY GREEDY', linestyle='dotted')
    plt.xlabel("Budget (percentage of database)")
    plt.ylabel("Quality percentage")
    plt.legend()
    #plt.show()
    plt.savefig('budget_size_vs_time_quality_photos.png')
    """
    """
    x = [0.001, 0.005, 0.01, 0.02]
    y_knapsack = [0.182736607625102, 0.48356294780266945, 0.6907967307063827, 0.919815671569535]
    y_scg_best = [0.4613660492299406, 0.7711509921601285, 0.8619560772493505, 0.9595225077804348]
    y_lazy_greedy = [0.644791862712373, 0.8382475602257057, 0.9132339703626257, 0.9844470897279535]
    bar_width = 0.25  # Adjust the bar width as needed
    bar_positions = np.arange(len(x))
    plt.bar(bar_positions - bar_width, y_knapsack, color='coral', width=bar_width, label='IndepDF')
    plt.bar(bar_positions, y_scg_best, color='black', width=bar_width, label='DepDF (T = 2K)')
    plt.bar(bar_positions + bar_width, y_lazy_greedy, color='teal', width=bar_width, label='LAZZY GREEDY')
    # Set x-axis ticks to match x values
    plt.xticks(bar_positions, x)
    plt.xlabel("Budget (percentage of database)")
    plt.ylabel("Quality percentage")
    # Move the legend to the bottom right corner
    plt.legend(loc='upper left')
    #plt.show()
    plt.savefig('budget_size_vs_time_quality_photos.png')
    """
    # FIGURE 1: QUALITY PERFORMANCE for changing budget Flights data
    """
    x = [0.1, 0.25, 0.5]
    y_depdf_mean = [0.7497814388803654, 0.8930522347686001, 0.9571032130200867]
    y_depdf_stdev = [0.015372358324392384, 0.008176720271674508, 0.007160154704195134]
    y_indepdf_mean = [0.831837735925193, 0.9334995163230462, 0.9789635349635353]
    y_indepdf_stdev = [0, 0, 0]
    y_query_based_amnesia_mean = [0.3683269576541349, 0.6271669308234213, 0.8692425648339823]
    y_query_based_amnesia_stdev = [0.039256508521323924, 0.03130656877120506, 0.016686886638077297]
    # Lazy Greedy data only for x = 0.1
    y_lazy_greedy_mean = [0.8333490674638844]
    y_lazy_greedy_stdev = [0]
    colors = {
        'DepDF': '#1E90FF',
        'IndepDF': '#87CEFA',
        'QB-Amnesia': '#FFD700',
        'LAZY GREEDY': '#FFA500'
    }
    width = 0.15
    x_pos = np.arange(len(x))
    fig, ax = plt.subplots()
    ax.bar(x_pos - 1.5 * width, y_depdf_mean, width, yerr=y_depdf_stdev, capsize=5, label='DepDF', color=colors['DepDF'])
    ax.bar(x_pos - 0.5 * width, y_indepdf_mean, width, yerr=y_indepdf_stdev, capsize=5, label='IndepDF', color=colors['IndepDF'])
    ax.bar(x_pos + 0.5 * width, y_query_based_amnesia_mean, width, yerr=y_query_based_amnesia_stdev, capsize=5, label='QB-Amnesia', color=colors['QB-Amnesia'])
    ax.bar(x_pos[0] + 1.5 * width, y_lazy_greedy_mean, width, yerr=y_lazy_greedy_stdev, capsize=5, label='LAZY GREEDY', color=colors['LAZY GREEDY'])
    ax.set_xlabel("Budget (percentage of database)")
    ax.set_ylabel("Quality percentage")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(['0.1', '0.25', '0.5'])
    ax.legend()
    plt.savefig('budget_size_vs_time_quality_flights.png')
    """
    # FIGURE 2: Photo data (NOT DONE)
    # FIGURE 3: Wiki data (DONE)
    """
    x = [0.01, 0.1, 0.25]
    y_depdf_mean = [0.34481920254238907, 0.6360870237879164, 0.7646407209622512]
    y_depdf_stdev = [0.008006435573677965, 0.01149358893056299, 0.004084723901125629]
    y_indepdf_mean = [0.5499046723239122, 0.8548548681719849, 0.9368025250538364 ]
    y_indepdf_stdev = [0, 0, 0, ]
    y_query_based_amnesia_mean = [0.3202069055218859, 0.6845831549826776, 0.8161548073120777]
    y_query_based_amnesia_stdev = [0.011604543284235425, 0.0054397038782312114, 0.0024012007975152383]
    y_lazy_greedy_mean = [0]
    y_lazy_greedy_stdev = [0]
    colors = {
        'DepDF': '#1E90FF',
        'IndepDF': '#87CEFA',
        'QB-Amnesia': '#FFD700',
        'LAZY GREEDY': '#FFA500'
    }
    width = 0.15  # Width of the bars
    x_pos = np.arange(len(x))

    fig, ax = plt.subplots()

    # Plotting bars with standard deviation error bars
    ax.bar(x_pos - 1.5 * width, y_depdf_mean, width, yerr=y_depdf_stdev, capsize=5, label='DepDF',
           color=colors['DepDF'])
    ax.bar(x_pos - 0.5 * width, y_indepdf_mean, width, yerr=y_indepdf_stdev, capsize=5, label='IndepDF',
           color=colors['IndepDF'])
    ax.bar(x_pos + 0.5 * width, y_query_based_amnesia_mean, width, yerr=y_query_based_amnesia_stdev, capsize=5,
           label='QB-Amnesia', color=colors['QB-Amnesia'])

    # No Lazy Greedy bars since data is empty
    ax.bar(x_pos[0] + 1.5 * width, y_lazy_greedy_mean, width, yerr=y_lazy_greedy_stdev, capsize=5, label='LAZY GREEDY', color=colors['LAZY GREEDY'])

    # Adding labels and legend
    ax.set_xlabel("Budget (percentage of database)")
    ax.set_ylabel("Quality percentage")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(['0.01', '0.1', '0.25'])
    ax.legend()

    # Save and display the plot
    plt.savefig('budget_size_vs_time_quality_wiki.png')
    """

    # QUALITY PERFORMANCE for changing T
    # Photo data
    """
    # Photo data (quality) difference representation
    x = [2000, 10000, 50000, 100000]
    y_scg_best = [0.8615699054128367, 0.8744355499838297, 0.8823625597440573, 0.8855239449041044]
    y_lazy_greedy = [0.9132339703626257,0.9132339703626257,0.9132339703626257,0.9132339703626257]
    y = [lg - knap for lg, knap in zip(y_lazy_greedy, y_scg_best)]
    plt.plot(x, y, color='black', marker='o', lw=1, label='Quality difference (LAZZY GREEDY vs DepDF)',
             linestyle='solid')
    plt.xlabel("Number of DepDF iterations (T)")
    plt.ylabel("Quality percentage")
    custom_labels = ["T = 2K", "T = 10K", "T = 50K", "T = 100K"]
    for i, txt in enumerate(custom_labels):
        plt.text(x[i] + 1000, y[i], txt, ha='left', va='bottom')
    plt.legend()
    #plt.show()
    plt.savefig('T_vs_quality_photo_difference.png')
    """
    # Photo data (time)
    """
    x = [2000, 10000, 50000, 100000]
    y_scg_average = [87.51587355852126, 436.5793798398972, 2133.824789247513, 4248.518572244644]
    y_lazy_greedy = [10682.727551698685, 10522.896597385406, 10147.123672485352, 9984.104957342148]
    bar_width = 0.25  # Adjust the bar width as needed
    bar_positions = np.arange(len(x))
    # Plot y_scg_average as dotted bars filled with black dots
    plt.bar(bar_positions - bar_width / 2, y_scg_average, color='black', width=bar_width, label='DepDF')
    # Commented out the bar for y_scg_best
    # plt.bar(bar_positions, y_scg_best, color='black', width=bar_width, label='DepDF best')
    # Plot y_lazy_greedy in teal
    plt.bar(bar_positions + bar_width / 2, y_lazy_greedy, color='teal', width=bar_width, label='LAZZY GREEDY')
    # Set x-axis ticks to match x values
    plt.xticks(bar_positions, x)
    # Use a logarithmic scale for the y-axis
    plt.yscale('log')
    plt.xlabel("Number of DepDF iterations (T)")
    plt.ylabel("Computation time (seconds)")
    plt.legend(loc='lower right')
    #plt.show()
    plt.savefig('T_vs_quality_photos_time_bars.png')
    """
    # Synthetic data
    """
    x = [2000, 10000, 50000, 100000]
    y_knapsack = [0.1965, 0.1965, 0.1965, 0.1965]
    y_scg_best = [0.9808, 0.9808, 0.9808, 0.9808]
    y_lazy_greedy = [0.9808, 0.9808, 0.9808, 0.9808]
    plt.plot(x, y_knapsack, color='coral', lw=1, label='IndepDF', linestyle='solid')
    plt.plot(x, y_scg_best, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.plot(x, y_lazy_greedy, color='teal', lw=1, label='LAZZY GREEDY', linestyle='solid')
    plt.xlabel("T")
    plt.ylabel("Quality percentage")
    plt.legend()
    # plt.show()
    plt.savefig('T_vs_quality_synthetic.png')
    """
    # Flights data
    """
    x = [2000, 10000, 50000, 100000]
    #y_knapsack = [0.9364871081213451,0.9364871081213451,0.9364871081213451,0.9364871081213451]
    y_scg_best = [0.9161678927509542,0.922307306583541,0.9284609979132528,0.930836400614828]
    #y_scg_average = [0.8966353438712413,0.91381592435688,0.9241051312250277,0.9274628103213921]
    y_lazy_greedy = [0.9412653072758796,0.9412653072758796,0.9412653072758796,0.9412653072758796]
    y = [lg - knap for lg, knap in zip(y_lazy_greedy, y_scg_best)]
    #plt.plot(x, y_knapsack, color='coral', lw=1, label='IndepDF',linestyle='solid')
    plt.plot(x, y, color='black', marker='o', lw=1, label='Quality difference (LAZZY GREEDY vs DepDF)', linestyle='solid')
    #plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF (average)', linestyle='dotted')
    #plt.plot(x, y_lazy_greedy, color='teal', lw=1, label='LAZZY GREEDY', linestyle='solid')
    plt.xlabel("Number of DepDF iterations (T)")
    plt.ylabel("Quality percentage")
    custom_labels = ["T = 2K", "T = 10K", "T = 50K", "T = 100K"]
    for i, txt in enumerate(custom_labels):
        plt.text(x[i] + 1000, y[i], txt, ha='left', va='bottom')
    plt.legend()
    #plt.show()
    plt.savefig('T_vs_quality_flights.png')
    """
    # Flights data (quality) difference representation
    """
    x = [2000, 10000, 50000, 100000]
    # y_knapsack = [0.9364871081213451,0.9364871081213451,0.9364871081213451,0.9364871081213451]
    y_scg_best = [0.9161678927509542, 0.922307306583541, 0.9284609979132528, 0.930836400614828]
    #y_scg_average = [0.8966353438712413,0.91381592435688,0.9241051312250277,0.9274628103213921]
    y_lazy_greedy = [0.9412653072758796, 0.9412653072758796, 0.9412653072758796, 0.9412653072758796]
    y = [lg - knap for lg, knap in zip(y_lazy_greedy, y_scg_best)]
    # plt.plot(x, y_knapsack, color='coral', lw=1, label='IndepDF',linestyle='solid')
    plt.plot(x, y, color='black', marker='o', lw=1, label='Quality difference (LAZZY GREEDY vs DepDF)',
             linestyle='solid')
    plt.xlabel("Number of DepDF iterations (T)")
    plt.ylabel("Quality percentage")
    custom_labels = ["T = 2K", "T = 10K", "T = 50K", "T = 100K"]
    for i, txt in enumerate(custom_labels):
        plt.text(x[i] + 1000, y[i], txt, ha='left', va='bottom')
    plt.legend()
    #plt.show()
    plt.savefig('T_vs_quality_flights_difference.png')
    """

    # Flights data (quality) bars representation
    """
    x = [2000, 10000, 50000, 100000]
    y_scg_best = [0.9161678927509542, 0.922307306583541, 0.9284609979132528, 0.930836400614828]
    #y_scg_average = [0.8966353438712413, 0.91381592435688, 0.9241051312250277, 0.9274628103213921]
    y_lazy_greedy = [0.9412653072758796, 0.9412653072758796, 0.9412653072758796, 0.9412653072758796]
    bar_width = 0.25  # Adjust the bar width as needed
    bar_positions = np.arange(len(x))
    # Set the figure size to make the plot frame smaller in height
    #plt.figure(figsize=(8, 4))
    plt.bar(bar_positions - bar_width / 2, y_scg_best, color='black', width=bar_width, label='DepDF')
    # Plot y_lazy_greedy in teal
    plt.bar(bar_positions + bar_width / 2, y_lazy_greedy, color='teal', width=bar_width, label='LAZZY GREEDY')
    # Set x-axis ticks to match x values
    plt.xticks(bar_positions, x)
    plt.xlabel("Number of DepDF iterations (T)")
    plt.ylabel("Quality percentage")
    # Move the legend to the bottom right corner
    plt.legend(loc='lower right')
    plt.savefig('T_vs_quality_flights_bars.png')
    """
    # Flights data (time)
    """
    x = [2000, 10000, 50000, 100000]
    # y_scg_best = [14.87398624420166, 76.74158239364624, 396.332572221756, 788.5913519859314]
    y_scg_average = [17.00263908624649, 81.85139081954956, 413.03129932641986, 807.1527675104142]
    y_lazy_greedy = [186178.70178604126, 188887.9600560665, 187906.53858208656, 185470.73424577713]
    bar_width = 0.25  # Adjust the bar width as needed
    bar_positions = np.arange(len(x))
    # Plot y_scg_average as dotted bars filled with black dots
    plt.bar(bar_positions - bar_width / 2, y_scg_average, color='black', width=bar_width, label='DepDF')
    # Commented out the bar for y_scg_best
    # plt.bar(bar_positions, y_scg_best, color='black', width=bar_width, label='DepDF best')
    # Plot y_lazy_greedy in teal
    plt.bar(bar_positions + bar_width / 2, y_lazy_greedy, color='teal', width=bar_width, label='LAZZY GREEDY')
    # Set x-axis ticks to match x values
    plt.xticks(bar_positions, x)
    # Use a logarithmic scale for the y-axis
    plt.yscale('log')
    plt.xlabel("Number of DepDF iterations (T)")
    plt.ylabel("Computation time (seconds)")
    plt.legend(loc='lower right')
    #plt.show()
    plt.savefig('T_vs_quality_flights_time_bars.png')
    """
    # Skyserver data
    """
    x = [2000, 10000, 50000, 100000]
    y_knapsack = [0.2499547838668866,0.2499547838668866,0.2499547838668866,0.2499547838668866]
    y_scg_best = [0.2499547838668866,0.2499547838668866,0.2499547838668866,0.2499547838668866]
    y_scg_average = [0.2499547838668866,0.2499547838668866,0.2499547838668866,0.2499547838668866]
    y_lazy_greedy = [0.2499547838668866,0.2499547838668866,0.2499547838668866,0.2499547838668866]
    plt.plot(x, y_knapsack, color='coral', lw=1, label='IndepDF', linestyle='solid')
    plt.plot(x, y_scg_best, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.plot(x, y_lazy_greedy, color='teal', lw=1, label='LAZZY GREEDY', linestyle='solid')
    plt.xlabel("T")
    plt.ylabel("Quality percentage")
    plt.legend()
    # plt.show()
    plt.savefig('T_vs_quality_skyserver.png')
    """
    # Wiki data
    """
    x = [2000, 10000, 50000, 100000]
    y_knapsack = [0.5149527078518078,0.5149527078518078,0.5149527078518078,0.5149527078518078]
    y_scg_best = [0.30432555390246135,0.38955381694285574, 0.46226705690191994, 0.479811385430121]
    y_scg_average = []
    y_lazy_greedy = []
    plt.plot(x, y_knapsack, color='coral', lw=1, label='IndepDF', linestyle='solid')
    plt.plot(x, y_scg_best, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    #plt.plot(x, y_lazy_greedy, color='teal', lw=1, label='LAZZY GREEDY', linestyle='solid')
    plt.xlabel("T")
    plt.ylabel("Quality percentage")
    plt.legend()
    # plt.show()
    plt.savefig('T_vs_quality_wikidata.png')
    """

    # Wiki data difference plot
    """
    x = [2000, 10000, 50000, 100000]
    y_scg_best = [0.30432555390246135,0.38955381694285574, 0.46226705690191994, 0.479811385430121]
    y_lazy_greedy = [0.644791862712373, 0.644791862712373, 0.644791862712373, 0.644791862712373]
    y = [lg - knap for lg, knap in zip(y_lazy_greedy, y_scg_best)]
    # plt.plot(x, y_knapsack, color='coral', lw=1, label='IndepDF',linestyle='solid')
    plt.plot(x, y, color='black', marker='o', lw=1, label='Quality difference (LAZZY GREEDY vs DepDF)',
             linestyle='solid')
    plt.xlabel("Number of DepDF iterations (T)")
    plt.ylabel("Quality percentage")
    custom_labels = ["T = 2K", "T = 10K", "T = 50K", "T = 100K"]
    for i, txt in enumerate(custom_labels):
        plt.text(x[i] + 1000, y[i], txt, ha='left', va='bottom')
    plt.legend()
    plt.show()
    #plt.savefig('T_vs_quality_photos_difference.png')
    """
    # TIME PERFORMANCE
    # Synthetic data
    # Time vs database size
    """
    x = [1000, 10000, 50000, 100000]
    y_knapsack = [0.004328489303588867, 0.05312824249267578, 0.27655982971191406, 0.557905912399292]
    y_scg_best = [150.75003814697266, 171.5881872177124, 222.7144525051117, 307.09306955337524]
    y_scg_average = [169.79319627046584, 186.0296595978737, 252.8817608475685, 321.6965695619583]
    y_lazy_greedy = [2530.955432653427, 2787.4164786338806, 3400.2080109119415, 4269.266548156738]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.plot(x, y_lazy_greedy, color='teal', marker='o', lw=1, label='LAZZY GREEDY', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Database size (number of tuples)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    plt.savefig('db_size_vs_time_synthetic.png')
    """
    # Time vs log size
    """
    x = [1, 1000, 5000, 10000]
    y_knapsack = [0.0032575130462646484, 0.6697661876678467, 3.0928566455841064, 6.505589485168457]
    y_scg_best = [157.83138179779053, 160.62016797065735, 164.3982458114624, 164.34407711029053]
    y_scg_average = [169.1958419394493, 164.86892694711685, 168.06755939006806, 165.3723399066925]
    y_lazy_greedy = [2515.2913496494293, 28769.599863290787, 133036.57333421707, 263737.5946471691]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.plot(x, y_lazy_greedy, color='teal', marker='o', lw=1, label='LAZZY GREEDY', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Query-log size (number of queries)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    plt.savefig('ql_size_vs_time_synthetic.png')
    """
    # Time vs budget size
    """
    x = [0.1,0.25,0.5,0.75]
    y_knapsack = [0.0037071704864501953, 0.00450897216796875, 0.0036575794219970703, 0.0041980743408203125]
    y_scg_best = [181.06821155548096, 173.55169105529785, 189.86261415481567, 200.71150732040405]
    y_scg_average = [188.61571950674056, 174.3621605014801, 192.66608548879623, 201.5326520419121]
    y_lazy_greedy = [4399.199303627014, 11963.925490140915, 48116.88911509514, 95261.95436835289]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.plot(x, y_lazy_greedy, color='teal', marker='o', lw=1, label='LAZZY GREEDY', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Budget (percentage of database)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    plt.savefig('budget_size_vs_time_synthetic.png')
    """
    ########################################
    # Flights data
    """
    # Time vs database size
    x = [0.25, 0.5, 0.75, 1]
    y_knapsack = [0.003899812698364258, 0.009813785552978516, 0.01578521728515625, 0.02410745620727539]
    y_scg_best = [2.820413112640381, 4.620015382766724, 7.105572938919067, 9.903147459030151]
    y_scg_average = [3.2216223740577696, 5.507647526264191, 8.364754068851472, 10.88465545654297]
    y_lazy_greedy = [3469.891182422638, 13448.199064016342, 31925.797295331955, 14098.878171920776]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.plot(x, y_lazy_greedy, color='teal', marker='o', lw=1, label='LAZZY GREEDY', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Database size (percentage of database)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    #plt.show()
    plt.savefig('db_size_vs_time_flights.png')
    """
    # Time vs log size
    """
    x = [0.25, 0.5, 0.75, 1]
    y_knapsack = [0.0068624019622802734, 0.011359214782714844, 0.018099069595336914, 0.024684906005859375]
    y_scg_best = [4.6796486377716064, 5.491217374801636, 8.485694408416748, 9.866000175476074]
    y_scg_average = [4.820750246047973, 5.759337148666382, 9.392980618476868, 11.309501926898957]
    y_lazy_greedy = [300.8953139781952, 1345.6963412761688, 8615.575507164001, 15063.496519565582]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.plot(x, y_lazy_greedy, color='teal', marker='o', lw=1, label='LAZZY GREEDY', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Query-log size (percentage of query-log)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    plt.savefig('ql_size_vs_time_flights.png')
    """
    # Time vs budget size
    """
    x = [0.1, 0.25, 0.5, 0.75]
    y_knapsack = [0.024480104446411133,0.023853778839111328, 0.02467489242553711, 0.024428844451904297]
    y_scg_best = [10.331410646438599,11.207442045211792, 12.149226427078247, 13.305735111236572]
    y_scg_average = [12.126237394809722,12.87460818052292, 13.70933828830719, 15.190605382919312]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    x = [0.1, 0.25]
    y_lazy_greedy = [14893.683580636978, 117007.94601273537]
    plt.plot(x, y_lazy_greedy, color='teal', marker='o', lw=1, label='LAZZY GREEDY', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Budget (percentage of database)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    plt.savefig('budget_size_vs_time_flights.png')
    """
    ########################################
    # Photo data
    # Time vs database size
    """
    x = [0.25, 0.5, 0.75, 1]
    y_knapsack = [0.4757518768310547, 1.4121289253234863, 2.7885560989379883, 4.517786741256714]
    y_scg_best = [24.84172821044922, 47.14532017707825, 70.4173150062561,95.15764689445496]
    y_scg_average = [25.506559624671937, 48.156388673782345, 72.053144261837,98.49250144481658]
    y_lazy_greedy = [288.5402281284332, 921.1867897510529, 1938.1703350543976,3760.3360245227814]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.plot(x, y_lazy_greedy, color='teal', marker='o', lw=1, label='LAZZY GREEDY', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Database size (percentage of database)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    #plt.show()
    plt.savefig('db_size_vs_time_photos.png')
    """
    # Time vs log size
    """
    x = [0.25, 0.5, 0.75, 1]
    y_knapsack = [1.2115960121154785, 2.4660212993621826, 3.827317476272583, 4.517786741256714]
    y_scg_best = [96.39048933982849, 97.5726249217987, 99.35202026367188, 95.15764689445496]
    y_scg_average = [100.35520425796508, 101.24481378555298, 103.19788735866547, 98.49250144481658]
    y_lazy_greedy = [1525.643858909607, 3718.0446033477783, 4384.106575965881,3760.3360245227814]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.plot(x, y_lazy_greedy, color='teal', marker='o', lw=1, label='LAZZY GREEDY', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Query-log size (percentage of query-log)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    plt.savefig('ql_size_vs_time_photos.png')
    """
    # Time vs budget size
    """
    x = [0.001, 0.005, 0.01, 0.02]
    y_knapsack = [0.37604451179504395, 0.37601709365844727, 0.3762376308441162, 0.3476734161376953]
    y_scg_best = [89.0256700515747, 86.86222910881042, 87.06705689430237, 79.19679617881775]
    y_scg_average = [91.4893985247612, 89.4820474243164,  89.705569293499, 80.22476348638534]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    y_lazy_greedy = [880.529301404953, 3866.179448366165, 10498.341153144836, 29613.581778526306]
    plt.plot(x, y_lazy_greedy, color='teal', marker='o', lw=1, label='LAZZY GREEDY', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Budget (percentage of database)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    #plt.show()
    plt.savefig('budget_size_vs_time_photos.png')
    """
    ########################################
    # Skyserver data
    # Time vs database size
    """
    x = [0.25, 0.5, 0.75, 1]
    y_knapsack = [0.5241560935974121, 2.2076327800750732, 5.0618062019348145, 8.940283060073853]
    y_scg_best = [4.934473752975464, 9.221255779266357, 13.412368535995483, 18.026517391204834]
    y_scg_average = [5.018848261833191, 9.461390652656554, 13.704821314811706, 18.72696128129959]
    y_lazy_greedy = [184.1152560710907, 1685.0655269622803, 3074.27885556221, 5163.732174396515]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.plot(x, y_lazy_greedy, color='teal', marker='o', lw=1, label='LAZZY GREEDY', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Database size (percentage of database)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    plt.savefig('db_size_vs_time_skyserver.png')
    """
    # Time vs log size
    """
    x = [0.25, 0.5, 0.75, 1]
    y_knapsack = [2.1317453384399414, 4.530511379241943, 6.882694721221924, 9.01269817352295]
    y_scg_best = [17.404266834259033, 17.69446325302124, 17.803529500961304, 17.971412897109985]
    y_scg_average = [18.731486196517945, 19.23995817422867, 19.891599898338317, 19.751319744586944]
    y_lazy_greedy = [220.94915342330933, 1741.1581063270569, 3068.6717739105225, 5098.643315553665]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.plot(x, y_lazy_greedy, color='teal', marker='o', lw=1, label='LAZZY GREEDY', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Query-log size (percentage of query-log)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    plt.savefig('ql_size_vs_time_skyserver.png')
    """
    # Time vs budget size
    """
    x = [0.1, 0.25, 0.5, 0.75]
    y_knapsack = [9.171797513961792, 9.29223346710205, 9.604455709457397, 9.814805746078491]
    y_scg_best = [19.2213454246521, 19.647393226623535, 20.98867416381836, 21.047019243240356]
    y_scg_average = [20.33356022119522, 20.806009690761567, 22.44000188589096, 22.270158097743987]
    y_lazy_greedy = [5026.575392007828, 6118.180355787277, 17877.225949287415, 24578.071284770966]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.plot(x, y_lazy_greedy, color='teal', marker='o', lw=1, label='LAZZY GREEDY', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Budget (percentage of database)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    plt.savefig('budget_size_vs_time_skyserver.png')
    """
    ########################################
    # Wikidata
    # Time vs database size
    """
    x = [0.25, 0.5, 0.75, 1]
    y_knapsack = [39.47792148590088,119.65058135986328,245.4351613521576,451.27913427352905]
    y_scg_best = [54.03641700744629,111.39731287956238,176.13414192199707,234.6079249382019]
    y_scg_average = [61.63474735021591, 123.39076393842697,181.8767843770981,251.7380623984337]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Database size (percentage of database)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    plt.savefig('db_size_vs_time_wikidata.png')
    """
    # Time vs log size
    """
    x = [0.25, 0.5, 0.75, 1]
    y_knapsack = [93.29072165489197, 214.8503873348236, 334.00794863700867,514.0357732772827]
    y_scg_best = [228.73489451408386, 238.84203219413757, 224.9423451423645,235.47054147720337]
    y_scg_average = [249.28254986047745, 252.1894390964508, 231.15009807348252,251.11487977027892]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Query-log size (percentage of query-log)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    plt.savefig('ql_size_vs_time_wikidata.png')
    """
    # Time vs budget size
    """
    x = [0.01, 0.1, 0.25, 0.5]
    y_knapsack = [492.58388781547546,541.9561607837677,544.34650182724,520.0659682750702]
    y_scg_best = [229.41212677955627,239.53992128372192,244.43260288238525,241.24141788482666]
    y_scg_average = [245.89446593284606,250.98201437711717,257.54544481039045,253.96924232006074]
    plt.plot(x, y_knapsack, color='coral', marker='o', lw=1, label='IndepDF', linestyle='dotted')
    plt.plot(x, y_scg_average, color='black', marker='o', lw=1, label='DepDF', linestyle='dotted')
    plt.yscale('log')
    plt.xlabel("Budget (percentage of database)")
    plt.ylabel("Computation time (seconds)")
    plt.legend()
    plt.savefig('budget_size_vs_time_wikidata.png')
    """


draw_plots_experiments()
