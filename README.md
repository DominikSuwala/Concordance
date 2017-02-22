# Concordance

Concordance processes input text and produces a list of words, their frequencies, and itemizes which sentences they occur in.

## Running

Libraries used are part of the standard Python library. This was written for the Python 2.7 interpreter.

> python concordance.py

## Usage

The program uses STDIN to prompt for the filename to process and prints the concordance to STDOUT. The working directory is the directory containing the Python script. Drag-and-dropping a file into the terminal will populate the entry with the absolute path to whichever file you wish to process.

## Design Choice

No concordance program is perfect for the English language due to nuances. I came up with my own regex which terminates sentences after seeing a punctuation point, followed by any number of whitespaces, followed by a capital letter. It's generally ill-advised to start a sentence with a digit, so I opted to not use the regex published by others. The regex choice is appropriate for the scope of this program.

Read more on Wikipedia: https://en.wikipedia.org/wiki/Sentence_boundary_disambiguation

If a word is too large for the field size in printing, the word is truncated with an ellipsis. 
