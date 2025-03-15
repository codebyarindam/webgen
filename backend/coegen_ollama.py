# import os
# import re
# import mysql.connector
# from dotenv import load_dotenv  # Ensure this is installed: pip install python-dotenv
# from groq import Groq

# load_dotenv()

# def remove_ansi_escape_sequences(text):
#     """Remove ANSI escape sequences from text."""
#     ansi_escape = re.compile(r'(?:\x1B[@-Z\\]|\x1B\[[0-?]*[ -/]*[@-~])')
#     return ansi_escape.sub('', text)

# def fetch_data_from_db():
#     """Fetch module data from the database."""
#     conn = mysql.connector.connect( 
#         database=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         host=os.getenv("DB_HOST")
#     )
#     cursor = conn.cursor()
    
#     # Query to fetch modules for a specific project
#     query = "SELECT * FROM AIA_MODULE WHERE project_id = %s;"
#     project_id = 1  # Replace with actual project_id
    
#     cursor.execute(query, (project_id,))
#     module_data = cursor.fetchall()
    
#     # Process module data with GroqCloud
#     send_to_groq("Module Details", module_data)
    
#     cursor.close()
#     conn.close()

# def send_to_groq(context, data):
#     """Send project data to GroqCloud for AI processing and generate Selenium test scripts."""
#     client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
#     message_content = f"{context}: Generate a Django project based on the following data: {data}"
    
#     chat_completion = client.chat.completions.create(
#         messages=[{"role": "user", "content": message_content}],
#         model="llama-3.3-70b-versatile",
#     )
    
#     generated_project_code = remove_ansi_escape_sequences(chat_completion.choices[0].message.content)
#     print("Generated Django Project Code:\n", generated_project_code)
    
#     # Request Selenium test script generation
#     selenium_request = f"Generate a Selenium test script to validate the functionality of the generated Django project: {generated_project_code}"
    
#     selenium_completion = client.chat.completions.create(
#         messages=[{"role": "user", "content": selenium_request}],
#         model="llama-3.3-70b-versatile",
#     )
    
#     selenium_script = remove_ansi_escape_sequences(selenium_completion.choices[0].message.content)
#     print("Generated Selenium Test Script:\n", selenium_script)
    
#     with open("selenium_test.py", "w") as file:
#         file.write(selenium_script)
#     print("Selenium test script saved: selenium_test.py")

# if __name__ == "__main__":
#     fetch_data_from_db()
# import sys  # Add this to read command-line arguments
# import os
# import re
# import mysql.connector
# from dotenv import load_dotenv  # Ensure this is installed: pip install python-dotenv
# from groq import Groq

# load_dotenv()

# def remove_ansi_escape_sequences(text):
#     """Remove ANSI escape sequences from text."""
#     ansi_escape = re.compile(r'(?:\x1B[@-Z\\]|\x1B\[[0-?]*[ -/]*[@-~])')
#     return ansi_escape.sub('', text)


# def fetch_data_from_db(module_id):
#     """Fetch selected module data from the database."""
#     conn = mysql.connector.connect( 
#         database=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         host=os.getenv("DB_HOST")
#     )
#     cursor = conn.cursor()
    
#     # Query to fetch the selected module
#     query = "SELECT * FROM AIA_MODULE WHERE module_id = %s;"
    
#     cursor.execute(query, (module_id,))
#     module_data = cursor.fetchall()
    
#     send_to_groq("Selected Module Details", module_data)
    
#     cursor.close()
#     conn.close()

# def send_to_groq(context, data):
#     """Send project data to GroqCloud for AI processing and generate Selenium test scripts."""
#     client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
#     message_content = f"{context}: Generate a Django project based on the following data: {data}"
    
#     chat_completion = client.chat.completions.create(
#         messages=[{"role": "user", "content": message_content}],
#         model="llama-3.3-70b-versatile",
#     )
    
#     generated_project_code = remove_ansi_escape_sequences(chat_completion.choices[0].message.content)
#     print("Generated Django Project Code:\n", generated_project_code)
    
#     # Request Selenium test script generation
#     selenium_request = f"Generate a Selenium test script to validate the functionality of the generated Django project: {generated_project_code}"
    
#     selenium_completion = client.chat.completions.create(
#         messages=[{"role": "user", "content": selenium_request}],
#         model="llama-3.3-70b-versatile",
#     )
    
#     selenium_script = remove_ansi_escape_sequences(selenium_completion.choices[0].message.content)
#     print("Generated Selenium Test Script:\n", selenium_script)
    
#     with open("selenium_test.py", "w") as file:
#         file.write(selenium_script)
#     print("Selenium test script saved: selenium_test.py")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Error: Module ID is required.")
#         sys.exit(1)

#     module_id = sys.argv[1]
#     fetch_data_from_db(module_id)

# groq

# import os
# import re
# import sys
# import mysql.connector
# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()

# def remove_ansi_escape_sequences(text):
#     """Remove ANSI escape sequences from text."""
#     ansi_escape = re.compile(r'(?:\x1B[@-Z\\]|\x1B\[[0-?]*[ -/]*[@-~])')
#     return ansi_escape.sub('', text)

# def fetch_data_from_db(module_id):
#     """Fetch selected module data from the database."""
#     conn = mysql.connector.connect(
#         database=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         host=os.getenv("DB_HOST")
#     )
#     cursor = conn.cursor()

#     # Fetch data for the specific module
#     query = "SELECT * FROM AIA_MODULE WHERE module_id = %s;"
    
#     cursor.execute(query, (module_id,))
#     module_data = cursor.fetchall()

#     send_to_groq("Selected Module Details", module_data)

#     cursor.close()
#     conn.close()

# def send_to_groq(context, data):
#     """Send module data to GroqCloud for AI processing and generate code."""
#     client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#     message_content = f"{context}: Generate a PHP code based on the following data: {data}"

#     chat_completion = client.chat.completions.create(
#         messages=[{"role": "user", "content": message_content}],
#         model="llama-3.3-70b-versatile",
#     )

#     generated_code = remove_ansi_escape_sequences(chat_completion.choices[0].message.content)
#     print("Generated Code:\n", generated_code)

#     # Save to file
#     with open(f"generated_module_{module_id}.py", "w") as file:
#         file.write(generated_code)
#     print(f"Code saved: generated_module_{module_id}.py")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Error: Module ID is required.")
#         sys.exit(1)

#     module_id = sys.argv[1]
#     fetch_data_from_db(module_id)


# ollama
# import os
# import re
# import sys
# import json
# import mysql.connector
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# def remove_ansi_escape_sequences(text):
#     """Remove ANSI escape sequences from text."""
#     ansi_escape = re.compile(r'(?:\x1B[@-Z\\]|\x1B\[[0-?]*[ -/]*[@-~])')
#     return ansi_escape.sub('', text)

# def fetch_data_from_db(module_id):
#     """Fetch selected module data from the database."""
#     conn = mysql.connector.connect(
#         database=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         host=os.getenv("DB_HOST")
#     )
#     cursor = conn.cursor()

#     # Fetch data for the specific module
#     query = "SELECT * FROM AIA_MODULE WHERE module_id = %s;"
    
#     cursor.execute(query, (module_id,))
#     module_data = cursor.fetchall()

#     send_to_ollama("Selected Module Details", module_data, module_id)

#     cursor.close()
#     conn.close()

# def send_to_ollama(context, data, module_id):
#     """Send module data to Ollama API for AI processing and generate code."""
#     ollama_url = "http://61.2.142.91:11434/api/chat"

#     # Define the message content for code generation
#     message_content = f"{context}: Generate a PHP code based on the following data: {data}"

#     # Prepare request payload
#     payload = {
#         "model": "llama3.1",
#         "messages": [{"role": "user", "content": message_content}]
#     }

#     try:
#         response = requests.post(ollama_url, json=payload)
#         response.raise_for_status()
        
#         # Extract generated response
#         generated_code = response.json()["message"]["content"]
#         generated_code = remove_ansi_escape_sequences(generated_code)

#         print("Generated Code:\n", generated_code)

#         # Save to file
#         filename = f"generated_module_{module_id}.php"
#         with open(filename, "w") as file:
#             file.write(generated_code)

#         print(f"Code saved: {filename}")

#     except requests.exceptions.RequestException as e:
#         print(f"Error communicating with Ollama: {e}")
#         return None

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Error: Module ID is required.")
#         sys.exit(1)

#     module_id = sys.argv[1]
#     fetch_data_from_db(module_id)

# ollama with choosen lan
import os
import re
import sys
import json
import mysql.connector
import requests
from dotenv import load_dotenv

load_dotenv()

def remove_ansi_escape_sequences(text):
    """Remove ANSI escape sequences from text."""
    ansi_escape = re.compile(r'(?:\x1B[@-Z\\]|\x1B\[[0-?]*[ -/]*[@-~])')
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

    send_to_ollama("Module Details", module_data, module_id, language)

    cursor.close()
    conn.close()

def send_to_ollama(context, data, module_id, language):
    """Send module data to Ollama API and generate code dynamically based on language."""
    ollama_url = "http://localhost:8434/api/chat"

    # Dynamic message content based on user-selected language
    message_content = f"{context}: Generate a {language.upper()} code based on the following data: {data}"

    payload = {
        "model": "llama3.1",
        "messages": [{"role": "user", "content": message_content}]
    }

    try:
        response = requests.post(ollama_url, json=payload)
        response.raise_for_status()
        
        # Extract and clean up generated response
        generated_code = response.json()["message"]["content"]
        generated_code = remove_ansi_escape_sequences(generated_code)

        print("Generated Code:\n", generated_code)

        # Save the generated file with appropriate extension
        extension = {"php": "php", "java": "java", "django": "py"}.get(language, "txt")
        filename = f"generated_module_{module_id}.{extension}"

        with open(filename, "w") as file:
            file.write(generated_code)

        print(f"Code saved: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Module ID and language are required.")
        sys.exit(1)

    module_id = sys.argv[1]
    language = sys.argv[2].lower()  # Ensure lowercase for consistency
    fetch_data_from_db(module_id, language)
