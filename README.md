# Tbt

## Installing packages

To install all the required packages run:

```shell
pip install -r requirements.txt
```

> Not all dependencies listed are required. We should clean everything up!

Adding a new package is down via the utility script `add_dependency.py` instead of `pip`. This is done for book-keeping reasons. For example, installing `numpy` can be achieved as such:

```shell
./add_dependency.py numpy
```

> Make sure you make the script executable via `chmod +x add_dependency.py`) (or simply run it via `python`).

## External Links:

- [Planet Labs](https://github.com/planetlabs/planet-amazon-deforestation)
