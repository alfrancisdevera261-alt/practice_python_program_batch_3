number_seen = []
while True:
    ask_number = int(input("Enter a number: "))
    
    if number_seen.count(ask_number) != 0:
        print("Duplicate")
        break