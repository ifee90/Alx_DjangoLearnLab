### Examples: Filtering, Searching & Ordering Books

- **Filter by title:**  
`GET /api/books/?title=things fall apart`

- **Filter by author ID:**  
`GET /api/books/?author=1`

- **Filter by publication year:**  
`GET /api/books/?publication_year=1958`

- **Search by keyword (title or author name):**  
`GET /api/books/?search=things`

- **Order by title (ascending):**  
`GET /api/books/?ordering=title`

- **Order by publication year (descending):**  
`GET /api/books/?ordering=-publication_year`
## 📚 API Endpoints

### Authors
- **List & Create Authors**
  - URL: `/api/authors/`
  - Methods: `GET`, `POST`
- **Retrieve, Update & Delete Author**
  - URL: `/api/authors/<id>/`
  - Methods: `GET`, `PUT`, `PATCH`, `DELETE`

### Books (Generic Views)
- **List Books**
  - URL: `/api/books/`
  - Method: `GET`
  - Features: Filtering (`?title=`, `?author=`, `?publication_year=`), Search (`?search=`), Ordering (`?ordering=title`, `?ordering=-publication_year`)
- **Retrieve Book**
  - URL: `/api/books/<id>/`
  - Method: `GET`
- **Create Book**
  - URL: `/api/books/create/`
  - Method: `POST`
- **Update Book**
  - URL: `/api/books/update/<id>/`
  - Method: `PUT` / `PATCH`
- **Delete Book**
  - URL: `/api/books/delete/<id>/`
  - Method: `DELETE`
# Advanced API Project – Task 1 & 2

## 📌 Overview
This project expands the **Advanced API Project** to handle CRUD operations efficiently for `Author` and `Book` models.  

Task 2 enhances the **Book API** by adding filtering, searching, and ordering capabilities to improve usability.

---
## 👤 Author Endpoints

- **ViewSet** based; supports all CRUD operations in a single class.

| Method | Endpoint           | Description                         | Permission       |
|--------|------------------|-------------------------------------|----------------|
| GET    | /api/authors/     | List all authors                    | Any user        |
| POST   | /api/authors/     | Create a new author                 | Authenticated   |
| GET    | /api/authors/{id}/| Retrieve author by ID               | Any user        |
| PUT    | /api/authors/{id}/| Update an author                    | Authenticated   |
| PATCH  | /api/authors/{id}/| Partial update of an author         | Authenticated   |
| DELETE | /api/authors/{id}/| Delete an author                     | Authenticated   |
## 📚 Book Endpoints

- **Generic Views** used for each operation (List, Retrieve, Create, Update, Delete)
- Supports filtering, searching, and ordering on the list view.

| Method | Endpoint                 | Description                              | Permission           | Features |
|--------|-------------------------|------------------------------------------|--------------------|----------|
| GET    | /api/books/             | List all books                            | Any user            | Filtering: ?title, ?author, ?publication_year<br>Search: ?search<br>Ordering: ?ordering |
| GET    | /api/books/{id}/        | Retrieve a single book by ID             | Any user            | -        |
| POST   | /api/books/create       | Create a new book                         | Authenticated       | -        |
| PUT    | /api/books/update/{id}  | Update an existing book                   | Authent
## 🔍 Filtering, Searching, and Ordering

The **Book List API** supports advanced query options to help users find and sort books:

### Filtering
- Filter by specific fields using query parameters:
  - `?title=SomeTitle` – filter by book title
  - `?author=1` – filter by author ID
  - `?publication_year=2020` – filter by publication year

### Searching
- Search by text in book title or author name:
  - `?search=keyword`

### Ordering
- Order results by any field (especially title and publication_year):
  - `?ordering=title` – ascending by title
  - `?ordering=-publication_year` – descending by publication year
## 👤 Author Endpoints

- **List and Create Authors**  
  Endpoint: `GET /api/authors/`  
  Endpoint: `POST /api/authors/`  
  - Uses `AuthorViewSet` with full CRUD support
  - Permissions: Anyone can view, only authenticated users can create/update/delete

- **Retrieve, Update, Delete Author**  
  Endpoint: `GET /api/authors/{id}/`  
  Endpoint: `PUT /api/authors/{id}/`  
  Endpoint: `PATCH /api/authors/{id}/`  
  Endpoint: `DELETE /api/authors/{id}/`  
  - Access individual author by ID
## 📚 Book Endpoints

- **List Books**  
  Endpoint: `GET /api/books/`  
  - Supports filtering: `?title=xxx`, `?author=1`, `?publication_year=2020`  
  - Supports search: `?search=keyword` (searches title and author name)  
  - Supports ordering: `?ordering=title` or `?ordering=-publication_year`  
  - Permissions: Anyone can view  

- **Retrieve Book**  
  Endpoint: `GET /api/books/{id}/`  
  - Permissions: Anyone can view  

- **Create Book**  
  Endpoint: `POST /api/books/create`  
  - Permissions: Authenticated users only  

- **Update Book**  
  Endpoint: `PUT /api/books/update/{id}/`  
  Endpoint: `PATCH /api/books/update/{id}/`  
  - Permissions: Authenticated users only  

- **Delete Book**  
  Endpoint: `DELETE /api/books/delete/{id}/`  
  - Permissions: Authenticated users only
## 🔍 Filtering, Searching, and Ordering Examples

### Filtering
- By title: `/api/books/?title=things fall apart`
- By author ID: `/api/books/?author=1`
- By publication year: `/api/books/?publication_year=1958`

### Searching
- Search by keyword in title or author name: `/api/books/?search=things`

### Ordering
- Order by title ascending: `/api/books/?ordering=title`
- Order by publication year descending: `/api/books/?ordering=-publication_year`
## 👩‍💼 Author Endpoints

- List all authors (GET): `/api/authors/`
- Retrieve a single author by ID (GET): `/api/authors/<id>/`
- Create a new author (POST): `/api/authors/`
- Update an existing author (PUT/PATCH): `/api/authors/<id>/`
- Delete an author (DELETE): `/api/authors/<id>/`
## 📚 Book Endpoints

- List all books (GET) with filtering, searching, and ordering: `/api/books/`
  - Filtering: `?title=xxx`, `?author=1`, `?publication_year=2020`
  - Search: `?search=keyword` (searches title and author's name)
  - Ordering: `?ordering=title` or `?ordering=-publication_year`

- Retrieve a single book by ID (GET): `/api/books/<id>/`
- Create a new book (POST): `/api/books/create/`
- Update an existing book (PUT/PATCH): `/api/books/update/<id>/`
- Delete a book (DELETE): `/api/books/delete/<id>/`
## ⚡ Usage Examples

### Filtering
- Get books with title "Things Fall Apart":  
  `GET /api/books/?title=Things Fall Apart`

- Get books by author ID 1:  
  `GET /api/books/?author=1`

- Get books published in 1958:  
  `GET /api/books/?publication_year=1958`

### Searching
- Search books with keyword "things":  
  `GET /api/books/?search=things`

### Ordering
- Order books by title ascending:  
  `GET /api/books/?ordering=title`

- Order books by publication year descending:  
  `GET /api/books/?ordering=-publication_year`
## 📝 Notes / Permissions

- **Permissions**:
  - `BookListView` and `BookDetailView` are publicly accessible (read-only).
  - `BookCreateView`, `BookUpdateView`, and `BookDeleteView` require authentication.
- Filtering, searching, and ordering are implemented on the `BookListView`.
- Author endpoints are managed via a `ViewSet` with full CRUD capabilities.
## ⚙️ Setup Instructions

1. **Clone the repository**:  
```bash
git clone <your-repo-url>
cd advanced-api-project
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

