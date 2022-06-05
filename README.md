# pdf-processing

# About The Project
Small project, that helps with pdf processing.
It removes all end-line characters from pargraphs, specified inside the file, adds spaces between paragraphs and tabulations at the beginning of each paragraph if required.
Also possible to fully justify the document.

# Built With
Python 3.9.10

# Getting started
### Requirements

All required packages in requirements.txt file.

To install all required packages, type:
```console
pip install -r requirements.txt
```
 in the terminal.

### Working with pdf-processing:
1. Copy text you need to process to a *text_to_process.txt* or to any other file and save it.
2. Use *load_text_from_file* function to read data from file.
3. Use *process_data_to_txt* or *process_data_to_word* to process text accordingly to the format, you want to save in.
4. Use *save_data_to_txt* or *save_data_to_word* to save data corresponding to the function you used previously.
6. After successful execution, a file with proper extention (*.txt* or *.docx*) should be created with processed text.

# Usage
I personally use it as a quick way of processing pdf files for .docx usage (listening to the text).
In order to listen to the document without having breaks at the end-line characters, that are present when copying directly from pdf to word document, they need to be removed.
Manually processing all changes requires more time, than using the script.

Script project contains also a sample txt file for processing.

# Licence
Distributed under the MIT License. See LICENSE file for more information.
