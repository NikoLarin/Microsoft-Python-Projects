import time

def teletype_printer(text="test", wait=0.5):
    for text in text:
        print(text, end='', flush=True) # flush to print immediately and end'' to avoid new line
        time.sleep(wait) # wait alloted time between characters

text = input("Enter text to print in teletype style: ") 
wait = float(input("Enter wait time between characters (in seconds): "))

teletype_printer(text, wait) # call the function with user inputs

print()
print("Done printing")