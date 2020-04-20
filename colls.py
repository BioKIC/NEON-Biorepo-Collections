import os, csv, json
# ***** Configure generator ******
version = "0"
groupBy = "collections"
structure = os.path.join("api", "v"+version, groupBy)

# inputFilename = "all-colls.csv"
inputFilename = "all-colls-biorepo-20200416.csv"
outputFilename = "index.json"

inputfile = os.path.abspath(os.path.join("data", inputFilename))
outputfile = os.path.abspath(os.path.join(structure, outputFilename))

os.makedirs(os.path.dirname(outputfile), exist_ok=True)

# # Read the CSV and add data to a dictionary
with open(inputfile) as csvFile:
  csvReader = csv.DictReader(csvFile)
  # for csvRow in csvReader:
  #   data[csvRow] = {[csvRow]}
  #   fullname = csvRow["fullname"]
  #   data[fullname] = csvRow
# print(data)

  # Add data to a root node
  root = {}
  root[groupBy] = [row for row in csvReader]
  # # Write data to JSON file
  with open(outputfile, "w") as jsonFile:
    # jsonFile.write(json.dumps([row for row in csvReader], indent=4))
    jsonFile.write(json.dumps(root, indent=4))
  print("Created JSON file for collections")