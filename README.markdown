# Jsonifinator

## Overview
The **Prompt-Processing-JSONificator-inator** is a Python script designed to take any user-provided prompt, enhance it using a Large Language Model (LLM) via an API, and output the result in a structured JSON format. Inspired by the ingenious (and slightly chaotic) spirit of Dr. Heinz Doofenshmirtz, this script is perfect for developers who want to process and organize prompts with a touch of flair.

## Features
- **Prompt Enhancement**: Uses an LLM to refine and improve input prompts for clarity and specificity.
- **JSON Output**: Wraps both original and processed prompts in a clean JSON structure with metadata.
- **File Saving**: Optionally saves the JSON output to a file (`prompt_output.json`).
- **Error Handling**: Falls back to the original prompt if the LLM API call fails.
- **Extensible**: Easily adaptable for different LLM APIs or prompt processing instructions.

## Requirements
- Python 3.6 or higher
- `requests` library (`pip install requests`)
- An API key for an LLM service (e.g., xAI, OpenAI, or another compatible provider)

## Setup
1. **Clone or Download**:
   - Download the script (`prompt_to_json_with_llm.py`) or clone this repository.
   
2. **Install Dependencies**:
   ```bash
   pip install requests
   ```

3. **Configure API Access**:
   - Obtain an API key from your LLM provider (e.g., [xAI API](https://x.ai/api) or OpenAI).
   - Replace the placeholder API endpoint in the script (`https://api.x.ai/v1/completions`) with your provider’s actual endpoint, if different.

4. **Secure API Key**:
   - Avoid hardcoding your API key. Consider using environment variables:
     ```bash
     export LLM_API_KEY='your-api-key-here'
     ```
     Update the script to read the key:
     ```python
     import os
     api_key = os.getenv('LLM_API_KEY')
     ```

## Usage
1. **Run the Script**:
   ```bash
   python prompt_to_json_with_llm.py
   ```

2. **Enter Inputs**:
   - Provide your LLM API key when prompted (or configure via environment variables).
   - Enter your prompt (e.g., "Tell me about space").
   - Choose whether to save the JSON output to a file (`prompt_output.json`).

3. **Example Output**:
   For an input prompt like "Tell me about space":
   ```json
   {
     "original_prompt": "Tell me about space",
     "processed_prompt": "Provide a detailed explanation of space exploration, including key milestones and future prospects",
     "metadata": {
       "source": "user_input",
       "format": "text",
       "processed_by": "LLM",
       "processed": true
     }
   }
   ```

## Notes
- **LLM API**: The script uses a placeholder API endpoint (`https://api.x.ai/v1/completions`). Update it to match your LLM provider’s endpoint (e.g., OpenAI’s `https://api.openai.com/v1/completions`).
- **Customization**: Modify the `call_llm_api` function to change how the LLM processes the prompt (e.g., summarize, rephrase, or translate).
- **Error Handling**: If the API call fails, the script falls back to the original prompt to ensure functionality.
- **Security**: Store API keys securely using environment variables or a configuration file.
- **Inspiration**: Named with a nod to Dr. Doofenshmirtz’s penchant for dramatic "-inator" devices, this script brings a bit of whimsy to prompt processing.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it, but beware of any Tri-State Area domination plans!
