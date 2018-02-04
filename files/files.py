inputFile = open("input.txt","r")
outputFile = open("output.txt","w")

outputFile.write(inputFile.read())

inputFile.close()
outputFile.close()
