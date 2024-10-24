# How to count words in Java

Say you are a scholar, curious to find out the number of times a word occurs
in a text, maybe Shakespeare's _Hamlet_ for instance. In the old days, you would have
to do it by hand, using pen and paper. Fortunately, we now have computers to do this tedious work.
Your assignment this week will be to create a program that can perform
such a task.


### ✅ Learning Goals

This week's learning goals include:

- Using documentation
- Reading from a text file
- Using the `HashMap` class

We encourage you to discuss with your course friends, **but do not share answers!** Similarily, use of any AI services 🤖 are great to help explain things, **but please do not submit AI-generated solutions** - you must be both responsible for your own solutions and must be able to explain them under examination.

### 🏛 Assignment

#### Exercise 7.0 -- Reading words from a file

We will begin by creating a class for reading text from 
a file and splitting it into separate words. In your [`src`](src)
folder, create a file containing a class called `FileWordSplitter`.
Add a `private` field to your class of type `ArrayList<String>` called
`words`. 

Now add a constructor to your class with the following header:

```java
public FileWordSplitter(String filename)
```

The constructor should read the file with the given filename and 
add all the words in the file to the `words` `ArrayList`. You can find a guide 
to reading a file with Java below.

When you read from a file with `nextLine` you get a `String` that will be 
a whole _line_ of the text. You will need to split this up into individual
words. Look in the documentation for the [String class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),
and see if you can find a method for splitting a `String` into smaller strings.
For each line, add the words from the line to the `words` `ArrayList`.
In order to make this exercise slightly easier, we have provided a sample file [`hamlet.txt`](src/hamlet.txt)
where all punctuation marks have been removed, and we have made sure that all words are separated by exactly
one space character (` `).

<details>
    <summary> 🛠 Reading a file line by line</summary>

```java
try {
    // Attempt to open a text file
    BufferedReader file = new BufferedReader(new FileReader("my_file.txt"));
    
    // Try to read the first line of the file
    String line = file.readLine();
    
    // Keep reading while there are lines left
    while (line != null){
        // TODO: Add some code here to do something with the line
        
        line = file.readLine();
    }

    // Don't forget to close the file!
    file.close();
// Handle any errors that come up, such as the file not existing
} catch (IOException e) {
    System.out.println("Something went wrong: " + e.getMessage());
    // Exit the program    
    System.exit(1);     
}
```

In this example, we simply shut down the program if something goes 
wrong. In actual "real world" code, 
it is more common to have some form of a fallback solution, such as
prompting the user to select a different file if the file was not
found.

Remember that you need to _import_ all classes that you want to use
(such as `BufferedReader`).
</details>

<details>
    <summary> 📚 A brief note on regex </summary>

In the documentation for [`String`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) 
class, you might find methods that requires a _Regular Expression_ (or _regex_).

You will get familiar with these kinds of expressions as you progress in your studies. For now, you can think of them as search patterns.
Oracle has an [official tutorial](https://docs.oracle.com/javase/tutorial/essential/regex/intro.html) on Java and regex, but it is fairly advanced. 
If you get stuck, follow the steps in the 🚨 **Troubleshooting Guide**.
</details>

#### Exercise 7.1 -- Getting the words

Add a _getter_ to `FileWordSplitter` that returns the `words` that you read from the file.

Now is a good time to check so that your class works as intended.
In the [`src`](src) folder you have been provided a file called [`hamlet.txt`](src/hamlet.txt).
This file contains the text from Shakespeare's _Hamlet_ (without punctuation). If you run the following code
(in a main method or using JShell) you should see that the fourth word
of the text is indeed `"Hamlet"`:

```java
FileWordSplitter splitter = new FileWordSplitter("hamlet.txt");
ArrayList<String> hamletWords = splitter.getWords();
System.out.println(hamletWords.get(3)); // Get the fourth word in hamlet.txt
```

#### Exercise 7.2 -- Textual analysis

Now it's time to create a class for analyzing the text and see if we can glean any insights.
Start by creating a new Java class called
`FileTextAnalyzer` in the [`src`](src) directory. Add a `private` field called 
`words` of type `FileWordSplitter` to your class, and add a constructor
with the following header:

```java
public FileTextAnalyzer(String filename)
```

The constructor should create a new `FileWordSplitter` object using the given file 
and save it in the `words` field.

#### Exercise 7.3 -- Counting words

Let's start with simply counting the number of words in the text. Create a new method with the header:

```java
public int wordCount()
```

This method should simply return the number of words in the file. 

<details>
    <summary> 📚 The Unix word count explained (and how the check your solution) </summary>

On Linux and MacOS you have the command line program `wc` (Word Count). 
If you open up your terminal, and type `man wc` (short for *manual wordcount*), you will find the manual for 
your system's integrated word count program (press *q* to end the manual).
You can use it to check so that your code works as intended. Run the following example in the terminal (in the [`src`](src) folder):

```bash
wc -w hamlet.txt
```

you should get the output:

```bash
30720 hamlet.txt
```

telling you that the file contains 30720 words. You can use this to make sure that your `wordCount` method works correctly.
</details>

#### Exercise 7.4 -- Counting different words using a `HashMap`

Let's move on to counting the number of times different words occur in the text.
For this, we will be using a data structure called a `HashMap` in Java (you might also find the 
same data structure called "dictionary" or "associative array" or something similar in other programming languages).
You can find a brief summary of how to work with `HashMaps` below.

Add a field called `wordOccurrences` to your `FileTextAnalyzer` class. This field should be a `HashMap` that associate
Strings with Integers. Add code in your constructor for iterating over every word in the file and counting the
number of times words occur. To test your implementation, you may also want to add a *getter* (`getwordOccurrences`). You don't have to make the keys case insensitive at the moment.

<details>
    <summary>📚 The HashMap class</summary>

The [`HashMap`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html) stores a `key` and an associated `value`. The type of the key and the value can be any Java class (but not primitive types) and therefore the class is _parameterized_ by two types. You can create a `HashMap` that has `String` keys and `Integer` 
values as:

```java
HashMap<String, Integer> myHashMap = new HashMap<>();
```

Note the similarity to creating an `ArrayList`, only with two class names instead of one.

You can _associate_ a value with a key using the `put` method. For instance

```java
myHashMap.put("Hello", 1337);
```

will link the key `"Hello"` to the value `1337`. It's important to remember that the key _must_ be unique, but there
can be several of the same value. For instance, it is not possible to have a `HashMap` where you have two keys with the
value `"Hello"`.

You can _get_ the value associated with a key using the `get` method:

```java
// Will store the value '1337' in the variable 'valueOfHello'
int valueOfHello = myHashMap.get("Hello"); 
```

A `HashMap` can be seen as a function (in the mathematical sense) taking one input (the key) and giving
one output (the value). Another term for a function sometimes used in mathematics is a 
[map](https://en.wikipedia.org/wiki/Map_(mathematics)), which explains the somewhat strange name of the `HashMap`
(we'll get to the "hash" part later in the course).

A common thing you want to do with a `HashMap` is to update the value of some key, for instance, adding a
word to the count, or changing the value associated with `"Hello"` to `1338`. This can be done using a combination
of `get` and `put`:

```java
int oldValue = myHashMap.get("hello");
myHashMap.put("Hello", oldValue + 1);
```

Since this is something you want to do often, there is a special method in `HashMap` called `merge`, that
allows you to take a value and _merge_ it with another value. The code above could also be written

```java
myHashMap.merge("Hello", 1, Integer::sum);
```

This will take the old value associated with `"Hello"` and merge it with `1` using the `sum` method from the `Integer`
class. Simply put, it will associate `oldValue + 1` with `"Hello"`. Don't worry if this seems a bit weird and abstract
right now, for this task you can simply use the code given above. If you would like an in-depth explanation of the latter example, we encourage you to ask a TA!
</details>

<details>
    <summary> 🛠 Pseudocode </summary>

We are going to give you so-called [*pseudocode*](https://en.wikipedia.org/wiki/Pseudocode)
describing how to count word occurrences.
Pseudocode serves as a template for your code but is not written in any actual programming language.
You will surely come across more examples like this as you progress in your studies, 
and being able to read and formulate pseudocode is a skill every programmer should have.

```
words := all words in hamlet.txt
map := empty hashmap
∀ word ∈ words:
    if word ∉ map
        put word in map with count 1
    else 
        increment count for word by 1
```

In this example, we use mathematical notation. Here is an explanation of the symbols:

* `:=` a new definition
* `∀` *for all*
* `∈` *in* 
* `∉` *not in*

There are no fixed standards for how to write pseudocode, so you will probably
see many different styles being used. In general, pseudocode tends to be more abstract
and "_high level_" than actual running program code.
</details>

#### Exercise 7.5 -- Capitalization matters (and `occurrencesOf`)!

One important thing to remember is that _capitalization matters_. Java considers 
`"Hello"` and `"hello"` to be two completely different strings, even though they contain the same English word.
Of course, if we have the text `"Hello hello my friends"`, we want to make sure that we count two occurrences 
of `"hello"`. The [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)
class contains a method for converting all letters to lowercase. Make sure to apply this method to every word 
that you use as a key in your `HashMap`, this way `"Hello"` and `"hello"` will count as the same word.

Add a method with the header: 

```java
public int occurrencesOf(String word) 
```

This should simply return the number of times a word occurs in the file. 
If you use the [`hamlet.txt`](src/hamlet.txt) file you should be able to see that the word `"Hamlet"`
occurs 92 times. This method should also be _case-insensitive_, so make sure that you get the same result
for the string `"hamlet"`. Make sure that you return `0` for words that are not present in the file. 

#### Exercise 7.6 -- Word frequencies

Add a method with the header

```java
public double frequencyOf(String word)
```

that returns the proportion of the text that consists of that word. As an example, since the file 
[`hamlet.txt`](src/hamlet.txt) contains 92 occurrences of `"Hamlet"` and 30720 words in total.
`frequencyOf("Hamlet")` should return `0.002994791666666667` (_92 / 30720_). Once again, this method should
be _case-insensitive_ and return `0` if a word that is not in the text is used as an argument.

<details> 
    <summary> 📚 Type conversion </summary>

You might find yourself with the error: `Type mismatch: cannot convert from int to double`.
The problem here is that we want the result as a double, but we
divide two whole numbers. As a default, Java will perform _integer division_, so that _5 / 2_ gives the value _2_
instead of _2.5_. In order to solve this you will need to use [_type conversion_](https://en.wikipedia.org/wiki/Type_conversion)
(sometimes called _casting_) to convert an `int` to a `double`. In Java, this is done by putting a type name in
parenthesis in front of the value you want to convert, such as 
```java
int fiveAsAnInt = 5;
double fiveAsADouble = (double) fiveAsAnInt;
```
</details>

#### Exercise 7.7 -- Unique words

As a final part of our `FileTextAnalyzer` class, let's calculate the number of _unique_ words in a file.
Create a method with the header:

```java
public int uniqueWordCount()
```

Here we can use the special property of `HashMap`, which is that the keys have to be unique. There is also a special method
in the `HashMap` class for getting all the keys. Read the 
[documentation](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html)
and use this method in your code. You should find that _Hamlet_ contains 4810 unique words.

### ❎ Checklist 

- [ ] Create class `FileWordSplitter`.
  - [ ] Add private field `words`. 
  - [ ] Add constructor using `public FileWordSplitter(String filename)`. Make the constructor read all words in a given file and add them to `words`.
  - [ ] Add a getter that returns `words`.
- [ ] Create class `FileTextAnalyzer`.
  - [ ] Add private field `words` of type `FileWordSplitter`.
  - [ ] Add a constructor `public FileTextAnalyzer(String filename)`. Make it assign a new `FileWordSplitter` to `words`.
  - [ ] Add a method `public int wordCount()` to count the number of words in a file. 
  - [ ] Add a field called `wordOccurrences` of type `HashMap` that associate Strings with Integers.
  - [ ] In the constructor, add all words in the file as keys to `wordOccurrences` and set the corresponding value to the number of occurrences.
  - [ ] Add a getter for `wordOccurrences` called `getwordOccurrences`.
  - [ ] Make your code case insensitive, meaning it should not matter if a word is capitalized or not. 
  - [ ] Add a method to count the number of occurrences of a specific word using method `public int occurrencesOf(String word)`. Make it case insensitive.
  - [ ] Add a method `public double frequencyOf(String word)` to print out the frequency of a specific word.
  - [ ] Add a method `public int uniqueWordCount()` that prints the total number of unique words in a file. 
