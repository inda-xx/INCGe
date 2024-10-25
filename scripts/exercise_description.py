import os
import sys
import openai

learning_goals = """
* Using Documentation
* Reading from a Text File
* Using the HashMap Class

    {
        "main_point": "Using Documentation",
        "sub_points": [
            "Description: This concept emphasizes the importance of using documentation to understand and implement Java classes and libraries effectively. Mastery of documentation is crucial for solving programming problems and enhancing code quality.",
            "Subpoint 1: Navigating official Java documentation and API references.",
            "Subpoint 2: Understanding code examples and integrating them into projects.",
            "Subpoint 3: Leveraging community resources and forums for additional insights."
        ]
    },
    {
        "main_point": "Reading from a Text File",
        "sub_points": [
            "Description: This concept introduces file I/O operations in Java, focusing on reading data from text files. Understanding file reading is essential for applications that require data persistence and external data processing.",
            "Subpoint 1: Setting up file paths and understanding file streams.",
            "Subpoint 2: Using classes like FileReader and BufferedReader for efficient file reading.",
            "Subpoint 3: Handling exceptions and ensuring resource management with try-with-resources."
        ]
    },
    {
        "main_point": "Using the HashMap Class",
        "sub_points": [
            "Description: This concept explores the HashMap class, a powerful collection for storing key-value pairs. Mastery of HashMap is important for efficient data retrieval and manipulation in Java applications.",
            "Subpoint 1: Creating and initializing a HashMap with generic types.",
            "Subpoint 2: Performing operations such as adding, removing, and accessing key-value pairs.",
            "Subpoint 3: Understanding hash functions and handling collisions for optimal performance."
        ]
    }
"""

def generate_with_retries(client, messages, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-2024-08-06",
                messages=messages
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating task description: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
    return None

def parse_exercise_details(details):
    if details:
        parts = details.split(",")
        difficulty = parts[0].strip()
        skills = parts[1].strip() if len(parts) > 1 else "None"
        subject = parts[2].strip() if len(parts) > 2 else "No subject provided"
        return difficulty, skills, subject
    return None, None, None

def generate_task_description(api_key, number_of_exercises, language, programming_language, *exercise_details):
    if not api_key:
        print("Error: OpenAI API key is missing.")
        sys.exit(1)

    openai.api_key = api_key

    # Prepare modular prompts for each exercise considering difficulty level, language, and skill maps
    exercise_details_formatted = []
    for i, details in enumerate(exercise_details):
        difficulty, skills, subject = parse_exercise_details(details)
        if difficulty and skills and subject:
            prompt_section = f"Exercise {i+1}: Subject: {subject}, Difficulty: {difficulty}, Skills: {skills}\n\n"
            if difficulty == "simple":
                prompt_section += (
                    "Focus on introductory concepts for beginners using basic applications of the skills. "
                    "Encourage understanding of foundational concepts in programming, especially for language: {programming_language}.\n"
                )
            elif difficulty == "medium":
                prompt_section += (
                    "This exercise should push students to apply their skills in moderately challenging scenarios. "
                    "Include tasks that involve real-world applications, encouraging problem-solving in {programming_language}.\n"
                )
            elif difficulty == "hard":
                prompt_section += (
                    "Challenge students to solve complex problems that require deeper knowledge of the specified skills. "
                    "The tasks should simulate industry-level complexity, especially suited for {programming_language} applications.\n"
                )
            elif difficulty == "v.hard":
                prompt_section += (
                    "The exercise should be highly challenging, combining multiple skills to solve complex, multi-step problems. "
                    "Designed for advanced students, it should demand a deep understanding of {programming_language} in practical applications.\n"
                )

            exercise_details_formatted.append(prompt_section)

    if not exercise_details_formatted:
        print("No valid exercises were provided.")
        sys.exit(1)

    # Modular prompt that integrates the learning goals and skill maps
    messages = [
        {
            "role": "system",
            "content": (
                "You are an experienced programming instructor creating a set of exercises for a university-level programming lab. "
                "These exercises should be challenging, pedagogically valuable, and focused on skill development in the specified programming language."
            )
        },
        {
            "role": "user",
            "content": f"Create {number_of_exercises} exercises in {programming_language} that align with these learning goals:\n\n{learning_goals}\n\n"
                       "Each exercise should follow the provided details:\n\n" +
                       "\n".join(exercise_details_formatted) +
                       "\n\nDesign these exercises to be challenging and to encourage the students to apply critical thinking and problem-solving skills."
        }
    ]

    task_description = generate_with_retries(openai, messages)
    if not task_description:
        print("Failed to generate task description.")
        sys.exit(1)

    # Write the task description to a markdown file
    with open("tasks/new_task.md", "w") as f:
        f.write(f"### Task Description\n\n")
        f.write(task_description)

    print("Task description generated successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: exercise_description.py <api_key> <number_of_exercises> <language> <programming_language> <exercise_1_details> [<exercise_2_details> ...]")
        sys.exit(1)

    api_key = sys.argv[1]
    number_of_exercises = sys.argv[2]
    language = sys.argv[3]
    programming_language = sys.argv[4]
    exercise_details = sys.argv[5:]

    generate_task_description(api_key, number_of_exercises, language, programming_language, *exercise_details)
