#!/bin/bash

DB_NAME="notes.db" # database name into a Bash variable
DB_MODES=".mode table\n.headers ON\n"

# Phase 1 - Preparations
rm $DB_NAME # poistaa tietokannan edellisen ajon jäljiltä.

# Phase 2 - Add note
 cat inputs_2.txt | python main.py > outputs_2.txt
 echo -e "${DB_MODES}SELECT * FROM note;" | sqlite3 $DB_NAME
# Phase 3 - List notes
# cat inputs_3.txt | python main.py > outputs_3.txt
# Phase 4 - View note
# cat inputs_4.txt | python main.py > outputs_4.txt
# Phase 5 - Edit note
# cat inputs_5.txt | python main.py > outputs_5.txt
# Phase 6 - Delete note
# cat inputs_6.txt | python main.py > outputs_6.txt