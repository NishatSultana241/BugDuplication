import re
import pandas as pd

def extract_similarity_score(text):
    """
    Extracts the similarity score from the given text using a regular expression.

    Args:
        text (str): The input text containing the similarity score.

    Returns:
        float: The extracted similarity score, or None if not found.
    """
    # Define the regular expression to find the similarity score
    pattern = r"similarity score of ([0-9]*\.[0-9]+)"

    # Search for the pattern in the text
    match = re.search(pattern, text)

    # If a match is found, return the similarity score as a float
    if match:
        return float(match.group(1))

    # Return None if no match is found
    return None

# Load the CSV file
data = pd.read_csv('responses.csv')

# Ensure the column exists
if 'Response from Llava' in data.columns:
    # Apply the extraction function to each row in the column
    data['Similarity Score'] = data['Response from Llava'].apply(extract_similarity_score)

    # Save the updated DataFrame to a new CSV file
    data.to_csv('responses_with_scores.csv', index=False)
    print("Similarity scores have been extracted and saved to 'responses_with_scores.csv'.")
else:
    print("The column 'Response from Llava' does not exist in the CSV file.")

