#extensions
user_extension=input("File extension:")
if user_extension.endswith(".gif"):
    print("image/gif")
elif user_extension.endswith(".jpg") or user_extension.endswith(".jpeg") :
    print("image/jpeg")
elif user_extension.endswith(".png"):
    print("image/png")
if user_extension.endswith(".pdf"):
    print("text/pdf")
elif user_extension.endswith(".txt"):
    print("text/text")
