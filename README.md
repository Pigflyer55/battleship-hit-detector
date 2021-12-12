# CISC/CMPE 204 Modelling Project

Welcome to the major project for CISC/CMPE 204 (Fall 2021)!

Our project consists of finding the best tile to attack in order to get a hit. Our model merely provides a suggestion based on all the possible states of the board and there are still chances for this model to attack tiles that do not contain a ship. We use the permutations of the active ships on the board as well as the board setup that the user manually inputs. This model assumes all data entered has come from a possible board state. Using an impossible board state can create undesired results.

## Structure

* `documents`: Contains folders for both of your draft and final submissions. README.md files are included in both.
* `run.py`: General wrapper script that you can choose to use or not. Only requirement is that you implement the one function inside of there for the auto-checks.
* `test.py`: Run this file to confirm that your submission has everything required. This essentially just means it will check for the right files and sufficient theory size.
