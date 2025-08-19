nam = input("What is your name?: ")

def are_you_playing_banjo(name):
    x = nam.startswith("R") or nam.startswith("r")
    print(x)
    return name
