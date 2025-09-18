import random

choices = {"stone": "🪨", "paper": "📄", "scissors": "✂️"}
options = list(choices.keys())

user = input("Enter stone/paper/scissors: ").lower()
comp = random.choice(options)

print(f"You chose: {choices.get(user, user)}")
print(f"Computer chose: {choices[comp]}")

if user == comp:
    print("It's a tie!")
elif (user == "stone" and comp == "scissors") or \
     (user == "paper" and comp == "stone") or \
     (user == "scissors" and comp == "paper"):
    print("🎉 You win!")
else:
    print("💻 Computerr wins!")
