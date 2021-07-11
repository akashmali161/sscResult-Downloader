import os
import requests
import base64
import json
name = input("enter your name")
year = input("enter your passing year")
roll_number = input("enter your seat number")
session = 'MAR'
total_marks = input("enter your marks")
os.chdir(r"C:\Users\Akash Mali\Desktop\demo")
url = f"https://mahadbtmahait.gov.in/Common/SSC_HSC_Service?Class=SSC&Passingyear={year}&rollnumber={roll_number}&exsession={session}&totalmarks={total_marks}"
res = requests.get(url)

data = res.text

j = json.loads(data)
q = j.get("serviceResponse")
e = q.get("DocContent")

# print(e)

with open(f"{name}_ssc_result.pdf",'wb') as file:
    file.write(base64.b64decode(e))
    print("your result genrated successfully!...")




# for i in q:
#     print()
#     print(i.get('DocContent'))