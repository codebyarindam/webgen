# import os
# import re
# import sys
# import json
# import mysql.connector
# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()

# def remove_ansi_escape_sequences(text):
#     """Remove ANSI escape sequences from text."""
#     ansi_escape = re.compile(r'(?:\x1B[@-Z\\]|]|\x1B\[[0-?]*[ -/]*[@-~])')
#     return ansi_escape.sub('', text)

# def fetch_data_from_db(module_id, language):
#     """Fetch selected module data from the database and send it for code generation."""
#     conn = mysql.connector.connect(
#         database=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         host=os.getenv("DB_HOST")
#     )
#     cursor = conn.cursor()
#     query = "SELECT * FROM AIA_MODULE WHERE module_id = %s;"
#     cursor.execute(query, (module_id,))
#     module_data = cursor.fetchall()
    
#     send_to_groq("Module Details", module_data, module_id, language)
    
#     cursor.close()
#     conn.close()

# def send_to_groq(context, data, module_id, language):
#     """Send module data to GroqCloud API and generate code dynamically based on language."""
#     client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
#     message_content = f"{context}: Generate a {language.upper()} code based on the following data: {data} and selenium script."
    
#     chat_completion = client.chat.completions.create(
#         messages=[{"role": "user", "content": message_content}],
#         model="llama-3.3-70b-versatile",
#     )
    
#     generated_code = remove_ansi_escape_sequences(chat_completion.choices[0].message.content)
#     print("Generated Code:\n", generated_code)
    
#     # Save the generated file with appropriate extension
#     extension = {"php": "php", "java": "java", "django": "py"}.get(language, "txt")
#     filename = f"generated_module_{module_id}.{extension}"
    
#     with open(filename, "w") as file:
#         file.write(generated_code)
#     print(f"Code saved: {filename}")
    

# if __name__ == "__main__":
#     if len(sys.argv) < 3:
#         print("Error: Module ID and language are required.")
#         sys.exit(1)
    
#     module_id = sys.argv[1]
#     language = sys.argv[2].lower()  # Ensure lowercase for consistency
#     fetch_data_from_db(module_id, language)
import os
import re
import sys
import json
import mysql.connector
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GENERATED_FILES_DIR = "generated_files"

# Ensure directory exists
if not os.path.exists(GENERATED_FILES_DIR):
    os.makedirs(GENERATED_FILES_DIR)

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
    
    send_to_groq("Module Details", module_data, module_id, language)
    
    cursor.close()
    conn.close()

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
    
    # Save the generated file with appropriate extension
    extension = {"php": "php", "java": "java", "django": "py"}.get(language, "txt")
    filename = os.path.join(GENERATED_FILES_DIR, f"generated_module_{module_id}.{extension}")
    
    with open(filename, "w") as file:
        file.write(generated_code)
    print(f"Code saved: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Module ID and language are required.")
        sys.exit(1)
    
    module_id = sys.argv[1]
    language = sys.argv[2].lower()  # Ensure lowercase for consistency
    fetch_data_from_db(module_id, language)
