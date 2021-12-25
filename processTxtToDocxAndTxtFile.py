import sys
from docx import Document

numberOfLinesInEachParagraph = [1, 1, 1, 7, 6, 10, 8, 9]

makeAdditionalSpacesBetweenParagraphs = True
makeTabulationsAtTheBeginningOfTheParagraph = False

targetFileName = "textToProcess.txt"
document = Document()

def saveAsNewFile(processedText):
    with open('processedText.txt', 'w', encoding='utf-8') as outFile_TXT:
        outFile_TXT.write(processedText)
    document.add_paragraph(processedText)
    document.save('processedText.docx')

def copyAndFixTextFromFile(inputFileName):
    fileContent = ""
    countLines = 1
    countParagraphs = 0
    with open(inputFileName, 'r', encoding='utf-8') as inFile:
        for (lineNumber, lineContent) in enumerate(inFile):
            temporaryLine = lineContent
            if countLines == 1:
                if temporaryLine[0].isalpha():
                    if temporaryLine[0].islower():
                        print("Possible mistake in counting the lines. Line, that mistake occurred: " + str(lineNumber + 1))
                        sys.exit()
                if makeTabulationsAtTheBeginningOfTheParagraph:
                    temporaryLine = '\t' + temporaryLine
            if countLines == numberOfLinesInEachParagraph[countParagraphs]:
                if makeAdditionalSpacesBetweenParagraphs:
                    temporaryLine +='\n'
                countLines = 1
                countParagraphs += 1
            else:
                temporaryLine = temporaryLine.replace("\n", " ")
                countLines += 1
            fileContent += temporaryLine
    fileContent = fileContent[:-1]
    return fileContent

if __name__ == '__main__':
    processedText = copyAndFixTextFromFile(targetFileName)
    saveAsNewFile(processedText)
