

# def digitCount(num):
#     if num < 10:
#         return 1
#     else:
#         return 1 + digitCount(num // 10)

# def findMaxNum(num):
#     if len(num) == 1:
#         return num[0]
#     else:
#         maxValue = findMaxNum(num[1:])
#         return num[0] if num[0] > maxValue else maxValue

# def countHtmlTags(html, tag):
#     openingTag = f"<{tag}>"
#     closingTag = f"</{tag}>"
#     open_index = html.find(openingTag)
#     if open_index == -1:
#         return 0
#     close_index = html.find(closingTag, open_index)
#     return 1 + countHtmlTags(html[close_index + len(closingTag):], tag)

# def main():
#     while True:
#         print("Menu:")
#         print("1. Count Digits")
#         print("2. Find Max")
#         print("3. Count Tags")
#         print("4. Exit")
#         choice = input("Enter a choice: ")

#         if choice == "1":
#             n = int(input("Enter an integer: "))
#             print("Number of digits:", digitCount(n))
#         elif choice == "2":
#             lst = list(map(int, input("Enter a list of integers: ").split()))
#             print("Maximum value:", findMaxNum(lst))
#         elif choice == "3":
#             html = """
# <html>
# <head>
# <title>My Website</title>
# </head>
# <body>
# <h1>Welcome to my website!</h1>
# <p>Here you'll find information about me and my hobbies</p>
# <h2>Hobbies</h2>
# <ul>
# <li>Playing guitar</li>
# <li>Reading books</li>
# <li>Traveling</li>
# <li>Writing cool h1 tags</li>
# </ul>
# </body>
# </html>
# """
#             tag = input("Please Enter a tag: ")
#             print("Number of occurrences of the tag:", countHtmlTags(html, tag))
#         elif choice == "4":
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()