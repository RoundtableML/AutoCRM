import imapclient
import pyzmail

# Initially followed this https://replit.com/talk/learn/How-to-Make-a-Python-Email-Bot/8194

def getMails(username, password, folderName):
    server = imapclient.IMAPClient('imap.gmail.com')

    # Username is email address
    # Password is an 'application specific' password (https://support.google.com/mail/answer/185833?hl=en)
    server.login(username, password)

    server.select_folder('Jobs')
    mail_ids = server.search() # Will mark emails as read.
    rawmsgs = server.fetch(mail_ids, ['BODY[]'])
    mails = []
    for id in mail_ids:
        msg = pyzmail.PyzMessage.factory(rawmsgs[id][b"BODY[]"])
        if msg.text_part:
            subject = msg.get_subject()
            sender = list(msg.get_address('from'))
            recipient = list(msg.get_address('to'))
            body = msg.text_part.get_payload().decode(msg.text_part.charset)
            body = " ".join(body.split()).replace(">", "").replace("&#39;", "'").replace("&rsquo;", "'")

            mail = {
                "subject": subject,
                "sender": {
                    "name": sender[0],
                    "address": sender[1]
                },
                "recipient": {
                    "name": recipient[0],
                    "address": recipient[1]
                },
                "body": body,
            }

            mails.append(mail)
            print("$$$$$$$$$$$$$$$$$$$$$$$$$")
            print("Subject: ", subject, "From: ", sender[1], "To: ", recipient[1])
            print("id", id)
            print(body)
            print("$$$$$$$$$$$$$$$$$$$$$$$$$")
    return mails
