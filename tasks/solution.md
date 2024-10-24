# Solution

Below is a solution for the given task, implementing a small inventory system for a bookstore using Java and HashMaps. The solution is comprehensive, covering the requirements such as creating a `Book` class, implementing the inventory management features, providing a command-line interface for user interaction, and ensuring input validation and exception handling. Additionally, it includes test cases.

### `Book` Class Implementation:

```java
public class Book {
    private String title;
    private String author;
    private String ISBN;
    private double price;

    // Constructor
    public Book(String title, String author, String ISBN, double price) {
        this.title = title;
        this.author = author;
        this.ISBN = ISBN;
        this.price = price;
    }

    // Getters and Setters
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getAuthor() { return author; }
    public void setAuthor(String author) { this.author = author; }

    public String getISBN() { return ISBN; }
    public void setISBN(String ISBN) { this.ISBN = ISBN; }

    public double getPrice() { return price; }
    public void setPrice(double price) { this.price = price; }

    @Override
    public String toString() {
        return "Book [Title=" + title + ", Author=" + author + ", ISBN=" + ISBN + ", Price=" + price + "]";
    }
}
```

### Inventory Management System:

```java
import java.util.*;

public class BookstoreInventory {
    private Map<String, Book> inventory;

    // Constructor
    public BookstoreInventory() {
        this.inventory = new HashMap<>();
    }

    // Add a Book
    public void addBook(Book book) {
        if (inventory.containsKey(book.getISBN())) {
            System.out.println("A book with this ISBN already exists.");
        } else {
            inventory.put(book.getISBN(), book);
            System.out.println("Book added successfully.");
        }
    }

    // Remove a Book
    public void removeBook(String ISBN) {
        if (inventory.remove(ISBN) != null) {
            System.out.println("Book removed successfully.");
        } else {
            System.out.println("No book found with the provided ISBN.");
        }
    }

    // Update Book Details
    public void updateBook(String ISBN, Book updatedBook) {
        if (inventory.containsKey(ISBN)) {
            inventory.put(ISBN, updatedBook);
            System.out.println("Book updated successfully.");
        } else {
            System.out.println("No book found with the provided ISBN.");
        }
    }

    // Search Books by Title
    public List<Book> searchBooksByTitle(String title) {
        List<Book> books = new ArrayList<>();
        for (Book book : inventory.values()) {
            if (book.getTitle().equalsIgnoreCase(title)) {
                books.add(book);
            }
        }
        return books;
    }

    // Display All Books
    public void displayAllBooks() {
        if (inventory.isEmpty()) {
            System.out.println("No books in inventory.");
        } else {
            for (Book book : inventory.values()) {
                System.out.println(book);
            }
        }
    }
}
```

### User Interaction:

```java
import java.util.*;

public class BookstoreApp {

    public static void main(String[] args) {
        BookstoreInventory inventory = new BookstoreInventory();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nBookstore Inventory Management:");
            System.out.println("1. Add a book");
            System.out.println("2. Remove a book");
            System.out.println("3. Update book details");
            System.out.println("4. Search for books by title");
            System.out.println("5. Display all books");
            System.out.println("6. Exit");

            System.out.print("Choose an option: ");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    addBook(scanner, inventory);
                    break;
                case "2":
                    removeBook(scanner, inventory);
                    break;
                case "3":
                    updateBook(scanner, inventory);
                    break;
                case "4":
                    searchBooks(scanner, inventory);
                    break;
                case "5":
                    inventory.displayAllBooks();
                    break;
                case "6":
                    System.out.println("Exiting... Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please choose a number between 1 and 6.");
            }
        }
    }

    private static void addBook(Scanner scanner, BookstoreInventory inventory) {
        System.out.print("Enter book title: ");
        String title = scanner.nextLine();
        System.out.print("Enter book author: ");
        String author = scanner.nextLine();
        System.out.print("Enter book ISBN: ");
        String ISBN = scanner.nextLine();
        System.out.print("Enter book price: ");
        double price = getValidPrice(scanner);
        Book book = new Book(title, author, ISBN, price);
        inventory.addBook(book);
    }

    private static void removeBook(Scanner scanner, BookstoreInventory inventory) {
        System.out.print("Enter the ISBN of the book to remove: ");
        String ISBN = scanner.nextLine();
        inventory.removeBook(ISBN);
    }

    private static void updateBook(Scanner scanner, BookstoreInventory inventory) {
        System.out.print("Enter the ISBN of the book to update: ");
        String ISBN = scanner.nextLine();
        if (!inventory.inventory.containsKey(ISBN)) {
            System.out.println("No book found with the provided ISBN.");
            return;
        }
        System.out.print("Enter new book title: ");
        String title = scanner.nextLine();
        System.out.print("Enter new book author: ");
        String author = scanner.nextLine();
        System.out.print("Enter new book price: ");
        double price = getValidPrice(scanner);
        Book updatedBook = new Book(title, author, ISBN, price);
        inventory.updateBook(ISBN, updatedBook);
    }

    private static void searchBooks(Scanner scanner, BookstoreInventory inventory) {
        System.out.print("Enter the title of the book to search: ");
        String title = scanner.nextLine();
        List<Book> books = inventory.searchBooksByTitle(title);
        if (books.isEmpty()) {
            System.out.println("No books found with the given title.");
        } else {
            for (Book book : books) {
                System.out.println(book);
            }
        }
    }

    private static double getValidPrice(Scanner scanner) {
        double price;
        while (true) {
            try {
                price = Double.parseDouble(scanner.nextLine());
                if (price < 0) {
                    throw new IllegalArgumentException();
                }
                return price;
            } catch (NumberFormatException | IllegalArgumentException e) {
                System.out.print("Invalid price. Please enter a non-negative number: ");
            }
        }
    }
}
```

### Test Cases Document:

#### Test Case 1: Adding, Removing, and Updating
- **Input:** Add a book with ISBN `1234567890`, remove it, then attempt to update it.
- **Expected Outcome:** Book is successfully added and removed, "No book found" message appears during update attempt.

#### Test Case 2: Search Books by Title
- **Input:** Add two books with the same title, search by title.
- **Expected Outcome:** List of books with that title is returned.

#### Test Case 3: Display All Books
- **Input:** Add multiple books, display all.
- **Expected Outcome:** All books are displayed in a list.

#### Test Case 4: Invalid Inputs
- **Input:** Enter non-numeric price, enter negative price.
- **Expected Outcome:** Appropriate error messages are displayed.

### README:

**Compiling and Running the Application**

To compile the application, navigate to the folder containing your `.java` files and execute:

```bash
javac Book.java BookstoreInventory.java BookstoreApp.java
```

To run the application:

```bash
java BookstoreApp
```

**Assumptions:**
- Each book has a unique ISBN.
- The application runs in a console environment.

**Limitations:**
- The ISBN is assumed to be a valid string (not validated for length or characters).

This setup provides a fully functional bookstore inventory management system using HashMaps in Java, complete with user input handling and exception mechanisms.