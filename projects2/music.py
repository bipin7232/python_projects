import time
import sys


lyrics = [
    ("But baby, let's face it", 1.2),
    ("I'm not into dating", 1.2),
    ("I haven't been patient", 1.4),
    ("Ever since I been famous my time has been racing", 1.7),
    ("My motives are basic, this life I've been chasing", 1.9),
    ("These hearts I've been breaking\n", 1.8),
  
    ("And these girls I been tasting don't never get naked", 2.0),
    ("Just put it in a ponytail, fuck 'em from behind", 1.8),
    ("Fuck 'em with their clothes on, panties to the side", 1.8),
    ("Put the panties to the side, like a done deal\n", 1.5),
  
    ("Get it wet, let it slide like a sunroof", 2.2),
    ("Got goals, got dreams, got hoes, got cribs", 1.8),
    ("Got niggas that'll die for a prince", 1.5),
    ("Got my city on lock, XO 'til the death", 1.5),
    ("Left town in a coach, came back in a jet", 2.0),
]

# Colors
WHITE = "\033[34m"
RESET = "\033[0m"

def play_lyrics():
    for line, delay in lyrics:
        if line == "":
            print("") 
        else:
            
            sys.stdout.write(WHITE + line + RESET + "\n")
            sys.stdout.flush()
        
        time.sleep(delay)

if __name__ == "__main__":
    play_lyrics()