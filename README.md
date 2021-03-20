## Mini-compiler
Course work: Implementation of a mini-compiler for a psuedo-python language

### Requirements:
Python 3.6+

### Directory structure:
doc: Documentation and related files <TODO>.  
src: Source code files for our mini-compiler psuedo language.  
src/common: Reusable code.  
src/scanner: Scanner implementation.  
src/parser: Parser implementation.  
src/tests: Test files.  
src/source: Mini language source files.  

### Running the program
Install python (3.6+): https://www.python.org/

Install pipenv:
```
pip install pipenv
```
Install dependencies:
```
pipenv install
```

Run:
```
cd src
python main.py <RELATIVE_PATH_TO_SOURCE_FILE>
```
Example:
```
cd src
python main.py source/main.spy
```
