import os
import sys
import openai

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
        skills = ", ".join(parts[1:]).strip() if len(parts) > 1 else "None"
        return difficulty, skills
    return None, None

def generate_task_description(api_key, subject, number_of_exercises, language, *exercise_details):
    if not api_key:
        print("Error: OpenAI API key is missing.")
        sys.exit(1)

    openai.api_key = api_key

    # Prepare messages for each exercise
    exercise_details_formatted = []
    for i, details in enumerate(exercise_details):
        difficulty, skills = parse_exercise_details(details)
        if difficulty and skills:
            exercise_details_formatted.append(f"Exercise {i+1}: Difficulty: {difficulty}, Skills: {skills}")

    if not exercise_details_formatted:
        print("No valid exercises were provided.")
        sys.exit(1)

    messages = [
        {
            "role": "system",
            "content": (
                "You are an experienced programming instructor creating a challenging task. "
                "You will generate multiple exercises that progressively increase in difficulty, "
                "based on the given specifications for each."
            )
        },
        {
            "role": "user",
            "content": f"Create {number_of_exercises} exercises for a task on the subject '{subject}' in {language}. "
                       "Here are the details for each exercise:\n\n" +
                       "\n".join(exercise_details_formatted)
        }
    ]

    task_description = generate_with_retries(openai, messages)
    if not task_description:
        print("Failed to generate task description.")
        sys.exit(1)

    # Write the task description to a markdown file
    with open("tasks/new_task.md", "w") as f:
        f.write(f"# {subject} Task\n\n")
        f.write(task_description)

    print("Task description generated successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: exercise_description.py <api_key> <subject> <number_of_exercises> <language> <exercise_1_details> [<exercise_2_details> ...]")
        sys.exit(1)

    api_key = sys.argv[1]
    subject = sys.argv[2]
    number_of_exercises = sys.argv[3]
    language = sys.argv[4]
    exercise_details = sys.argv[5:]

    generate_task_description(api_key, subject, number_of_exercises, language, *exercise_details)
