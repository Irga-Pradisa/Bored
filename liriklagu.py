import sys
import time

def gabut():
    lirik = [
        ("Mask on, Fuck it, Mask off", 0.1),
        ("Mask on, Fuck it, Mask off", 0.09),       
        ("Percocets, Molly, Percocets", 0.1),
        ("Chase a check, never chase a BITCH", 0.08),
        ("Don't chase no BITCHES", 0.03),
    ]

    delay = [0.4, 0.4, 0.3, 0.3, 0.1]
    print("\n<<Mask Off - Future>>")
    time.sleep(2)
    for i,(baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(0.5) # Add a delay after printing each line
        print('')
        time.sleep(0.5) # Add a delay after printing each line

    print("//Code lyric by Prds")

# Call the function to run the lyrics display
gabut()