import imapclient # Fetches email
import pyzmail # Parses the email into readable text

import secrets
import llmJSONs
import fun_with_sheets # Decided to use gspread instead of sheets api
import getMails
import fun_with_gspread # Decided to use gspread instead of sheets api






# Main has 3 steps
def main():
    # Step 1 - Get mails from gmail
    mails = getMails.getMails(secrets.username, secrets.password)
    for mail in mails:
        print(mail)



    # Step 2 - TODO - Programmatically call AI to analyze mails and return JSON


    # Step 3 - Take the AI-generated JSON, add it to google sheets using gspread
    next_open_row = 0

    rows = []
    for res in llmJSONs.responses:
        if res['isRelatedToJob']:
            row = []
            row.append(res['companyName'])
            row.append(res['applicationStatus'])
            row.append(res['roleName'])
            rows.append(row)
    fun_with_gspread.add_rows('test sheet 2', rows)



if __name__ == '__main__':
    main()