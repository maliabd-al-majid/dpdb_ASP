# Nesthdb and Dpdb

Solve dynamic programming problems on tree decomposition using databases

## Installation

### Database

[Postgresql](https://www.postgresql.org/)

### htd 

[htd Github](https://github.com/TU-Wien-DBAI/htd/tree/normalize_cli)

### clingo

```bash
pip install clingo
```
### Python
* Python 3
* psycopg2
* future-fstrings
* Clingo

```bash
pip install psycopg2
pip install future-fstrings
pip install clingo
```

## Configuration
Basic configuration (database connection, htd PATH, ...) are configured in **config.json**
### Nesthdb
* configuration (database connection, htd PATH, guess_min.lp PATH, guess_increase.lp PATH) are configured in **config.json**
## Usage
### DPDB
```python
python3 decomposer.py ./test_program.lp
```
### Nesthdb
#### Ground program with gringo
```python
gringo ./test_program.lp --text > ground_program
```
#### Run Nesthdb to the obtained Ground program
```python
gringo ./test_program.lp --text
python3 nesthdb.py -f ./ground_program  --config Config.json_PATH_FILE
```
