import json
import requests  # For making API calls to the LLM

def call_llm_api(prompt, api_key, endpoint="https://api.x.ai/v1/completions"):
    """
    Calls an LLM API to process the input prompt.
    
    Args:
        prompt (str): The input prompt to be processed.
        api_key (str): API key for authentication.
        endpoint (str): API endpoint for the LLM.
    
    Returns:
        str: Processed prompt from the LLM.
    """
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": f"Refine and enhance the following prompt for clarity and specificity, keeping the original intent: {prompt}",
            "max_tokens": 200,
            "temperature": 0.7
        }
        response = requests.post(endpoint, headers=headers, json=data)
        response.raise_for_status()
        # Assuming the API returns a JSON with a 'text' field containing the processed prompt
        return response.json().get("text", prompt)  # Fallback to original prompt if API fails
    except Exception as e:
        print(f"Error calling LLM API: {e}")
        return prompt  # Fallback to original prompt

def convert_to_json_prompt(input_prompt, api_key):
    """
    Processes an input prompt with an LLM and converts it to JSON.
    
    Args:
        input_prompt (str): The input prompt to be processed.
        api_key (str): API key for the LLM service.
        
    Returns:
        str: JSON-formatted string containing the processed prompt.
    """
    # Process the prompt with the LLM
    processed_prompt = call_llm_api(input_prompt, api_key)
    
    # Structure the prompt in JSON format
    json_prompt = {
        "original_prompt": input_prompt,
        "processed_prompt": processed_prompt,
        "metadata": {
            "source": "user_input",
            "format": "text",
            "processed_by": "LLM",
            "processed": True
        }
    }
    
    # Convert to JSON string with proper formatting
    return json.dumps(json_prompt, indent=2)

def main():
    # Get API key (in practice, use environment variables or secure storage)
    api_key = input("Enter your LLM API key: ")
    
    # Get input prompt from user
    user_prompt = input("Enter your prompt: ")
    
    # Convert the prompt to JSON with LLM processing
    json_output = convert_to_json_prompt(user_prompt, api_key)
    
    # Print the JSON result
    print("\nJSON-formatted prompt:")
    print(json_output)
    
    # Optionally save to file
    save = input("\nWould you like to save the JSON output to a file? (y/n): ").lower()
    if save == 'y':
        with open('prompt_output.json', 'w') as f:
            f.write(json_output)
        print("JSON output saved to 'prompt_output.json'")

if __name__ == "__main__":
    main()
