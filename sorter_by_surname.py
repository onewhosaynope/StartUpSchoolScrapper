from bs4 import BeautifulSoup
import helper_surname
import os
import sys

with open(os.path.join(sys.path[0], "result.html"), 'rb') as html:
    soup = BeautifulSoup(html, 'html.parser')

# Create directory
dirName = 'bySurname'
 
try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

suffixes = ['ov', 'ova', 'aya', 'ev', 'eva', 
    'in', 'ina', 'sky', 'skaya', 'ykh', 'qızı',
    'yan', 'ian',
    'vych', 'chuk', 'enko', 'ko', 'ka', 'shyn', 'uk'] 

for suffix in suffixes:
    print('===========================SUFFIX {}==============================='.format(suffix.upper()))
    count = 0
    filename = 'bySurname\\result_{}.html'.format(suffix.upper())
    with open(filename, "w", encoding="utf-8") as file:
        print('created file named: ' + filename)
        file.write('<link rel="stylesheet" href="https://www.startupschool.org/packs/css/application-b8935dc9.css">')
        print('addes styles to ' + filename)
        for company in soup(class_='directory-company-profile'):
            for founder in company.find_all(class_ ='founder'):
                done = False
                founder_name = founder.find(class_='name')
                print('Founder: ' + founder_name.text.rstrip())
                if helper_surname.check_custom(founder_name.text.rstrip(), suffix):
                    file.write(company.prettify())
                    count = count + 1
                    done = True
                    break
                if done:
                    break
        print("Totall companies: " + str(count))
        file.close()