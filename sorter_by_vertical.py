from bs4 import BeautifulSoup
import helper_surname
import os
import sys

with open(os.path.join(sys.path[0], "result.html"), 'rb') as html:
    soup = BeautifulSoup(html, 'html.parser')

# Create directory
dirName = 'byVertical'
 
try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

verticals = [
    'Agriculture / Agtech', 'Artificial Intelligence','Augmented Reality', 
    'B2B', 'Biomedical', 'Biotech', 'Blockchain',
    'Community', 'Consumer', 'Crowdfunding',
    'Developer Tools', 'Diversity', 'Drones',
    'E-commerce','Education', 'Energy', 'Enterprise', 'Entertainment', 'Esports / Online Gaming',
    'Financial / Banking',
    'Government',
    'Hardware', 'Healthcare',
    'International Market',
    'Jobs',
    'Marketplace', 'Media / Advertising', 'Moonshots / Hard Tech',
    'Nonprofit',
    'Robotics',
    'Science', 'Security', 'Sport / Fitness',
    'Transportation', 'Travel',
    'Virtual Reality',
    'Other']

totall_companies = 0
# итерация по каждому из направлений
for vertical in verticals:
    print('===========================vertical {}==============================='.format(vertical.upper()))
    count = 0
    # генерация файла для записи результатов по направлению
    filename = 'byVertical\\result_{}.html'.format(vertical.upper().replace(' ', '').replace('/', ''))
    with open(filename, "w", encoding="utf-8") as file:
        print('created file named: ' + filename)
        # подключение стилей
        file.write('<link rel="stylesheet" href="https://www.startupschool.org/packs/css/application-b8935dc9.css">')
        print('addes styles to ' + filename)
        # итерация по каждой из компаний
        for company in soup(class_='directory-company-profile'):
            company_vertical = company.find(class_='vertical').text.lstrip().rstrip()
            # если направление компании совпало - запись в файл
            if company_vertical == vertical:
                file.write(company.prettify())
                count = count + 1
        print("Totall companies: " + str(count))
        totall_companies = totall_companies + count
        file.close()
print(totall_companies)