studentDict = dict()
with open("./students.dat") as file:
  for line in file:
    studentData = line.split(" ")
    studentDict.update({studentData[0] : tuple((studentData[1],studentData[2],studentData[3].replace("\n","")))})

for student in studentDict:
  print(student + " " + str(studentDict[student]))