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

```bash
pip install psycopg2
pip install future-fstrings

```

## Configuration
Basic configuration (database connection, htd path, ...) are configured in **config.json**

## Usage

```python
python3 decomposer.py ./test_program.lp
```
