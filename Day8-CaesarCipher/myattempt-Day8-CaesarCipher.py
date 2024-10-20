import string

def print_word_from_list(word):
    word1=""
    for letter in word:
        word1+=letter
    print(word1)

def caeser_cipher_encoder(message,shift):
    shift=shift%26
    list1=list(message.lower())
    list2=[] #indices of symbols
    list5=[] #symbols
    alphabets=list(string.ascii_lowercase)
    list3=alphabets[shift:]+alphabets[:shift] #acquiring the shifted list of alphabets
    list4=[] #encoded message
    for i in range(0,len(list1)):
        if list1[i] not in alphabets:
            list2.append(i) #storing indices of symbols from the message
            list5.append(list1[i]) #storing the symbols from the message 
    for i in range(len(list2)):
        x=int(list2[i])-i
        del list1[x] #deleting the symbols from the message
    for i in list1:
        list4.append(list3[alphabets.index(i)])
    for i in range(len(list2)):
        a=int(list2[i])
        b=list5[i]
        list4.insert(a,b)
    print_word_from_list(list4)
    
def caeser_cipher_decoder(message,shift):
    shift=shift%26
    list1=list(message.lower())
    list2=[] #indices of symbols
    list5=[] #symbols
    alphabets=list(string.ascii_lowercase)
    list3=alphabets[-shift:]+alphabets[:-shift] #acquiring the shifted list of alphabets
    list4=[] #decoded message
    for i in range(0,len(list1)):
        if list1[i] not in alphabets:
            list2.append(i) #storing indices of symbols from the message
            list5.append(list1[i]) #storing the symbols from the message 
    for i in range(len(list2)):
        x=int(list2[i])-i
        del list1[x] #deleting the symbols from the message
    for i in list1:
        list4.append(list3[alphabets.index(i)])
    for i in range(len(list2)):
        a=int(list2[i])
        b=list5[i]
        list4.insert(a,b)
    print_word_from_list(list4)
    
    
while(True):
    
    choice=input("Do you wish to 'encode' or 'decode'? ").lower()
    if choice=='encode':
        message=input("Please enter the message you wish to encode: ")
        shift=int(input("Please enter the shift: "))
        caeser_cipher_encoder(message,shift)
    elif choice=='decode':
        message=input("Please enter the message you wish to decode: ")
        shift=int(input("Please enter the shift: "))
        caeser_cipher_decoder(message,shift)
    else:
        print("We don't do that here!")
    choice1=input("\nDo you wish to continue? ").lower()
    if choice1=='yes':
        continue
    else:
        print("\nBye! Exiting.........")
        break

     

