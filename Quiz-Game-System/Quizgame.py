print("Welcome to quiz game")
score = 0

# Question 1
print("\nQ1: What is 2 + 2?")
print("a) 3")
print("b) 4")
print("c) 5")
ans = input("Your answer: ")

if ans == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
print("\nQ2: Capital of India?")
print("a) Delhi")
print("b) Mumbai")
print("c) Chennai")
ans = input("Your answer: ")

if ans == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 3
print("\nQ3: Which is a programming language?")
print("a) Python")
print("b) HTML")
print("c) CSS")
ans = input("Your answer: ")

if ans == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 4
print("\nQ4: 5 * 5 = ?")
print("a) 10")
print("b) 25")
print("c) 20")
ans = input("Your answer: ")

if ans == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 5
print("\nQ5: Sun rises from?")
print("a) West")
print("b) North")
print("c) East")
ans = input("Your answer: ")

if ans == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Final Score
print("\nYour Final Score:", score, "/5")
