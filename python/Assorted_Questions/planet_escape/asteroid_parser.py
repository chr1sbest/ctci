import json

def asteroid_parser(filename):
    """
    Build a list of asteroid tuples from a JSON file.
    """
    assert filename.split('.')[-1] == 'json', 'File must be JSON'
    with open(filename) as json_file:
        data = json.load(json_file)
        asteroids = []
        for asteroid in data[u'asteroids']:
            ast_tuple = (asteroid[u'offset'], asteroid[u't_per_asteroid_cycle'])
            asteroids.append(ast_tuple)
    return asteroids

if __name__ == "__main__":
    filename = 'chart.json'
    asteroid_parser(filename)
