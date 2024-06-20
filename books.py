from fastapi import Body, FastAPI, Query

app = FastAPI()

BOOKS = [
    {'title':'Title One', 'author':'Author One', 'category': 'science'},
    {'title':'Title Two', 'author':'Author Two', 'category': 'science'},
    {'title':'Title Three', 'author':'Author Three', 'category': 'history'},
    {'title':'Title Four', 'author':'Author Four', 'category': 'math'},
    {'title':'Title Five', 'author':'Author Five', 'category': 'math'},
    {'title':'Title Six', 'author':'Author Six', 'category': 'math'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book_by_title(book_title: str):
    for book in BOOKS:
        if book['title'].casefold() == book_title.casefold():
            return book
    return {"error": "Book not found"}

@app.get("/books-by-author")
async def read_books_by_author_and_category(author: str = Query(None), category: str = Query(None)):
    if author and category:
        books_to_return = [book for book in BOOKS if book['author'].casefold() == author.casefold() and book['category'].casefold() == category.casefold()]
    elif author:
        books_to_return = [book for book in BOOKS if book['author'].casefold() == author.casefold()]
    elif category:
        books_to_return = [book for book in BOOKS if book['category'].casefold() == category.casefold()]
    else:
        return {"error": "Provide author and/or category"}
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book