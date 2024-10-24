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

def generate_task_description(api_key, subject, difficulty, language):
    if not api_key:
        print("Error: OpenAI API key is missing.")
        sys.exit(1)

    openai.api_key = api_key

    # Create messages for chat model
    messages = [
        {
            "role": "system",
            "content": (
                "You are an experienced programming instructor creating challenging tasks for university-level students. "
                "The task should be pedagogically valuable and detailed."
            )
        },
        {
            "role": "user",
            "content": f"Create a task in {language} with the subject '{subject}' and a difficulty level of {difficulty}."
        }
    ]

    # Generate task description with retries
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
    if len(sys.argv) != 5:
        print("Usage: exercise_description.py <api_key> <subject> <difficulty> <language>")
        sys.exit(1)

    api_key = sys.argv[1]
    subject = sys.argv[2]
    difficulty = sys.argv[3]
    language = sys.argv[4]

    generate_task_description(api_key, subject, difficulty, language)
