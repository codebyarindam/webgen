# import os
# import re
# import sys
# import json
# import datetime
# import mysql.connector
# import subprocess
# from dotenv import load_dotenv
# from groq import Groq

# # Load environment variables
# load_dotenv()

# def remove_ansi_escape_sequences(text):
#     """Remove ANSI escape sequences from text."""
#     ansi_escape = re.compile(r'(?:\x1B[@-Z\\]|\x1B\[[0-?]*[ -/]*[@-~])')
#     return ansi_escape.sub('', text)

# def execute_code(code, language):
#     """Execute the generated code and return output or error."""
#     extension = {"php": "php", "java": "java", "django": "py"}.get(language, "txt")
#     temp_filename = f"temp_code.{extension}"
    
#     with open(temp_filename, "w", encoding="utf-8") as file:
#         file.write(code)
    
#     try:
#         if language == "django" or extension == "py":
#             result = subprocess.run(["python", temp_filename], capture_output=True, text=True)
#         elif extension == "php":
#             result = subprocess.run(["php", temp_filename], capture_output=True, text=True)
#         elif extension == "java":
#             subprocess.run(["javac", temp_filename], capture_output=True, text=True)
#             result = subprocess.run(["java", temp_filename.replace(".java", "")], capture_output=True, text=True)
        
#         os.remove(temp_filename)  # Remove the temporary file after execution
#         return result.stdout, result.stderr
#     except Exception as e:
#         return "", str(e)

# def refine_code_until_successful(generated_code, language):
#     """Refine code by iterating through errors until it compiles successfully."""
#     client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
#     while True:
#         output, error = execute_code(generated_code, language)
#         if not error:
#             print("Code executed successfully.")
#             return generated_code  # Return final working code
        
#         print(f"Error encountered: {error}")
        
#         error_fix_request = f"Fix the following error in {language} code: {error}\n\nOriginal code:\n{generated_code}"
#         chat_completion = client.chat.completions.create(
#             messages=[{"role": "user", "content": error_fix_request}],
#             model="llama-3.3-70b-versatile",
#         )
        
#         generated_code = remove_ansi_escape_sequences(chat_completion.choices[0].message.content)
#         print("Updated Code:\n", generated_code)

# def generate_selenium_script(generated_project_code, module_id):
#     """Generate a Selenium test script for the generated project."""
#     try:
#         client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#         selenium_request = f"Generate a Selenium test script to validate the functionality of the generated project: {generated_project_code}"

#         selenium_completion = client.chat.completions.create(
#             messages=[{"role": "user", "content": selenium_request}],
#             model="llama-3.3-70b-versatile",
#         )

#         selenium_script = remove_ansi_escape_sequences(selenium_completion.choices[0].message.content)
#         print("Generated Selenium Test Script:\n", selenium_script)

#         return selenium_script
#     except Exception as e:
#         print(f"Error generating Selenium script: {e}")
#         return None

# def fetch_data_from_db(module_id, language):
#     """Fetch module data from the database and process it."""
#     try:
#         conn = mysql.connector.connect(
#             database=os.getenv("DB_NAME"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#             host=os.getenv("DB_HOST")
#         )
#         cursor = conn.cursor()

#         query = "SELECT * FROM AIA_MODULE WHERE module_id = %s;"
#         cursor.execute(query, (module_id,))
#         module_data = cursor.fetchall()

#         if not module_data:
#             print(f"Error: No data found for module_id {module_id}.")
#             return

#         client = Groq(api_key=os.getenv("GROQ_API_KEY"))
#         message_content = f"Generate a {language.upper()} code based on the following data: {module_data}"
#         chat_completion = client.chat.completions.create(
#             messages=[{"role": "user", "content": message_content}],
#             model="llama-3.3-70b-versatile",
#         )

#         generated_code = remove_ansi_escape_sequences(chat_completion.choices[0].message.content)
#         generated_code = refine_code_until_successful(generated_code, language)
        
#         selenium_script = generate_selenium_script(generated_code, module_id)
#         print("Final Selenium Script:\n", selenium_script)

#     except mysql.connector.Error as err:
#         print(f"Database Error: {err}")
#     finally:
#         cursor.close()
#         conn.close()

# if __name__ == "__main__":
#     if len(sys.argv) < 3:
#         print("Error: Module ID and language are required.")
#         sys.exit(1)

#     module_id = sys.argv[1]
#     language = sys.argv[2].lower()
#     fetch_data_from_db(module_id, language)
# import os
# import re
# import sys
# import json
# import datetime
# import mysql.connector
# import subprocess
# from dotenv import load_dotenv
# from groq import Groq

# # Load environment variables
# load_dotenv()

# def remove_ansi_escape_sequences(text):
#     """Extract only the code from the response, removing unnecessary descriptions."""
#     code_match = re.search(r'```\w*\n(.*?)```', text, re.DOTALL)
#     return code_match.group(1).strip() if code_match else text.strip()

# def execute_code(code, language):
#     """Execute the generated code and return output or error."""
#     extension = {"php": "php", "java": "java", "django": "py"}.get(language, "txt")
#     temp_filename = f"temp_code.{extension}"
    
#     with open(temp_filename, "w", encoding="utf-8") as file:
#         file.write(code)
    
#     try:
#         if language == "django" or extension == "py":
#             result = subprocess.run(["python", temp_filename], capture_output=True, text=True)
#         elif extension == "php":
#             result = subprocess.run(["php", temp_filename], capture_output=True, text=True)
#         elif extension == "java":
#             subprocess.run(["javac", temp_filename], capture_output=True, text=True)
#             result = subprocess.run(["java", temp_filename.replace(".java", "")], capture_output=True, text=True)
        
#         os.remove(temp_filename)  # Remove the temporary file after execution
#         return result.stdout, result.stderr
#     except Exception as e:
#         return "", str(e)

# def refine_code_until_successful(generated_code, language):
#     """Refine code by iterating through errors until it compiles successfully."""
#     client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
#     while True:
#         output, error = execute_code(generated_code, language)
#         if not error:
#             print("Code executed successfully.")
#             return generated_code  # Return final working code
        
#         print(f"Error encountered: {error}")
        
#         error_fix_request = f"Fix the following error in {language} code. Do not include explanations, only provide the corrected code.\n\nError: {error}\n\nOriginal code:\n{generated_code}"
#         chat_completion = client.chat.completions.create(
#             messages=[{"role": "user", "content": error_fix_request}],
#             model="llama-3.3-70b-versatile",
#         )
        
#         generated_code = remove_ansi_escape_sequences(chat_completion.choices[0].message.content)
#         print("Updated Code:\n", generated_code)

# def generate_selenium_script(generated_project_code, module_id):
#     """Generate a Selenium test script for the generated project."""
#     try:
#         client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#         selenium_request = f"Generate a Selenium test script to validate the functionality of the generated project. Only return the Selenium script without any explanations.\n\n{generated_project_code}"

#         selenium_completion = client.chat.completions.create(
#             messages=[{"role": "user", "content": selenium_request}],
#             model="llama-3.3-70b-versatile",
#         )

#         selenium_script = remove_ansi_escape_sequences(selenium_completion.choices[0].message.content)
#         print("Generated Selenium Test Script:\n", selenium_script)

#         return selenium_script
#     except Exception as e:
#         print(f"Error generating Selenium script: {e}")
#         return None

# def fetch_data_from_db(module_id, language):
#     """Fetch module data from the database and process it."""
#     try:
#         conn = mysql.connector.connect(
#             database=os.getenv("DB_NAME"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#             host=os.getenv("DB_HOST")
#         )
#         cursor = conn.cursor()

#         query = "SELECT * FROM AIA_MODULE WHERE module_id = %s;"
#         cursor.execute(query, (module_id,))
#         module_data = cursor.fetchall()

#         if not module_data:
#             print(f"Error: No data found for module_id {module_id}.")
#             return

#         client = Groq(api_key=os.getenv("GROQ_API_KEY"))
#         message_content = f"Generate a {language.upper()} code based on the following data. Only return the code without any explanations.\n\n{module_data}"
#         chat_completion = client.chat.completions.create(
#             messages=[{"role": "user", "content": message_content}],
#             model="llama-3.3-70b-versatile",
#         )

#         generated_code = remove_ansi_escape_sequences(chat_completion.choices[0].message.content)
#         generated_code = refine_code_until_successful(generated_code, language)
        
#         selenium_script = generate_selenium_script(generated_code, module_id)
#         print("Final Selenium Script:\n", selenium_script)

#     except mysql.connector.Error as err:
#         print(f"Database Error: {err}")
#     finally:
#         cursor.close()
#         conn.close()

# if __name__ == "__main__":
#     if len(sys.argv) < 3:
#         print("Error: Module ID and language are required.")
#         sys.exit(1)

#     module_id = sys.argv[1]
#     language = sys.argv[2].lower()
#     fetch_data_from_db(module_id, language)
import os
import re
import sys
import json
import datetime
import mysql.connector
import subprocess
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

def remove_ansi_escape_sequences(text):
    """Extract only the code from the response, removing unnecessary descriptions and comments."""
    code_match = re.search(r'```\w*\n(.*?)```', text, re.DOTALL)
    if code_match:
        return code_match.group(1).strip()
    
    # Remove extra explanations or comments
    text = re.sub(r'\n\s*-.*', '', text)  # Remove list-style explanations
    text = re.sub(r'\b(Note|Explanation|Description):.*', '', text, flags=re.IGNORECASE)  # Remove explicit explanations
    return text.strip()

def execute_code(code, language):
    """Execute the generated code and return output or error."""
    extension = {"php": "php", "java": "java", "django": "py"}.get(language, "txt")
    temp_filename = f"temp_code.{extension}"
    
    with open(temp_filename, "w", encoding="utf-8") as file:
        file.write(code)
    
    try:
        if language == "django" or extension == "py":
            result = subprocess.run(["python", temp_filename], capture_output=True, text=True)
        elif extension == "php":
            result = subprocess.run(["php", temp_filename], capture_output=True, text=True)
        elif extension == "java":
            subprocess.run(["javac", temp_filename], capture_output=True, text=True)
            result = subprocess.run(["java", temp_filename.replace(".java", "")], capture_output=True, text=True)
        
        os.remove(temp_filename)  # Remove the temporary file after execution
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)

def refine_code_until_successful(generated_code, language):
    """Refine code by iterating through errors until it compiles successfully."""
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    while True:
        output, error = execute_code(generated_code, language)
        if not error:
            print("Code executed successfully.")
            return generated_code  # Return final working code
        
        print(f"Error encountered: {error}")
        
        error_fix_request = f"Fix the following error in {language} code. Only provide the corrected code.\n\nError: {error}\n\nOriginal code:\n{generated_code}"
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": error_fix_request}],
            model="llama-3.3-70b-versatile",
        )
        
        generated_code = remove_ansi_escape_sequences(chat_completion.choices[0].message.content)
        print("Updated Code:\n", generated_code)

def generate_selenium_script(generated_project_code, module_id):
    """Generate a Selenium test script for the generated project."""
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        selenium_request = f"Generate a Selenium test script to validate the functionality of the generated project. Only return the Selenium script without any explanations.\n\n{generated_project_code}"

        selenium_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": selenium_request}],
            model="llama-3.3-70b-versatile",
        )

        selenium_script = remove_ansi_escape_sequences(selenium_completion.choices[0].message.content)
        print("Generated Selenium Test Script:\n", selenium_script)

        return selenium_script
    except Exception as e:
        print(f"Error generating Selenium script: {e}")
        return None

def fetch_data_from_db(module_id, language):
    """Fetch module data from the database and process it."""
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

        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        message_content = f"Generate a {language.upper()} code based on the following data. Only return the code without any explanations.\n\n{module_data}"
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": message_content}],
            model="llama-3.3-70b-versatile",
        )

        generated_code = remove_ansi_escape_sequences(chat_completion.choices[0].message.content)
        generated_code = refine_code_until_successful(generated_code, language)
        
        selenium_script = generate_selenium_script(generated_code, module_id)
        print("Final Selenium Script:\n", selenium_script)

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Module ID and language are required.")
        sys.exit(1)

    module_id = sys.argv[1]
    language = sys.argv[2].lower()
    fetch_data_from_db(module_id, language)
