#import os

path = "/workspaces/54375901/figlet/fonts.txt"
with open(path, "r") as f:
    file = f.readlines()


fonts = []
for line in file:
    fonts.append(line.split('\t')[0].strip())
fonts.pop(0)
print("[")
for font in fonts:
    print(f"'{font}',")
print("]")