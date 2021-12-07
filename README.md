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
## Results

#### Experiments


[Rules](https://www.dbai.tuwien.ac.at/proj/argumentation/systempage/dung/adm.dl) 


[instances](http://argumentationcompetition.org/2019/iccma-instances.tar.gz)



#### Results

[ASP Results](https://github.com/maliabd-al-majid/dpdb_ASP/blob/main/Results.xlsx)


Some of the obtained results are presented in the table below:

| Instance  | CPU Time(seconds) | Tree width  | Solvable | 
| ------------- | ------------- | ------------- | ------------- |
| T-2-admbuster_10000  | 936.058  | 5 | OK |
| Small-result-b39  | 0.095  | 15 | OK |
| A-1-ferry2.pfile-L2-C1-05.pddl.3.cnf  | 28.212  | 22 | OK |
| Small-result-b53  | 1.356  | 47 | OK |
| Small-result-b22  | 0.744  | 31 | OK |
| Small-result-b10  | 2.788  | 48 | TLE |
| T-1-ferry2.pfile-L2-C4-07.pddl.2.cnf  | 18.833  | 69 | TLE |
| T-2-ferry2.pfile-L3-C3-03.pddl.2.cnf  | 53.357 | 89 | TLE |
| B-3-stb_767_429 | 26.431 | 927 | TLE |
| A-1-grd_2065_1_8  | 334.024 | 2928 | TLE |


