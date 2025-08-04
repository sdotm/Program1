# Simple Kaun Banega Crorepati Game

print("Welcome to Kaun Banega Crorepati!\n")

# List of questions, options, answers, and prize money
questions = [
    ["What is the capital of India?", "A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai", "B", 1000],
    ["Which gas do plants absorb?", "A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen", "C", 5000],
    ["Who is known as the father of computers?", "A) Alan Turing", "B) Steve Jobs", "C) Charles Babbage", "D) Bill Gates", "C", 10000],
    ["How many states are there in India?", "A) 27", "B) 28", "C) 29", "D) 30", "B", 20000],
    ["Who wrote the national anthem of India?", "A) Rabindranath Tagore", "B) Bankim Chandra", "C) Mahatma Gandhi", "D) Nehru", "A", 50000]
]

total_prize = 0

for q in questions:
    print(q[0])
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])
    
    answer = input("Enter your answer (A/B/C/D): ").upper()
    
    if answer == q[5]:
        total_prize = q[6]
        print("Correct! You won Rs.", total_prize)
    else:
        print("Wrong answer.")
        print("You take home Rs.", total_prize)
        break

print("Game Over. Thank you for playing!")
