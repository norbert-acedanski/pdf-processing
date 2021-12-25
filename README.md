# pdf-processing

# About The Project
Small project, that helps with pdf processing.
For now, there is only one file, that processes text copied from pdf to .txt file.
It removes all end-line characters from pargraphs, specified inside the file, adds spaces between paragraphs and tabulations at the beginning of each paragraph if required.
Unfortunately for now, amount of lines in each paragraph must be specified in program itself.

# Built With
Python 3.8.0

# Getting started
### Requirements
##### packages:
- docx (pip install python-docx)

### Working with pdf-processing:
1. Copy text you need to process to a .txt file and save it.
2. Make sure, that _targetFileName_ variable is set properly.
3. Count the number of lines in each paragraph and put it in _numberOfLinesInEachParagraph_ list.
4. Set _makeAdditionalSpacesBetweenParagraphs_ and _makeTabulationsAtTheBeginningOfTheParagraph_ variables accordingly.

# Usage
I personally use it as a not-so-quick way of processing pdf files for .docx usage (listening to the text).
In order to listen to the document without having breaks at the end-line characters, that are present when copying directly from pdf to word document, they need to be removed.
Manually processing all changes requires more time, than counting the lines and using the script.

Script project contains also a sample txt file for processing and number of lines inf each paragraph in _numberOfLinesInEachParagraph_ already specified.

# Licence
Distributed under the MIT License. See LICENSE file for more information.
