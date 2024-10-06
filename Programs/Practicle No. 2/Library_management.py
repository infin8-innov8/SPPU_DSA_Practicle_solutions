# Q.  Write a Python program for college library which has N books, write functions for following:
#       a) Delete the duplicate entries
#       b) Display books in ascending order based on cost of books
#       c) Count number of books with cost more than 500.
#       d) Copy books in a new list which has cost less than 500.
#       e) Function to take input for books and prices

def input_books():
    books = []
    N = int(input("Enter the number of books: "))
    
    for i in range(N):
        name = input(f"\n\tEnter the name of book {i+1} : ")
        cost = int(input(f"\tEnter the cost of book {i+1} : Rs. "))
        books.append({"name": name, "cost": cost})
    
    return books 

def remove_duplicates(books):
    unique_books = []
    seen = set()
    
    for book in books:
        if book["name"] not in seen:
            unique_books.append(book)
            seen.add(book["name"])
    
    return unique_books

def display_books_sorted_by_cost(books):
    n = len(books)
    for i in range(n):
        for j in range(0, n-i-1):
            if books[j]['cost'] > books[j+1]['cost']:
                books[j], books[j+1] = books[j+1], books[j]  # Swap
    
    print("\nBooks sorted by cost (Ascending Order):")
    for book in books:
        print(f"\tBook Name: {book['name']}, \tCost: Rs. {book['cost']}")

    print(f"\tBook Name: {book['name']}, \tCost: Rs. {book['cost']}")

def count_books_costing_more_than_500(books):
    count = 0
    for book in books:
        if book['cost'] > 500:
            count += 1
    return count

def copy_books_costing_less_than_500(books):
    cheaper_books = []
    for book in books:
        if book['cost'] < 500:
            cheaper_books.append(book)
    return cheaper_books

library_books = input_books()
library_books = remove_duplicates(library_books)
print("\nAfter removing duplicates : ")
for book in library_books:
    print(f"\tBook Name: {book['name']}, \tCost : Rs. {book['cost']}")
display_books_sorted_by_cost(library_books)
count_expensive_books = count_books_costing_more_than_500(library_books)
print(f"\nNumber of books costing more than 500 : {count_expensive_books}")
cheaper_books = copy_books_costing_less_than_500(library_books)
print("\nBooks with cost less than 500 :")
for book in cheaper_books:
    print(f"\tBook Name: {book['name']}, \tCost : Rs. {book['cost']}")
