import os


def extract_integer(filename):
    return int(filename.split('.')[0].split('_')[1])


base_folder = './folders'

all_2020_products = ['Ride-Iso-2-01', 'Freedom-Iso-3-01', 'Triumph-17', 'Guide-13-01', 'Peregrine-10-01', 'Peregrine-10-02', 'Cohesion-13', 'Triumph-18', 'Ride-Iso-2-02', 'Freedom-Iso-3-02', 'Guide-13-02', 'Kinvara-11-01', 'Kinvara-11-02',
                     'Clarion-2', 'Ride-13-01', 'Ride-13-02', 'Jazz-Original-Vintage-01', 'Jazz-Original-Vintage-02', 'Shadow-5000-01', 'Shadow-5000-02', 'Jazz-Original-01', 'Jazz-Original-02', 'Jazz-Original-03', 'Stopwatch-Long-Sleeve', 'Packaway-Jacket']

sorted_w_dot = sorted([f for f in os.listdir(
    base_folder) if not f.startswith('.')])

sorted_wo_dot = sorted(sorted_w_dot, key=extract_integer)

for i, value in enumerate(sorted_wo_dot):
    os.rename(os.path.join(base_folder, value),
              os.path.join(base_folder, all_2020_products[i]))
