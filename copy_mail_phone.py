import re
import pyperclip

reg_tel =  re.compile(r"(06|04|02|01|07)(-|.|\s)?(\d{2})(-|.|\s)?(\d{2})(-|.|\s)?(\d{2})(-|.|\s)?(\d{2})")
reg_mail = re.compile(r"(\w+)(.|_)?(\w+)(@)(\w+)(.|_)?(\w+)")

text = str(pyperclip.paste())

phoneNumber = reg_tel.findall(text)
mailAdress =  reg_mail.findall(text)

infoList = []

for num in phoneNumber:
    infoList.append(num[0] + num[2] + num[4] + num[6] + num[8])

for mail in mailAdress:
    infoList.append(mail[0] + mail[1] + mail[2] + mail[3] + mail[4] + mail[5] + mail[6])

pyperclip.copy("\n".join(infoList))
print("\n".join(infoList))