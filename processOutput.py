from os import listdir
from os.path import isfile, join
import csv
from datetime import datetime


def format_decimal(number):
    return str(number).replace('.', ',')

results_path = '/home/leonardo/projects/tcc/ttplab/output'
data_path = '/home/leonardo/projects/tcc/ttplab/database/TTP1_data/'

result_files = [f for f in listdir(results_path) if isfile(join(results_path, f))]
processed_results = []

### ADDING HEADER
header = ['test_file',
                    'instance_full_name',
                    'instance',
                    'instance_type',
                    'number_of_itens',
                    'capacity_of_knapsack',
                    'algo',
                    'instance_repeated',
                    'result',
                    'time']
processed_results.append(header)

for f in result_files:
    print(f)
    filename_splitted = f.split('_')
    instance = filename_splitted[0]
    number_of_itens = filename_splitted[1].replace('n', '')
    instance_type = filename_splitted[2]
    instance_full_name = f[:f.find('ttp')+3]
    capacity_of_knapsack = 0

    with open(join(data_path, instance + '-ttp', instance_full_name)) as reader:
        capacity_of_knapsack = float(reader.readlines()[4].split(' ')[3])

    with open(join(results_path, f)) as reader:
        for line in reader.readlines():
            processed_line = line.replace('\n', '')
            processed_line_splitted = processed_line.split(' ')
            algo = 'cs2b' if f.find('cs2b') > 0 else 'cs2sa'
            print(processed_line)
            result = [f,
                    instance_full_name,
                    instance,
                    instance_type,
                    format_decimal(number_of_itens),
                    format_decimal(capacity_of_knapsack),
                    algo,
                    processed_line_splitted[0],
                    format_decimal(processed_line_splitted[1]),
                    format_decimal(processed_line_splitted[2])]
            processed_results.append(result)
            

with open(datetime.now().strftime("%d-%m-%Y_%H-%M-%S")+'processed_result.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(processed_results)
