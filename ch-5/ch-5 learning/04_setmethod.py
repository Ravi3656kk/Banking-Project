reward = {
    "mukesh": 401,
    "dinesh": 501,
    "samir": 641,
    "naryan": 1001
}

print(reward.items())  # Prints all items before update

reward.update({"mukesh": 1000})  # ✅ Correct way to update

print(reward)  # ✅ Now you can see the updated dictionary
