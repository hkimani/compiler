## Mini compiler

### Requirements:
Python 3.6+

### Directory structure:
doc: Documentation and related files.  
src: Source code files for our mini-compiler psuedo language.  
src/common: Reusable code.  
src/scanner: Scanner implementation.  
src/parser: Parser implementation.  
src/tests: Test files.  
src/source: Mini language source files.  

### Running the program
install python (3.6+): https://www.python.org/

install pipenv:
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
python main.py <RELATIVE_PATH_TO_FILE>
```
Example:
```
cd src
python main.py source/main.spy
```
