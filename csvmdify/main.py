from markdownify import markdownify as md
import argparse
import json
import csv
from csv import DictReader

parser = argparse.ArgumentParser()


parser.add_argument('-if','--input', action='store', type=str, help="input file", required=True)
parser.add_argument('-of', '--output', action='store', type=str, help="output file", required=True)
args = parser.parse_args()

infile = args.input
outfile = args.output

content = []
headers = ['body']

with open(infile, "r", encoding="ISO-8859-1") as input:
    with open(outfile, "w", encoding="ISO-8859-1")as output:
        reader = DictReader(input)
        print("Reading File Contents....")
        for column in reader:
            content.append(column['body'])
        print("Cleaning Content Field....")
        for x, contents in enumerate(content):
            content[x] = md(contents)
        print("Writing to file....")
        writer = csv.writer(output)
        writer.writerow(headers)
        writer.writerows(zip(content))
        print("Done!")
