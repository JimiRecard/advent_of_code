import hashlib
import pathlib

path = pathlib.Path(__file__).parent.resolve()

input_hash = open(f"{path}/input.txt").read()

first = True
for i in range(int(1e7)):
    string = f"{input_hash}{i}".encode()
    if first and hashlib.md5(string).hexdigest()[0:5] == "00000":
        first = False
        print(i)  # anser: 282749
    elif hashlib.md5(string).hexdigest()[0:6] == "000000":
        print(i)  # anser: 9962624
        break
