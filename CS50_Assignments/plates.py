def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 and len(s) > 6 :
        return False
    if s[0].isalpha()== False and s[1].isalpha() == False :
        return False

    for i in range(len(s)):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
    for ch in s:
        if ch in ['.' , ',' , ' ' , '!' , '?']:
            return False      
       
        
    return True   

main()