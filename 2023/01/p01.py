calibration_list = []
real_calibration_list = []

eq_dict = {
    "oneight": "18",
    "twone": "21",
    "threeight": "38",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "nineight": "98",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


with open("input.txt", "r") as file:
    for line in file.readlines():
        digits = [l for l in line if l.isnumeric()]
        cal = int(f"{digits[0]}{digits[-1]}")
        calibration_list.append(cal)

        for k, v in eq_dict.items():
            while k in line:
                line = line.replace(k, v)

        new_digits = [l for l in line if l.isnumeric()]
        new_cal = int(f"{new_digits[0]}{new_digits[-1]}")
        real_calibration_list.append(new_cal)

print(sum(calibration_list))  # answer: 54605
print(sum(real_calibration_list))  # answer: 55429
