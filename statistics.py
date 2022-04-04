import matplotlib.pyplot as plt
import scipy.stats as norm
import scipy.stats as ss
import numpy as np


def plot_bar_chart(x, y, x_label, y_label, title, show_plot=True, save_path=None):
    """
    This function is to draw bar chart from the given x and y value.
    :param x: is a list of elements that represents x-axis.
    :param y: is a list of elements that represents y-axis.
    :param x_label: value name of x_label.
    :param y_label: value name of y_label.
    :param title: title name of bar chart.
    :param show_plot: True to show the plot, otherwise False.
    :param save_path: path to save the plot, None if not willing to save.
    :return: a bar chart.
    """
    plt.bar(x, y, width = 0.8)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    if save_path:
        plt.savefig(save_path, dpi=1000)

    if show_plot:
        plt.show()


def plot_pie_chart(y, y_labels, title, show_plot=True, save_path=None):
    """
    This functions is to draw pie chart from the given y.
    :param y: is a list of elements that represents the portion of the pie chart.
    :param y_labels: is a list of strings that represents the label parameter.
    :param title: title name of pie chart.
    :param show_plot: True to show the plot, otherwise False.
    :param save_path: path to save the plot, None if not willing to save.
    :return: a pie chart.
    """
    plt.pie(y, labels=y_labels)
    plt.title(title)

    if save_path:
        plt.savefig(save_path, dpi=1000)

    if show_plot:
        plt.show()


def plot_histogram(x, bins, x_label, y_label, title, show_plot=True, save_path=None):
    """
    This function is to draw histogram from the given x.
    :param x: sequence of data.
    :param bins: integer or sequence or string.
    :param x_label: value name of x-axis.
    :param y_label: value name of y-axis.
    :param title: title name of histogram.
    :param show_plot: True to show the plot, otherwise False.
    :param save_path:path to save the plot, None if not willing to save.
    :return: a histogram chart.
    """

    plt.hist(x, bins)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

    if save_path:
        plt.savefig(save_path, dpi=1000)

    if show_plot:
        plt.show()


def plot_GaussianDistribution(data, bins, x_label, y_label):
    """
    This function is to draw Gaussian Distribution from the given data.
    :param data: sequence of data.
    :param bins: integer or sequence or string.
    :param x_label: value name of x-axis.
    :param y_label: value name of y-axis.
    :return: a histogram chart and gaussian distribution.
    """
    mu, std = norm.fit(data)
    plt.hist(data, bins, density=True)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    title = "Fit results: mu = %.2f, std = %.2f" %(mu, std)
    plt.title(title)

    plt.show()


def plot_ExponentialDistribution(data):
    """
    This function is to draw Exponential Distribution from the given data.
    :param data: sequence of data.
    :return: a histogram chart and exponential distribution.
    """
    plt.hist(data, density=True)
    p = ss.expon.fit(data)
    xmin, xmax = plt.xlim()
    rX = np.linspace(1, xmax, 100)
    rP = ss.expon.pdf(rX, *p)
    plt.plot(rX, rP)

    plt.show()








