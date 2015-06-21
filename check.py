import glob
import toml

for filename in glob.glob('*.toml'):
    with open(filename) as fh:
        toml.load(fh)

