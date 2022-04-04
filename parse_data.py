import collections
import csv


class ParseData:
    def __init__(self, path):
        """
        This class is to parse csv document and put it into python data structures that is ready to be used.
        :param path: path to the csv file.
        """
        file_obj = open(path, 'r')
        reader = csv.reader(file_obj)

        self.raw_data = []

        for row in reader:
            self.raw_data.append(row)

        self.country_dic = collections.defaultdict(dict)

        for row_idx in range(1, len(self.raw_data)):
            country =  self.raw_data[row_idx][0]
            for col_idx in range(1, len(self.raw_data[0])):
                data_label = self.raw_data[0][col_idx]
                data = self.raw_data[row_idx][col_idx]

                # Deal with missing data.
                if not data:
                    data = None
                else:
                    data = float(data)

                self.country_dic[country][data_label] = data


    def query_by_country(self, country_name):
        """
        By giving a country name, returns data of this country.
        :param country_name: a string of country name.
        :return: a dictionary containing data of this country.
        """
        if country_name in self.country_dic:
            return self.country_dic[country_name]
        else:
            raise RuntimeError("Given country name is not included.")


    def query_by_label(self, label_name):
        """
        By giving a label name, returns the data under this label.
        :param label_name: a string of label name.
        :return: a list of data.
        """
        if label_name not in self.raw_data[0]:
            raise RuntimeError("Given label name is not in the query.")

        labeled_data = []
        idx = self.raw_data[0].index(label_name)

        for row in range(1, len(self.raw_data)):
            country = self.raw_data[row][0]
            data = self.raw_data[row][idx]
            if data:
                labeled_data.append([country, float(data)])
            else:
                labeled_data.append([country, None])

        return labeled_data
