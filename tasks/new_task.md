# Hashmaps and other stuff Task

**Task: Implementing a Small Application Using HashMaps**

**Objective:**  
The goal of this task is to help you gain a better understanding of HashMaps in Java by applying them to a practical situation. You will design and implement a small application that manages a simple inventory system for a bookstore.

**Requirements:**

1. **Create a Book Class:**
   - Implement a `Book` class with the following attributes:
     - `String title`
     - `String author`
     - `String ISBN` (International Standard Book Number)
     - `double price`
   - Implement getters and setters for all attributes.
   - Override the `toString()` method to provide a human-readable representation of a `Book`.

2. **Design the Inventory System:**
   - Use a `HashMap<String, Book>` to store the inventory, where the key is the ISBN and the value is the `Book` object.
   - Implement methods to:
     - Add a new book to the inventory.
     - Remove a book from the inventory using its ISBN.
     - Update the details of a book in the inventory.
     - Search for a book by its title and return a list of books matching this title.
     - Display all books in the inventory.

3. **User Interaction:**
   - Implement a simple text-based menu that provides the following options to the user:
     1. Add a book
     2. Remove a book
     3. Update book details
     4. Search for books by title
     5. Display all books
     6. Exit
   - Ensure the menu loops until the user chooses to exit.

4. **Input Validation:**
   - Provide input validation to ensure that books have a valid ISBN, and that prices are non-negative.
   - Handle any potential exceptions that might arise during user inputs, such as `NumberFormatException` when reading numeric values.

5. **Test Cases:**
   - Create a set of test cases to ensure the correctness of your application:
     - Test adding, removing, and updating books.
     - Test searching for a book by title.
     - Test displaying all books.

**Guidelines:**

- Make sure your code is well-documented. Use comments to explain the purpose of classes, methods, and complex logic.
- Focus on the efficiency of operations, especially considering that HashMaps have average constant-time complexity for get/put operations.
- Ensure proper exception handling and error messages that are user-friendly.

**Deliverables:**

1. Submit the complete Java source code file(s) for your bookstore inventory application.
2. Include a README file that describes how to compile and run your program, along with any assumptions or limitations.
3. Provide a document (or section in the README) with test cases and their expected outcomes.

**Evaluation Criteria:**

- Correctness: The program should meet all specified requirements and handle edge cases gracefully.
- Code quality: Your code should be clean, readable, and well-organized. Proper use of data structures and algorithms is expected.
- User Interface: Although text-based, the user interface should be intuitive and user-friendly.
- Error Handling: The program should handle erroneous input without crashing and provide meaningful feedback to the user.