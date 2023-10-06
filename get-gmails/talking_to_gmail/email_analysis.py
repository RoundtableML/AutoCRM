import openai
import config

# Initialize OpenAI API
openai.api_key = config.OPENAI_API

def analyze_email(mail):
    # Construct the prompt for the OpenAI model
    prompt = f"Analyze the following internship application email:\n\nSubject: {mail['subject']}\nFrom: {mail['sender']['address']}\nBody: {mail['body']}\n\nIdentify the company name, position applied for, and application status."

    # Make the API call
    response = openai.Completion.create(
      engine="gpt-3.5-turbo-16k",
      prompt=prompt
    )

    # Parse the response to extract the desired information
    # Assuming the model returns answers in the format "Company: XYZ, Position: ABC, Status: Accepted"
    lines = response.choices[0].text.strip().split(', ')
    data = {line.split(": ")[0]: line.split(": ")[1] for line in lines}

    # Extract information or set to None if not available
    company = data.get("Company", None)
    position = data.get("Position", None)
    status = data.get("Status", None)

    for mail in mails:
      company, position, status = analyze_email(mail)
      print(f"Company: {company}, Position: {position}, Status: {status}")

    return company, position, status

# Iterate over mails list and analyze each mail

