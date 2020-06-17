print("|----------------------|")
print("| Flat Converter-1.0.0 |")
print("|----------------------|")
print("")
print("------------------------------")
print("")
text1 = input("Input The Crackheads Text: ")
print("")
true = False
true2 = False
true3 = False

true = bool("flat" in text1)

if true == True:
	text2 = text1.replace("flat", "a globe" )

true2 = bool("globetards" in text1)

if true2 == True:
	text2 = text1.replace("globetards", "Normal people" )

true3 = bool("no curvature" in text1)

if true3 == True:
	text2 = text1.replace("no curvature", "a curvature" )

print("|---------------------|")
print("|" + text2 + " |")
print("|---------------------|")



