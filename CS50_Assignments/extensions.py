x = input("File Name: ")
x = x.lower()

if ".jpg" or ".jpeg" in x:
    print("image/jpeg")
        
elif ".gif" in x:
    print("image/gif")
    
elif ".png" in x:
    print("image/png")
    
elif ".pdf" in x:
    print("application/pdf")
    
elif ".txt" in x:
    print("text/plain")
    
elif ".zip" in x:
    print("application/zip")
    
else:
    print("application/octet-stream")