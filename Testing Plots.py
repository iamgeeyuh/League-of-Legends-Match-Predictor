import csv

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            data.append(row)
    return data
Control_wards, wards, total_kills, dragon_kills, herald_kills, inhibitors, turret_plates = [], [], [], [], [], [], []
wins = []
# Example usage:
filename = 'match_data_v5.csv'  # Replace 'example.csv' with the name of your .csv file
csv_data = read_csv(filename)
for row in csv_data:
    Control_wards.append(row[1])
    wards.append(row[2])
    total_kills.append(row[3])
    dragon_kills.append(row[4])
    herald_kills.append(row[5])
    inhibitors.append(row[6])
    turret_plates.append(row[7])
    wins.append(row[8])
import matplotlib.pyplot as plt

def plot_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("The lists must be of equal length.")
    
    plt.bar(list1, list2)
    plt.xlabel('List 1')
    plt.ylabel('List 2')
    plt.title('Plot of List 1 against List 2')
    plt.show()

plot_lists(wins, total_kills)