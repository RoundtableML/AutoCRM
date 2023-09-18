import secrets
import llmJSONs

import getMails
import fun_with_gspread

# import fun_with_sheets # Decided to use gspread instead of sheets api







# Main has 3 steps
def main():
    #Step 1 - Get mails from gmail
    mails = getMails.getMails(secrets.username, secrets.password, "Jobs")
    for mail in mails:
        print("got mail!", (mail["body"][:10]))



# https://docs.google.com/document/d/1n7TDQAV_fVOOjWpiIDpD4YlDbNzhRJOdXciePi6P6RU/edit

    # # Step 2 - TODO - Programmatically call AI to analyze mails and return JSON
    #
    #
    # # Step 3 - Take the AI-generated JSON, add it to google sheets using gspread
    # next_open_row = 0
    #
    # rows = []
    # for res in llmJSONs.responses:
    #     if res['isRelatedToJob']:
    #         row = []
    #         row.append(res['companyName'])
    #         row.append(res['applicationStatus'])
    #         row.append(res['roleName'])
    #         rows.append(row)
    # fun_with_gspread.add_rows('test sheet 2', rows)



if __name__ == '__main__':
    main()