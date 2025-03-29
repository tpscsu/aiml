books_purchased = int(input("Enter the number of books you purchased this month : "))

if books_purchased == 0:
    points = 0
elif 2 <= books_purchased < 4:
    points = 5
elif 4 <= books_purchased < 6:
    points = 15
elif 6 <= books_purchased < 8:
    points = 30
elif books_purchased >= 8:
    points = 60
else:
    points = 0

print("You have earned {} points.".format(points))
