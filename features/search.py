import os

def localSearch(filename, path):
    locations = []
    for root, dirs, files in os.walk(path):
        if filename in files:
            locations.append(str(os.path.join(root, filename)))
    return locations