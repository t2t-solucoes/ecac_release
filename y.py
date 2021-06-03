import yaml

with open(r'./config.yaml') as file:
    content = yaml.load(file, Loader=yaml.FullLoader)
    print(content)