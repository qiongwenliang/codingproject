from matplotlib import pyplot as plt


def plot_bar_chart(x, y, x_label, y_label, title, show_plot=True, save_path=None):
    """
    This function is to draw bar chart from the given x and y value.
    :param x: is a list of elements that represents x-axis.
    :param y: is a list of elements that represents y-axis.
    :param x_label: value name of x_label
    :param y_label: value name of y_label
    :param title: title name of bar chart
    :param show_plot: True to show the plot, otherwise False
    :param save_path: path to save the plot, None if not willing to save
    :return: a bar chart
    """
    plt.bar(x, y, width = 0.8)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    if save_path:
        plt.savefig(save_path, dpi=1000)

    if show_plot:
        plt.show()
