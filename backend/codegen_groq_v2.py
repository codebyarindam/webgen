import os
import re
import sys
import json
import mysql.connector
from dotenv import load_dotenv
from groq import Groq
import datetime


load_dotenv()

GENERATED_FILES_DIR = "generated_files"
SELENIUM_FILES_DIR = os.path.join(GENERATED_FILES_DIR, "selenium")

# Ensure directories exist
for directory in [GENERATED_FILES_DIR, SELENIUM_FILES_DIR]:
    if not os.path.exists(directory):
        os.makedirs(directory)

def remove_ansi_escape_sequences(text):
    """Remove ANSI escape sequences from text."""
    ansi_escape = re.compile(r'(?:\x1B[@-Z\\]|]|\x1B\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def fetch_data_from_db(module_id, language):
    """Fetch selected module data from the database and send it for code generation."""
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
    
    generated_project_code = send_to_groq("Module Details", module_data, module_id, language)
    
    generate_selenium_script(generated_project_code)
    
    cursor.close()
    conn.close()

# def send_to_groq(context, data, module_id, language):
#     """Send module data to GroqCloud API and generate code dynamically based on language."""
#     client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
#     message_content = f"{context}: Generate a {language.upper()} code based on the following data: {data} and selenium script using python."
    
#     chat_completion = client.chat.completions.create(
#         messages=[{"role": "user", "content": message_content}],
#         model="llama-3.3-70b-versatile",
#     )
    
#     generated_code = remove_ansi_escape_sequences(chat_completion.choices[0].message.content)
#     print("Generated Code:\n", generated_code)
    
#     # Save the generated file with appropriate extension
#     extension = {"php": "php", "java": "java", "django": "py"}.get(language, "txt")
#     filename = os.path.join(GENERATED_FILES_DIR, f"generated_module_{module_id}.{extension}")
    
#     with open(filename, "w") as file:
#         file.write(generated_code)
#     print(f"Code saved: {filename}")
    
#     return generated_code

# def generate_selenium_script(generated_project_code):
#     """Generate a Selenium test script for the generated Django project."""
#     client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
#     selenium_request = f"Generate a Selenium test script to validate the functionality of the generated Django project: {generated_project_code}"
    
#     selenium_completion = client.chat.completions.create(
#         messages=[{"role": "user", "content": selenium_request}],
#         model="llama-3.3-70b-versatile",
#     )
    
#     selenium_script = remove_ansi_escape_sequences(selenium_completion.choices[0].message.content)
#     print("Generated Selenium Test Script:\n", selenium_script)
    
#     selenium_filename = os.path.join(SELENIUM_FILES_DIR, "selenium_test.py")
    
#     with open(selenium_filename, "w") as file:
#         file.write(selenium_script)
#     print(f"Selenium test script saved: {selenium_filename}")
    
#     # Provide download link
#     print(f"Download the Selenium test script from: file://{os.path.abspath(selenium_filename)}")



def send_to_groq(context, data, module_id, language):
    """Send module data to GroqCloud API and generate code dynamically based on language."""
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    message_content = f"{context}: Generate a {language.upper()} code based on the following data: {data} and selenium script using python."
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": message_content}],
        model="llama-3.3-70b-versatile",
    )
    
    generated_code = remove_ansi_escape_sequences(chat_completion.choices[0].message.content)
    print("Generated Code:\n", generated_code)
    
    # Save the generated file with appropriate extension and timestamp
    extension = {"php": "php", "java": "java", "django": "py"}.get(language, "txt")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(GENERATED_FILES_DIR, f"generated_module_{module_id}_{timestamp}.{extension}")
    
    with open(filename, "w") as file:
        file.write(generated_code)
    print(f"Code saved: {filename}")
    
    return generated_code

# def generate_selenium_script(generated_project_code):
#     """Generate a Selenium test script for the generated project."""
#     client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
#     selenium_request = f"Generate a Selenium test script to validate the functionality of the generated project: {generated_project_code}"
    
#     selenium_completion = client.chat.completions.create(
#         messages=[{"role": "user", "content": selenium_request}],
#         model="llama-3.3-70b-versatile",
#     )
    
#     selenium_script = remove_ansi_escape_sequences(selenium_completion.choices[0].message.content)
#     print("Generated Selenium Test Script:\n", selenium_script)
    
#     # Save the Selenium test script with timestamp
#     timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     selenium_filename = os.path.join(SELENIUM_FILES_DIR, f"selenium_test_{timestamp}.py")
    
#     with open(selenium_filename, "w") as file:
#         file.write(selenium_script)
#     print(f"Selenium test script saved: {selenium_filename}")
    
#     # Provide download link
#     print(f"Download the Selenium test script from: file://{os.path.abspath(selenium_filename)}")
def generate_selenium_script(generated_project_code, module_id):
    """Generate a Selenium test script for the generated project."""
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
    
    with open(selenium_filename, "w") as file:
        file.write(selenium_script)
    print(f"Selenium test script saved: {selenium_filename}")
    
    return selenium_filename  # Return filename to be stored or accessed later

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Module ID and language are required.")
        sys.exit(1)
    
    module_id = sys.argv[1]
    language = sys.argv[2].lower()  # Ensure lowercase for consistency
    fetch_data_from_db(module_id, language)
