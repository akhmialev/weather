import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = input("Введите название файла с расширением\n"
                 "пример: minsk.csv ")

# Статические данные
date_column = int(input("Введите номер колонки с датой: ")) - 1
temp_max_column = int(input("Введите номер колонки с макс.температурой: ")) - 1
temp_min_column = int(input("Введите номер колонки с мин.температурой: ")) - 1
data, tmax, tmin = [], [], []

with open(filename) as f:
    read = csv.reader(f)

    for row in read:
        try:
            data_current = datetime.strptime(row[date_column], '%Y-%m-%d')
            tmaxs = (int(row[temp_max_column]) - 32) / 1.8
            tmins = (int(row[temp_min_column]) - 32) / 1.8
        except Exception:
            print("Что-то пошло не так!")
        else:
            data.append(data_current)
            tmax.append(tmaxs)
            tmin.append(tmins)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(data, tmax, c='red', alpha=0.5)
    ax.plot(data, tmin, c='blue', alpha=0.5)
    plt.fill_between(data, tmax, tmin, facecolor='blue', alpha=0.1)

    plt.title(f"Температура с {data[1]} по {data[-1]} ", fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Температура (цельсия)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
