### Task Description

**Exercise 1: Analyzing and Mapping Word Frequencies from a Text File**  
*Subject: Arrays, Difficulty: Medium, Skills: Loops*

### Objective:
Explore real-world data processing by reading a text file and using a `HashMap` to store and analyze word frequencies. This exercise will build on your ability to navigate Java documentation, perform file I/O, and utilize collections effectively.

### Task:
Write a Java program that reads a given text file and computes the frequency of each word, storing these frequencies in a `HashMap`. The program should then display the top 5 most frequently occurring words along with their counts.

### Steps:

1. **Read Java Documentation:**
   - Begin by familiarizing yourself with the Java documentation for `FileReader`, `BufferedReader`, and `HashMap`. Focus on understanding the examples provided for each class.
   - Identify additional resources or community forums that may provide useful tips on handling file I/O and `HashMap` usage in Java.

2. **Setup File Reading:**
   - Set up a path to your text file. The file can contain any sample text such as a short story or article.
   - Use `FileReader` and `BufferedReader` to read the text file efficiently. Make sure to handle exceptions using try-with-resources for effective resource management.

3. **Parse and Process Data:**
   - Read each line from the file and split it into words using a space delimiter. Consider removing punctuation to ensure accurate word counting.
   - Initialize a `HashMap<String, Integer>` to store each word as a key and its frequency as a value.

4. **Populate the HashMap:**
   - Loop through the array of words obtained from splitting each line. For each word, update its frequency in the `HashMap`.
     - If the word is already in the map, increment its count.
     - If not, add it to the map with a count of 1.

5. **Analyze and Display Results:**
   - Once the file reading and processing is complete, iterate over the `HashMap` to determine the top 5 most frequently occurring words.
   - Display these words and their counts to the console in a formatted manner.

### Additional Challenge:
- Implement a basic hash function explanation within your code comments to demonstrate understanding of hash functions and potential collision issues.
- Consider the efficiency of your implementation when handling large text files.

### Example Code Structure:

```java
import java.io.*;
import java.util.*;

public class WordFrequencyAnalyzer {

    public static void main(String[] args) {
        String filePath = "path/to/your/textfile.txt";
        
        // Step 1: Initialize the HashMap
        Map<String, Integer> wordCountMap = new HashMap<>();

        // Step 2: Perform file reading and processing
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // Split line into words
                String[] words = line.toLowerCase().replaceAll("[^a-zA-Z ]", "").split("\\s+");
                
                // Populate the HashMap
                for (String word : words) {
                    if (word.isEmpty()) continue;
                    wordCountMap.put(word, wordCountMap.getOrDefault(word, 0) + 1);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Step 3: Analyze and display results
        List<Map.Entry<String, Integer>> sortedEntries = new ArrayList<>(wordCountMap.entrySet());
        sortedEntries.sort((e1, e2) -> e2.getValue().compareTo(e1.getValue()));

        System.out.println("Top 5 most frequent words:");
        for (int i = 0; i < Math.min(5, sortedEntries.size()); i++) {
            Map.Entry<String, Integer> entry = sortedEntries.get(i);
            System.out.printf("%s: %d\n", entry.getKey(), entry.getValue());
        }
    }
}
```

### Key Learning Outcomes:
- Efficiently navigate and utilize Java documentation.
- Understand and implement file reading using `BufferedReader`.
- Skillfully manipulate data with `HashMap` for real-world applications.
- Enhance critical thinking and problem-solving skills through a moderately complex algorithm.