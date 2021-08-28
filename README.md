# marathiSentenceCollector
A Simple Parsing script to read the content of epub book and create out put file with sentences suitable for Mozilla Common Voice Sentence Collector for Marathi language.

Steps :
    1. place the marathi epub file in the ./books directory.
    2. update the "bookpath" value in simpleParsing.py path to the particular book file.
        e.g. bookpath = "../books/sampleBook.epub"
    3. In terminal, go to the ./src directory and execute the script with following command :
        $ python simpleParsing.py
    4. the output file will be created in the ./output directory with local date and time stamp.
