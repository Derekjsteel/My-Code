#!/usr/bin/python3

#turn each line from the file into a list item.
data = open("CRY100_05_Lab_tags.txt").readlines()
#Split those items, using : as a delimiter.
dct = {item.split(":")[0]:item.split(":")[1] for item in data}
#Remove \n from the end of the lines.
cleaned = {key.strip(): item.strip("\n") for key, item in dct.items()}
keys_only = []
vals_only = []
for item in cleaned.keys():
    keys_only += [item]
for item in cleaned.values():
    vals_only += [item]
f_pt = open("pt.txt", "w+")
f_hash = open("hashes.txt", "w+")
for item in keys_only:
    f_pt.write(item + "\n")
for item in vals_only:
    f_hash.write(item + "\n")

p_hash = open("truehash.txt").readlines()
p2_hash = open("posthash.txt", "w+")
dct2 = {item.split(":")[0]:item.split(":")[1] for item in p_hash}
#Remove \n from the end of the lines.
cleaned2 = {key.strip(): item.strip("\n") for key, item in dct2.items()}
hashes_only = []
for item in cleaned2.values():
    hashes_only += [item]
for item in hashes_only:
    p2_hash.write(item + "\n")