import json,os
rows = []
reversedRows = []
file = "mapToRotate.txt"
def rotate_matrix( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
matrix = []
with open("./"+file) as f:
    content = f.read()
    jsonContent = json.loads(content)
    for rowContent in jsonContent:
        row = []
        for char in rowContent:
            row.append(char)
        matrix.append(row)
rots = []
rots.append(matrix)
r90 = rotate_matrix(matrix)
rots.append(r90)
r180 = rotate_matrix(r90)
rots.append(r180)
r270 = rotate_matrix(r180)
rots.append(r270)
finished = []
for rotations in rots:
    array = []
    for rows in rotations:
        row = "\""
        for char in rows:
            row += char
        row += "\","
        print(row)
    print("\n")
    finished.append(array)