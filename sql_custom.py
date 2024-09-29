import requests
import json
import sqlite3

def get_db_schema(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema = {}
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        schema[table_name] = [column[1] for column in columns]

    conn.close()
    return schema

def schema_to_string(schema):
    schema_str = "Database Schema:\n"
    for table, columns in schema.items():
        schema_str += f"Table: {table}\n"
        schema_str += f"Columns: {', '.join(columns)}\n\n"
    return schema_str

def generate_query(prompt, schema, model="llama2"):
    url = "http://localhost:11434/api/generate"

    schema_str = schema_to_string(schema)
    full_prompt = f"""Given the following database schema:

{schema_str}

Generate an SQL query for the following request:
{prompt}

Provide only the SQL query without any additional explanation."""

    data = {
        "model": "llama3.1",
        "prompt": full_prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return json.loads(response.text)['response']
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def get_available_models():
    url = "http://localhost:11434/api/tags"
    try:
        response = requests.get(url)
        response.raise_for_status()
        models = json.loads(response.text)['models']
        return [model['name'] for model in models]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching models: {str(e)}")
        return []

def main():
    print("Flexible LLM-based Query Generator using Ollama")
    print("===============================================")

    db_path = "sample_company.db"
    schema = get_db_schema(db_path)

    print("\nDatabase schema loaded successfully.")
    print(schema_to_string(schema))

    available_models = get_available_models()
    print("\nAvailable models:")
    for i, model in enumerate(available_models, 1):
        print(f"{i}. {model}")

    model_choice = input("\nEnter the number of the model you want to use (default is llama2): ")
    if model_choice.isdigit() and 1 <= int(model_choice) <= len(available_models):
        chosen_model = available_models[int(model_choice) - 1]
    else:
        chosen_model = "llama2"

    print(f"\nUsing model: {chosen_model}")

    while True:
        user_input = input("\nEnter your database query in natural language (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Exiting the program. Goodbye!")
            break

        generated_query = generate_query(user_input, schema, model=chosen_model)
        print("\nGenerated SQL Query:")
        print(generated_query)

if __name__ == "__main__":
    main()
