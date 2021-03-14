import csv

newmap = {
2: "PostFail",
4: "a",
5: "b",
6: "c",
7: "d",
8: "e",
9: "f",
10: "g",
11: "h",
12: "i",
13: "j",
14: "k",
15: "l",
16: "m",
17: "n",
18: "o",
19: "p",
20: "q",
21: "r",
22: "s",
23: "t",
24: "u",
25: "v",
26: "w",
27: "x",
28: "y",
29: "z",
30: "1",
31: "2",
32: "3",
33: "4",
34: "5",
35: "6",
36: "7",
37: "8",
38: "9",
39: "0",
40: "Enter",
41: "esc",
42: "del",
43: "tab",
44: "space",
45: "-",
47: "[",
48: "]",
56: "/",
57: "CapsLock",
79: "RightArrow",
80: "LetfArrow"
}

with open('export.csv', 'r') as in_file:
    reader = csv.DictReader(in_file)
    for line in reader:
        if line['Info'] == "URB_INTERRUPT in":
            if line['Leftover Capture Data'] != None and line['Leftover Capture Data'] != '':
                # print(line['Leftover Capture Data'].strip())
                bytesArray = bytearray.fromhex(line['Leftover Capture Data'].strip())
                # print(bytesArray)
                for byte in bytesArray:
                    if byte != 0:
                        keyVal = int(byte)
                        if keyVal in newmap:
                            print(newmap[keyVal], end ="")
                # print()