import os
import re
import sys
import json
import mysql.connector
from dotenv import load_dotenv
from groq import Groq
import datetime

# Load environment variables
load_dotenv()

# Define directories
GENERATED_FILES_DIR = "generated_files"
SELENIUM_FILES_DIR = os.path.join(GENERATED_FILES_DIR, "selenium")

# Ensure directories exist
os.makedirs(GENERATED_FILES_DIR, exist_ok=True)
os.makedirs(SELENIUM_FILES_DIR, exist_ok=True)

def remove_ansi_escape_sequences(text):
    """Remove ANSI escape sequences from text."""
    ansi_escape = re.compile(r'(?:\x1B[@-Z\\]|]|\x1B\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def fetch_data_from_db(module_id, language):
    """Fetch module data from the database and send it for code & Selenium script generation."""
    try:
        conn = mysql.connector.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST")
        )
        cursor = conn.cursor()

        query = "SELECT * FROM AIA_MODULE WHERE module_id = %s;"
        cursor.execute(query, (module_id,))
        module_data = cursor.fetchall()

        if not module_data:
            print(f"Error: No data found for module_id {module_id}.")
            return

        generated_project_code = send_to_groq("Module Details", module_data, module_id, language)
        
        selenium_script_path = generate_selenium_script(generated_project_code, module_id)
        
        print(f"Selenium script generated: {selenium_script_path}")

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        cursor.close()
        conn.close()

def send_to_groq(context, data, module_id, language):
    """Send module data to GroqCloud API and generate code dynamically."""
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        message_content = f"{context}: Generate a {language.upper()} code based on the following data: {data}"

        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": message_content}],
            model="llama-3.3-70b-versatile",
        )

        generated_code = remove_ansi_escape_sequences(chat_completion.choices[0].message.content)
        print("Generated Code:\n", generated_code)

        # Save generated code with timestamp
        extension = {"php": "php", "java": "java", "django": "py"}.get(language, "txt")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(GENERATED_FILES_DIR, f"generated_module_{module_id}_{timestamp}.{extension}")

        with open(filename, "w", encoding="utf-8") as file:
            file.write(generated_code)

        print(f"Code saved: {filename}")
        return generated_code

    except Exception as e:
        print(f"Error generating code: {e}")
        return None

def generate_selenium_script(generated_project_code, module_id):
    """Generate a Selenium test script for the generated project."""
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        selenium_request = f"Generate a Selenium test script to validate the functionality of the generated project: {generated_project_code}"

        selenium_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": selenium_request}],
            model="llama-3.3-70b-versatile",
        )

        selenium_script = remove_ansi_escape_sequences(selenium_completion.choices[0].message.content)
        print("Generated Selenium Test Script:\n", selenium_script)

        # Save the Selenium test script with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        selenium_filename = os.path.join(SELENIUM_FILES_DIR, f"selenium_test_{module_id}_{timestamp}.py")

        with open(selenium_filename, "w", encoding="utf-8") as file:
            file.write(selenium_script)

        print(f"Selenium test script saved: {selenium_filename}")
        return selenium_filename  # Return the filename for external use

    except Exception as e:
        print(f"Error generating Selenium script: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Module ID and language are required.")
        sys.exit(1)

    module_id = sys.argv[1]
    language = sys.argv[2].lower()  # Ensure lowercase for consistency
    fetch_data_from_db(module_id, language)
