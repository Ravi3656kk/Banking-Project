import random  # ✅ Needed for random.randint()

def game():
    print("You are playing the game...")
    score = random.randint(1, 62)

    # Fetch the hiscore
    try:
        with open("hiscore.txt", "r") as f:
            hiscore = f.read()
            hiscore = int(hiscore) if hiscore.strip() != "" else 0
    except FileNotFoundError:
        hiscore = 0

    print(f"Your score: {score}")

    # Update high score if necessary
    if score > hiscore:
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
        print("New high score!")
    else:
        print(f"High score remains: {hiscore}")

    return score

# ✅ Call the function
game()
