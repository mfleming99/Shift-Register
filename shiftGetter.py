from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import imaplib
import email
import time

ORG_EMAIL = "@gmail.com" #change this to your email providor

FROM_EMAIL = "johnny_appleseed" + ORG_EMAIL #change this to your name

FROM_PWD = "Password1" #Change this to your password
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993
LOGIN_URL = "https://login.wheniwork.com"
SHIFT_URL = "https://appx.wheniwork.com/requests/shift"

#Change the below login to match your WhenIWork credentials.
LOGIN = {'email': 'johnny_appleseed@gmail.com', 'password': 'password1'}

def getShift(varSubject):

    varSubject = varSubject.split()
    name = varSubject[0] +" " + varSubject[1]
    driver = webdriver.Firefox()
    driver.maximize_window()
    try:
        driver.get(LOGIN_URL)
        u = driver.find_element_by_name('email')
        u.send_keys(LOGIN['email'])
        p = driver.find_element_by_name('password')
        p.send_keys(LOGIN['password'])
        p.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.get(SHIFT_URL)
        a = driver.find_element_by_xpath("//*[contains(text(), '"+ name + "')]")
        a.click()
        b = driver.find_elements_by_xpath("//*[contains(text(), 'Accept')]")[1]
        time.sleep(1)
        b.click()
    except:
        print("Registration failed")

    time.sleep(3)
    time.sleep(3)
    driver.close()


#Redefine this function to match your avalibilty. I was indifferent to time of
#Shift. I think it would be super cool to used google calender API 
def dayFree(varSubject):
    try:
        varSubject = varSubject.split()
        month = varSubject[-2]
        day = int(varSubject[-1])
        return ((month == 'Jul' and day > 22) or (month == 'Aug' and day < 22 and day > 4))
    except:
        print("Email was not a time off request")
        return False

def scanMail():
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL,FROM_PWD)
    mail.select('inbox')
    checked = ''
    while(True):
        result, data = mail.search(None, '(FROM "When I Work")')
        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]
        typ, data = mail.fetch( latest_email_id, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                varSubject = msg['subject']
                print(varSubject)
                dayFree(varSubject)
                if varSubject != checked and dayFree(varSubject):
                    getShift(varSubject)
                checked = varSubject
        time.sleep(10)
    mail.close()

scanMail()
