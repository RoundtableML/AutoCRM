import gspread

# you will need to add your own credentials.json and authorized_user.json
def testing():
    gc = gspread.oauth(
        credentials_filename='../credentials.json',
        authorized_user_filename='../authorized_user.json'
    )

    sh = gc.open("test sheet 2")

    print(sh.sheet1.get('A1'))

def add_rows(sh, contents):
    gc = gspread.oauth(
        credentials_filename='../credentials.json',
        authorized_user_filename='../authorized_user.json'
    )
    sh = gc.open("test sheet 2")

    r = 1
    ws = sh.get_worksheet(0)
    occupied_rows = (len(ws.get_all_values()))
    r = occupied_rows + 1
    for application in contents:
        c = 1
        for value in application:
            ws.update_cell(r, c, value)
            c += 1
        r += 1