import aqgFunction
import sys
from bs4 import BeautifulSoup

def getContentFromFile():
    
    # path to the HTML document to read content from
    html = open('/home/prashant/Desktop/QTR4/2488_000119312509245120_dex101.htm')
    bs = BeautifulSoup(html, "html.parser")
    li = bs.select('body')

    # path to the ./DB/db.txt file
    fp = open("/home/prashant/intern/productlab/Automatic-Question-Generator/AutomaticQuestionGenerator/DB/db.txt","w+")
    fp.write(li[0].text)
    fp.close()

# Main Function
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

