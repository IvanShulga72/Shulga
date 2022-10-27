a = ["1" , "2" , "3"]
with open("data.txt", "w") as outfile:
        outfile.write("\n".join(a))