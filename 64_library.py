# import time
# class Library:
#     def __init__(self, bookname,i):
#         self.books = bookname
#         self.i =i
#         print(self.books,"\n")       
#         print(f"THE TOTAL NUMBER OF BOOKS ARE : {self.i}")
# try:
#     a = int(input("KINDLY ENTER THE NUMBER OF BOOKS YOU WANT TO INSERT : "))
#     if type(a) is not int :
#         raise ValueError
#     for i in range (1,a+1):
#         b = input(f"THE {i}th BOOK NAME :  ")
#         libinsert = Library(b,i)
#         i+=1
# except ValueError as v:
#             print("KINDLY ENTER ONLY A NUMBER" , v)
# finally :
#             time.sleep(3)   # Delay for 3 seconds
#             print("Program ended.")

''' HARRY BHAI KA CODE '''

class Library:
  def __init__(self):
    self.noBooks = 0
    self.books = []
    
  def addBook(self, book):
    self.books.append(book)
    self.noBooks = len(self.books)

  def showInfo(self):
    print(f"The library has {self.noBooks} books. The books are")
    for book in self.books:
      print(book)


l1 = Library()
l1.addBook("Harry Potter1")
l1.addBook("Harry Potter2")
l1.addBook("Harry Potter3")
l1.showInfo()