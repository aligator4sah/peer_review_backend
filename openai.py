import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'

# Define the prompt
prompt_text = "What is the meaning of life?"

individual_summary_prompt = "You are required to provide a summary of keywords extracted from each individual reviewer, capturing the key aspects of their comments on the paper. Ensure that the keywords are concise, limited to no more than five words, and that similar topics are grouped under the same keywords."
all_summary_prompt = "Based on Section 1, now you are tasked with providing keywords that have been summarized from all reviewers' comments. These keywords should be mentioned by two or more reviewers. Keep the keywords succinct, limited to no more than five words. Additionally, include a brief summary paragraph (around 2-3 sentences) to highlight the reviewers' comments on the topic, specifying the reviewer involved. There may be more than one keyword so you should provide all the keywords you have identified."
disagreement_summary_prompt = """In this section, your task is to identify and summarize the disagreements found in the review comments. Disagreements can be identified in the following ways: 1) differing or contradictory opinions among reviewers on a specific topic, 2) a topic mentioned and strongly supported by only one reviewer while others ignored it, and 3) reviewers providing different recommendations for the paper, valuing different aspects.
Use keywords to summarize these disagreements, limited to no more than five words. Additionally, provide a brief summary paragraph (around 2-3 sentences) highlighting the reviewers' comments on the topic, specifying the reviewer involved. 
Furthermore, for each corresponding topic, provide a question for the editor to ask the reviewers, motivating them to discuss this disagreement. The question should specify the exact topic and reviewer. 
There may be more than one keyword so you should provide all the keywords you have identified. """
review_comment_prompt = "Your task is to motivate each reviewer to join the discussion. After thoroughly examining each reviewer's comment, identify areas where the reviewer has not addressed a certain topic or has contradictory ideas compared to other reviewers. Provide all the 4 reviewers with a specific question to highlight these points and ask them to elaborate further."

# Generate a response from the model
response = openai.Completion.create(
  engine="text-davinci-003",  # Choose the GPT model you want to use
  prompt=prompt_text,
  max_tokens=50  # Adjust the length of the response if needed
)

# Print the response
print(response.choices[0].text.strip())
