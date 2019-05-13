import matplotlib.pyplot as plot


class ChartUtil(object):

    @staticmethod
    def create_curve_line(fitness_values):
        plot.plot(fitness_values, label="Fish")
        plot.xlabel("Number of iterations")
        plot.ylabel("Fitness")
        plot.yscale('log')
        plot.legend()
        plot.title("Curve Line: Fish Swarm Search")
        plot.savefig('..//file//curve_line_fish_swarm_search.png')
        plot.close()

    @staticmethod
    def create_boxplot(fitness_values):
        fig = plot.figure(1, figsize=(9, 6))
        ax = fig.add_subplot(111)
        data_to_plot = [fitness_values]
        bp = ax.boxplot(data_to_plot)
        ax.set_xticklabels(['Fish'])
        plot.title("Boxplot: Fish Swarm Search")
        fig.savefig('..//file//boxplot_fish_swarm_search.png', bbox_inches='tight')
        plot.close()

