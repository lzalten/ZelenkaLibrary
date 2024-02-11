

class WebsiteHelper:

    def search_book(self, keyword):
        books = Book.objects.filter(
            Q(name__icontains=keyword) |
            Q(author__icontains=keyword) |
            Q(genre__name__icontains=keyword)
        )
        return books
