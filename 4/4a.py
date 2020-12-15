required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
counter = 0

# Open the file
f = open('passports.txt')
contents = f.read()
f.close()

passport_list = contents.split(",")

# passport_list = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
#                  "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
#                  "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm",
#                  "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in"]

def check_if_passport_valid(passport_data):
    for required_field in required_fields:
        if passport_data.find(required_field) == -1:
            return False
    return True

for passport_data in passport_list:
    if check_if_passport_valid(passport_data):
        counter += 1

print(counter)