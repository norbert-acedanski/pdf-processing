# pdf-processing

# About The Project
Small project, that helps with pdf processing.
For now, there is only one file, that processes text copied from pdf to .txt file.
It removes all end-line characters from pargraphs, specified inside the file, adds spaces between paragraphs and tabulations at the beginning of each paragraph if required.
Also possible to fully justify the document.
Unfortunately for now, amount of lines in each paragraph must be specified in program itself.

# Built With
Python 3.8.0

# Getting started
### Requirements

All required packages in requirements.txt file.

To install all required packages, type "_pip install -r requirements.txt_" in the terminal.

### Working with pdf-processing:
1. Copy text you need to process to a .txt file and save it.
2. Make sure, that *target_filename* variable is set properly.
3. Count the number of lines in each paragraph and put it in *number_of_lines_in_each_paragraph* list.
4. Set *make_additional_spaces_between_paragraphs*,  make_tabulations_at_the_beginning_of_the_paragraph* and *fully_justify_paragraph* variables accordingly.
5. Run the script.
6. After successful execution, 2 files should be created: .docx and .txt file with processed text.

**Note:** Script checks whether, during the processing, word at the beginning of the paragraph starts with lowercase letters. If it does, script will send logging information about possible mistake in counting the lines and exit the execution.
If you have lowercase letters if your pdf file at the beggining of the paragraph, script will count them as fails in counting.

# Usage
I personally use it as a not-so-quick way of processing pdf files for .docx usage (listening to the text).
In order to listen to the document without having breaks at the end-line characters, that are present when copying directly from pdf to word document, they need to be removed.
Manually processing all changes requires more time, than counting the lines and using the script.

Script project contains also a sample txt file for processing and number of lines inf each paragraph in *number_of_lines_in_each_paragraph* already specified.

# Licence
Distributed under the MIT License. See LICENSE file for more information.
