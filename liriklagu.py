import sys
import time

def gabut():
    lirik = [
        ("\nForget about where we are", 0.1),
        ("And let go, were so close", 0.09),       
        ("If you dont know where to start", 0.1),
        ("Just hold on and dont run", 0.08),
        ("No...", 0.03),
        ('\nIm sorry if i say, "I need you"', 0.08),
        ('But i dont care, Im not scared of love', 0.08),
        ('Cause when im not with you, Im weaker', 0.05),
        ('Is that so wrong? Is it so wrong?', 0.05),
        ('\nIf happy-ever-afters did exist', 0.07),
        ('I would still be holding you like this', 0.08),
        ('And all those fairy tales are full of shit', 0.07),
        ('One more fucking love song,Ill be sick', 0.07),
        ('Now Im at a Payphone',0.08)
        ]

    delay = [0.4, 0.4, 0.3, 0.3, 0.1]
    print('Where We Are - One Direction'),
    print('Strong - One Direction'),
    print('Payphone - Maroon 5'),
    time.sleep(2)
    for i,(baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(0.5) 
        print('')
        time.sleep(0.5) 

    print("//Code lyric by Prds")

gabut()
