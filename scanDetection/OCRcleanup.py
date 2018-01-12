'''Script to clean up the original OCR file

we want to:
    - get rid of non letter characters.
    - get rid of "CHAPTER #"
    - replace dashes with spaces unless EOL
    - get rid of line denoting the next file
    - make all characters lowercase
'''

import re

with open('testOCRFull.txt', 'r') as inputFile:

    with open('cleanTestData.txt', 'w') as output:

        newFileRE = re.compile("-+File:")
        figRE = re.compile("^.? ?[Ff]ig")
        reunite = None

        for line in inputFile:

            if line.isspace():
                continue
            if newFileRE.match(line) or figRE.match(line):
                continue
            if "CHAPTER" in line:
                continue

            line = line.lower()

            if reunite is not None:
                reunite = re.sub("[^a-z]", "", reunite)
                line = reunite + line
                reunite = None

            # line ends with - if you ignore whitespace, but not multiple
            # dashes.
            if line.rstrip()[-1] == '-' and line.rstrip()[-2] != "-":
                # save the word start
                reunite = line.rpartition(" ")[-1]
                # remove it from original line
                line = line.rsplit(' ', 1)[0]

            # now replace all with space
            line = line.replace("-", " ")
            # now strip all non letter chars.
            line = re.sub("[^a-z \n]", "", line)
            # write to new file
            output.write(line)
