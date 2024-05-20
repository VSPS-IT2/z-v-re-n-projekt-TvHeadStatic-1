def Dekrypshn(sajfr, kii_valju): #defines a function with the name dekrypšn
    plejn = ''
    for i in range(len(sajfr)): #decrypting loop
        speshl = sajfr[i]
        niev_speshl = speshl.lower() #makes the characters lowercase
        if niev_speshl == " ":
            plejn += ' ' #adds space if there space uwu
        elif speshl.isalpha(): #Checks if characters are in the Alphabet
            plejn += chr((ord(niev_speshl) - kii_valju - 97) % 26 + 97) #the MAGIC (decrypts the text)
    return plejn
    
def Enkrypshn(plejn, kii_valju): #defines a function with the name enkrypšn
    sajfr = ''
    for i in range(len(plejn)): #encrypting loop
        speshl = plejn[i]
        niev_speshl = speshl.lower()
        if niev_speshl == " ":
            sajfr += ' '
        elif speshl.isalpha():
            sajfr += chr((ord(niev_speshl) + kii_valju - 97) % 26 + 97) #the MAGIC (encrypts the text)
    return sajfr

while True:
    print('Welcome to the world of ciphering loves ;3..\n  Smack 1 for Decryption \n  Smack 2 for Encryption \n  Smack 0 to go away ')
    chojs = input('Your choice comes here love :3 :') #choice variables
    if chojs.isdigit():

        if chojs == '1': #Choice is 1, decrypting encrypted text
            Sa_sentnc = input('You gib cipher here: ')
            kii = int(input('You gib the move value here (only numbers bi-): '))
            print(f'Your decrypted text: {Dekrypshn(Sa_sentnc, kii)}')

        elif chojs == '2':  #Choice is 2, Encrypting plain text
            sentnc = input('You gib normal text here: ')
            kii = int(input('You gib the move value here (only numbers bi-): '))
            print(f'Your Encrypted text: {Enkrypshn(sentnc, kii)}')

        elif chojs == '0':  #Choice is 0, Shutting down program
            print('Leaving..:(..')
            break
        else:
            print('Exception error .. \n' #Invalid input
                  'Please insert 0 or 1 ')

    if chojs == '1' or chojs == '2': #Checks choices to inform the user special characters have been removed
        print('You though your sentence could be special?? (removed spec. chars.)')
    continiu = input('Are you staying for longer? [Any key/no]') #Variable asks user if they want to continue using the program or exit
    if continiu.lower() == 'no' or continiu.lower() == 'n': #If user chooses to leave, closes the program 
        print('Leaving..:(..')
        break
    else:
        pass
