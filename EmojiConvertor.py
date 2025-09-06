def emojiconvertor(message):
    words = message.split(" ")
    emojis ={
        ":)":"😊",
         ":(": "☹️",
        "<3": "❤️",
        ":D": "😃"
    }

    output=""
    for word in words:
        output +=emojis.get(word,word) + " "
    
    return output

msg = input("Enter your message :")
print(emojiconvertor(msg))

