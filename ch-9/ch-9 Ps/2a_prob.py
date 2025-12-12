
import random

def game():
      print("lets paly the game.")
      score = random.randint(2,111)

      with open("anchal.txt") as f:
            hiscore = f.read
            if(hiscore!=""):
                  hiscore = int(hiscore)
            else:
                  hiscore = 0
            print(f"youe score: {score}")

      with open("anchal.txt", "w") as f:
            f.write(str(score))
            
            return score
      
game()
