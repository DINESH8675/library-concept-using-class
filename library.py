class library:
  def __init__(self,book):
    self.booklist=book
  def show(self):
    print(*self.booklist)
  def lend_book(self,book_name):
    if book_name in self.booklist:
      self.booklist.remove(book_name)
      print("thank your book  issed")
      return True
    else:
      print("book is not available")
      return False
  def return_book(self,book_name):
    self.booklist.append(book_name)
    return True

class customer:
  def __init__(self):
    self.booklist=[]
  def add_book(self,book_name):
    self.booklist.append(book_name)
  def show(self):
    print(self.booklist)
  
  def request_book(self):
    print("enter the book")
    self.book=input()
    return self.book
  def return_book(self):
    print("enter book to checking")
    self.book=input()
    return self.book
  def lend_booktolib(self,book_name):
    if book_name in self.booklist:
      self.booklist.remove(book_name)
      print("you retrun correct book and book name is",book_name,"thank you")
      status=lib_cbe.return_book(book_name)
      return True
    else:
      print("you return wrong book")
      

lib_cbe=library(["book1","book2","book3","book4","book5"])
dinesh=customer()
while True:
  print("----------------------------------------------------")
  print("select the option below")
  print("1--show the list of book,\n2-lent a book,\n0 -exit,\n3--book list,\n4-return a book")
  option=int(input())
  if option==1:
    lib_cbe.show()
  elif option==2:
    requested_book=dinesh.request_book()
    status= lib_cbe.lend_book(requested_book)
    if status==True:
      sandeep.add_book(requested_book)
  elif option==3:
     sandeep.show()
  elif option==4:
    returned_book=dinesh.return_book()
    status=dinesh.lend_booktolib(returned_book)

  elif option==0 :
     break
