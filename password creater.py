import random

letters = ["a", "b", "c", "d", "f", "e"]
specials = ["_", "-", "#", ".", "!", "/", "{"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Welcome to Password Creator!\n")


let = []
print("Do you want to add letters? (yes/no)\n")
ad_let = input().strip().lower()
if ad_let == "yes":
    print("How many characters do you need?\n")
    ad_let_cr = int(input().strip())
    let = random.sample(letters, ad_let_cr)

spc = []
print("Do you want to add special characters? (yes/no)\n")
ad_spc = input().strip().lower()
if ad_spc == "yes":
    print("How many characters do you need?\n")
    ad_spc_cr = int(input().strip())
    spc = random.sample(specials, ad_spc_cr)


num = []
print("Do you want to add numbers? (yes/no)\n")
ad_num = input().strip().lower()
if ad_num == "yes":
    print("How many characters do you need?\n")
    ad_num_cr = int(input().strip())
    num = random.sample(numbers, ad_num_cr)

total = let + spc + num
random.shuffle(total)


password = ''.join(total)

print(f"Generated password: {password}")





