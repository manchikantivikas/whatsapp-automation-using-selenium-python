import openpyxl as excel
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime
from tkinter import *
from tkinter import filedialog

root=Tk()
root.withdraw()


moblie_no_list = []
# list of phone number can be of any length
print("Select a list of phone numbers to send messages(in excel format)")
sleep(1)
l=filedialog.askopenfilename()
file = excel.load_workbook(l)
sheet = file.active
firstCol = sheet['A']

for cell in range(len(firstCol)):
    contact = str(firstCol[cell].value)
    contact="91"+contact
    #print(contact)
    c1=contact[0:12]
    moblie_no_list.append(c1)
# get mobile no from excel file file
print(moblie_no_list)

def timescheduling(imgw,docw):

    if imgw=="yes":
        hour = datetime.datetime.now().hour
        if(hour >= 5 and hour <= 11):
            text="goodmorning"
            print("Select goodmorning image")
            sleep(2)
            im=filedialog.askopenfilename()
        elif (hour >= 21 and hour <= 23):
            text="goodnight"
            print("Select goodafternoon image")
            sleep(2)
            im=filedialog.askopenfilename()
        else:
            text="how are you?"
            print("Select hope ypu are doing well")
            sleep(2)
            im=filedialog.askopenfilename()
    elif imgw!="yes":
        im='null'
        text='null'
    if docw=="yes":
        print("Select document")
        sleep(2)
        doc=filedialog.askopenfilename()
        doctext="Hey folk!,Check the document."
    elif docw!="yes":
        doc='null'
        doctext='null'
    print(im,doc,text,doctext)
    return im,doc,text,doctext

def image(im):
    clipButton = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
    clipButton.click()
    sleep(2)
    driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[3]/div[1]/div[2]/span[1]/div[1]/div[1]/ul[1]/li[1]/button[1]/input[1]").send_keys(im)
    sleep(3)
    whatsapp_send_button = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]/div[1]/span[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/span[1]')
    sleep(2)
    whatsapp_send_button.click()
    sleep(3)
    
def document(doc):
    clipButton = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
    clipButton.click()
    sleep(2)
    driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[3]/div[1]/div[2]/span[1]/div[1]/div[1]/ul[1]/li[3]/button[1]/input[1]").send_keys(doc)    
    sleep(3)
    whatsapp_send_button = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]/div[1]/span[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/span[1]')
    sleep(2)
    whatsapp_send_button.click()
    sleep(3)

def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)
    
def send_whatsapp_msg(phone_no,im,doc,text,imgw,docw,doctext):


    driver.get(
        "https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no)
    )

    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass
    
    if(imgw=='yes'):
        element_presence(
           By.XPATH,
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',
         30)
        txt_box = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    
        txt_box.send_keys(text)
        txt_box.send_keys("\n")
        image(im)
    sleep(2)
    if(docw=='yes'):
        element_presence(
           By.XPATH,
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',
         30)
        txt_box = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    
        txt_box.send_keys(doctext)
        txt_box.send_keys("\n")
        document(doc)
        
imgw=input("Want to send image(if yes then enter 'yes' else 'no')")
docw=input("want to send document(if yes then enter 'yes' else 'no')")
im,doc,text,doctext=timescheduling(imgw,docw)
driver = webdriver.Chrome('D:\chromedriver')
driver.get(path of driver)
sleep(10)
for moblie_no in moblie_no_list:
    try:
        send_whatsapp_msg(moblie_no,im,doc,text,imgw,docw,doctext)
    except Exception as e:
        sleep(10)
print("Task completed")
driver.quit()
    
    