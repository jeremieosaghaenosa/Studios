import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('bit.json', scope)
client = gspread.authorize(creds)

sheet = client.open('BitbucketRequest(Responses)').sheet1

# data = sheet.col_values(2)
# id = sheet.cell(2, 6)
# print(id)

container = set()
box = [2, 3, 4, 5, 6, 7]

# for i in range(sheet.row_count):
for i in box:
    id = sheet.cell(i, 2).value
    lastName = sheet.cell(i, 3).value
    firstName = sheet.cell(i, 4).value
    key = sheet.cell(i, 5).value
    credit_PF = sheet.cell(i, 6).value
    email = sheet.cell(i, 7).value

    if credit_PF == 'Credit':
        credit_PF = 'C'
    if credit_PF == 'Pass Fail':
        credit_PF = 'P'

    person = (str(id) + ',' + str(firstName) + '  ,' + str(lastName) + '  ,'
              + str(key) + ',E81,247  , ,' + credit_PF + ',' + str(email))

    container.add(person)

    with open('info.txt', 'a') as file:
        file.write(person)
        file.write("\n")

# print(container)

# with open('info.txt', 'a') as file:
#     file.write(person)
