# Never did python, but I copied this first. Will extend later.
# Not finished yet. Help is welcome to automate the whole thing.
#
import pickle
PIK = "00.pickle"

with open("bitcoin-file.txt") as file_in: # one P2PKH bitcoin address per line i.e starting with 1 dnt load other addresses 
    data = set()
    for line in file_in:
        dline = line.rstrip("\n")
        data.add(dline)
with open(PIK, "wb") as f:
    pickle.dump(data, f)
