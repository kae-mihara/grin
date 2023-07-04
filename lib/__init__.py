import os

base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

config = {
    'logs': '../../logs/'
}
datasets_path = {
    'air': '../../data/grin-data/air_quality',
    'la': '../../data/grin-data/metr_la',
    'bay': '../../data/grin-data/pems_bay',
    'synthetic': '../../data/grin-data/synthetic'
}
epsilon = 1e-8

for k, v in config.items():
    config[k] = os.path.join(base_dir, v)
for k, v in datasets_path.items():
    datasets_path[k] = os.path.join(base_dir, v)
