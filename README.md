# Automatic Question Generator [AQG]
Automatic Question Generator from Text


Prerequisites
-------------
```
- Python 3.5+
- NLTK
- SpaCy
- NumPy
- BeautifulSoup
```

## Quickstart

### Run a textfile
```
python main.py 

```


## Example
### input:
```
My best friend and I have been studying in the same school since kindergarten. We have been classmates each year at 
school. We share a very close bond and have a special friendship that we cherish and treasure. My friend is my 
partner, sitting beside me in class. She is kindly and helpful, and if I have any difficulties in understanding any 
topic in my studies, or in completing my homework or school project, she helps me. She is brilliant in mathematics 
and the sciences, while I am good at English. So we both help each other in whatever way possible. She helps me 
without ever belittling me. I greatly appreciate the quality in her. She does not make me feel obliged.
```

### output:
```
Q-01: Who have been studying in the same school since kindergarten?
Ans: My best friend and I have been studying in the same school since kindergarten
----------
Q-02: What have you been at school?
Ans:  We have been classmates each year at  school
----------
Q-03: Who have been classmates each year at school?
Ans:  We have been classmates each year at  school
----------
Q-04: Who have a special friendship that you cherish and treasure?
Ans:  We share a very close bond and have a special friendship that we cherish and treasure
----------
Q-05: Who cherish and treasure?
Ans:  We share a very close bond and have a special friendship that we cherish and treasure
----------
```
 
# Main Function
## main.py
```python
  def main():

      # Create AQG object
      aqg = aqgFunction.AutomaticQuestionGenerator()

      # store your content into ./DB/db.txt file
      # Use the function getContentFromFile
      inputTextPath = "./DB/db.txt"
      readFile = open(inputTextPath, 'r+', encoding="utf8")

      inputText = readFile.read()
      #inputText = '''I am Dipta. I love codding. I build my carrier with this.'''

      questionList = aqg.aqgParse(inputText)
      # print(questionList)
      aqg.display(questionList)

      return 0


  # Call Main Function
  if __name__ == "__main__":
      main()
 
```


|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
===================================================================================================


## Reference (Code taken from): [Here](https://github.com/dipta1010/Automatic-Question-Generator)

### Other References
Automatic question generation by using NLP : [Here](https://github.com/indrajithi/genquest)
