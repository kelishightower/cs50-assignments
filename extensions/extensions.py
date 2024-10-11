# extensions.py
# Kelis Hightower

# gathering data from user, plus making it case insensitive

image = input("Enter a media name: ").strip().lower()

# if statments that decide what to print based of image suffix
if image.endswith(".gif"):
    print("image/gif")
elif image.endswith(".jpeg") or image.endswith(".jpg"):
    print("image/jpeg")
elif image.endswith(".png"):
    print("image/png")
elif image.endswith(".pdf"):
    print("application/pdf")
elif image.endswith(".txt"):
    print("text/plain")
elif image.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
