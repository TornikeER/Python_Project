# Python_Final_Project

Commits are on different branches. 

### Docker instruction
**4 step to run project using Docker**

1) Use this command to build the project 
```
docker-compose up -d --build
```
2) Use this command to run the App itself 
```
docker-compose run -it app
```
3) Use this custom-made command to create Data base for test runs  
```
create_db
```
4) Use this custom-made command to run all tests in "Test"  package

```
run_tests
```

## About Project 


The app was developed for processing and analysis of the genomic data.There are 3 general functions it does:

* DNA to RNA transcription,
* RNA to protein translation
* Creating plots of GC-content ratio in a given DNA sequence


### Project Structure
- `App`: the app root directory
  - `Data`: database related logic
    - `Constants.py`: Different types of data for Database and tests
    - `db_create.py`: this script creates database 
    - `db_tables.py`: constructions of Database 
    - `db_query.py`: data retrieving queries
  - `Scripts`: Main functions logic
    - `DnaToProteinFunctionScript.py`: converts dna to rna and then rna to protein
    - `DnaToProteinFunctionScriptUsingDatabases.py`: same as previous functions, but using database queries
    - `PlottingGraphFunctionScript.py`: Creates plot graph of any Genome
  - `Tests`: Tests of Main functions
    - `DnaToProteinFunctionScript.py`: DnaToProteinFunctionScript.py Test
    - `DnaToProteinFunctionScriptUsingDatabases.py`:[UnitTest] DnaToProteinFunctionScriptUsingDatabases Test
    - `PlottingGraphFunctionScript.py`:[UnitTest] PlottingGraphFunctionScript Test
  - `Dockerfile`: for app service container
  - `requirements.txt`: dependencies
  - `docker-compose.yaml`: for app and db services



