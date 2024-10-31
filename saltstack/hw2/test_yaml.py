import yaml
from pprint import pprint

with open('main.yaml', 'r') as f:
  data = yaml.safe_load(f)

pprint(data)
