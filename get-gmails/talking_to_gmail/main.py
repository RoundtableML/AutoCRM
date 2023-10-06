# Existing imports
import getMails
from email_analysis import analyze_email  # If using a separate module
import config

def main():
    # Step 1: Get mails from Gmail
    mails = getMails.getMails(config.username, config.password, "Jobs")


    # Step 2: Analyze each email using OpenAI
    # for mail in mails:
    #     company, position, status = analyze_email(mail)
    #     print(f"Company: {company}, Position: {position}, Status: {status}")
    mail = mails[0]
    print(mail)
    company, position, status = analyze_email(mail)
    print(f"Company: {company}, Position: {position}, Status: {status}")

    
    # Step 3: Add to Google Sheets (if required)
    # ...

if __name__ == "__main__":
    main()
