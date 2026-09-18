import time, sys

def slowam(text, delay):
    "The first parameter is the text itself, and the second is the typing speed; example: `slowam('hello,world!', 0.5)`."
    if isinstance(text,int):
            print("[ERROR] You cannot enter numbers without ''!")
            sys.exit(1)
    else:
         pass
    for c in str(text):
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
        

