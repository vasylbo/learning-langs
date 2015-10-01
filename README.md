# learning-langs
Scripts made to help learning languages

### makeTranslator.py

Used to create a csv-based dictionary from original text language to specified one. 
It has no any heuristics and takes all words excluding ones that have less than two letters. 
You can use it by inlining parameters in code or running it from command line. For example:
```
python makeTranslator.py book.txt translation.csv en uk
```
