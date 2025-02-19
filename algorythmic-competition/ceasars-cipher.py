txt = input("nco: ")
posun = int(input('posun:'))

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
outcome = ''

# cyklus pro pusunuti kazdeho pismene
for letter in txt:
    if letter == " ":
        outcome = outcome + letter
        continue
    pos = alphabet.index(letter)

    pos += posun
    pos = abs(pos % len(alphabet))
    outcome = outcome + alphabet[pos]

print(outcome)