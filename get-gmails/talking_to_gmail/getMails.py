import imapclient
import pyzmail


# I followed this https://replit.com/talk/learn/How-to-Make-a-Python-Email-Bot/8194

def getMails(username, password):
    i = imapclient.IMAPClient('imap.gmail.com')

    # Username is email address
    # Password is an 'application specific' password (https://support.google.com/mail/answer/185833?hl=en)

    i.login(username, password)

    # Note: When this reads your mails, it will mark them as read. Unless you want to mark all your emails as read,
    # you should pick a folder besides "INBOX".  I created a folder (label) in gmail named 'Jobs'.
    i.select_folder('Jobs')
    uids = i.search()
    rawmsgs = i.fetch(uids, ['BODY[]'])

    mails = []
    for uid in uids:
        msg = pyzmail.PyzMessage.factory(rawmsgs[uid][b"BODY[]"])
        if msg.text_part:
            mail = msg.text_part.get_payload().decode(msg.text_part.charset)
            mails.append(mail)
    return mails