# Python Basic Tasks
# 1. Hello World
name = input("Enter your name: ")
print("Hello World ...", name)

# 2. Calculate Profit or Loss
cost_price = float(input("\nEnter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    print("Profit =", selling_price - cost_price)
elif cost_price > selling_price:
    print("Loss =", cost_price - selling_price)
else:
    print("No Profit, No Loss")

# 3. Check Odd or Even
num = int(input("\nEnter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# 4. Check Voting Eligibility
age = int(input("\nEnter your age: "))

if age < 0:
    print("Invalid age.")
elif age >= 18:
    print("Age is valid and you are eligible for voting.")
else:
    print("Age is valid, but you are not eligible for voting.")

# 5. Check Anagram
word1 = input("\nEnter first word: ")
word2 = input("Enter second word: ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("The words are Anagrams.")
else:
    print("The words are Not Anagrams.")
