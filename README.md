# dpdb_ASP

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
```python
python3 nesthdb.py -f ./test_program.lp   --config Config.json_PATH_FILE
```
