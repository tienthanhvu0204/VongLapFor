letter = input ("Ký tự dùng là: ")
high = int (input ("Chiều cao hình là: "))
width = int (input ("Chiều rộng hình là: "))

for i in range (high):
    if i == 0 or i == high - 1:
        print (letter * width, sep = "")
    else:

        for j in range (width):
            if j == 0:
                print (letter, end = "")
            elif j == width - 1:
                print (letter)
            else:
                print (" ", end = "")


