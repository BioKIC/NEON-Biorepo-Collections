import os, csv, json
# ***** Configure generator ******
version = "1"
groupBy = "collections"
structure = os.path.join("api", "v"+version, groupBy)

inputFilename = "all-colls-biorepo-20200910.csv"
outputFilename = "index.json"

inputfile = os.path.abspath(os.path.join("data", inputFilename))
outputfile = os.path.abspath(os.path.join(structure, outputFilename))

os.makedirs(os.path.dirname(outputfile), exist_ok=True)

# # Read the CSV and add data to a dictionary
with open(inputfile) as csvFile:
  csvReader = csv.DictReader(csvFile)

  # Add data to a root node
  root = {}
  root[groupBy] = [row for row in csvReader]

  # # Write data to JSON file
  with open(outputfile, "w") as jsonFile:
    jsonFile.write(json.dumps(root, indent=4))
  print("Created JSON file for NEON biorepo collections")