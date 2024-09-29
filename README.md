# LLM-based SQL Query Generator using Ollama

This project implements a natural language to SQL query generator using Ollama, a platform for running large language models locally. The system allows users to input database queries in natural language and receive corresponding SQL queries based on a given database schema.

## Features

- Automatic database schema extraction from SQLite databases
- Flexible model selection from available Ollama models
- Natural language to SQL query generation
- Interactive command-line interface

## Prerequisites

- Python 3.7+
- Ollama installed and running on your local machine
- SQLite (usually comes pre-installed with Python)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/llm-query-generator.git
   cd llm-query-generator
   ```

2. Install the required Python packages:
   ```
   pip install requests
   ```

3. Ensure Ollama is installed and running. Follow the installation instructions on the [Ollama GitHub page](https://github.com/jmorganca/ollama).

## Usage

1. Start the Ollama service:
   ```
   ollama serve
   ```

2. Create a sample SQLite database (optional):
   ```
   python create_sample_db.py
   ```

3. Run the query generator:
   ```
   python query_generator.py
   ```

4. Follow the prompts to select a model and enter your natural language queries.

## Sample Queries

Here are some example queries you can try:

- "Show me all employees in the Engineering department"
- "What is the average salary of employees older than 35?"
- "List the departments and their locations"
- "Who is the highest paid employee in each department?"

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- This project uses [Ollama](https://github.com/jmorganca/ollama) for running large language models locally.
- Inspired by the growing need for natural language interfaces to databases.
