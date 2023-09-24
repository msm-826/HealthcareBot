import openai

class GetGPT:

    def __init__(self) -> None:
        openai.api_key = 'paste your openai api key'

    def getResult(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",  # Use the Codex engine for code-related prompts
            prompt= prompt,
            max_tokens=100,  # Set the desired length of the response
            temperature=0.7,  # Control the randomness of the generated response
            n=1,  # Generate a single response
            stop=None  # Let the model generate a complete response
        )

        generated_text = response.choices[0].text.strip()
        # print(type(generated_text))
        generated_text = generated_text.replace('?', '').strip()
        return(generated_text)
