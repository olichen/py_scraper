# Takes a .json input file and formats it to a csv file
# Usage: python json_to_csv.py <input file>.json <output_file>.csv

import json
import sys
import html

# Simple argument handling
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as jfile:
    data = json.load(jfile)
    with open(output_file, 'w') as outfile:
        for paper in data:
            title = f'"{paper["title"]}","{paper["url"]}","{paper["date"]}"'
            for key, value in paper.items():

                def listToString(l):
                    nohtmllist = list(map(html.unescape,l))
                    return f'"{"; ".join(nohtmllist)}"'

                if isinstance(value, dict):
                    name = listToString(value['name'])
                    affil = listToString(value['affiliation'])
                    email = listToString(value['email'])
                    outstring = f'{title},{name},{affil},{email}\n'
                    outfile.write(outstring)
