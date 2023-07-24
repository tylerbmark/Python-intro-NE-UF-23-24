# Self-help on merging formats

# by yours truly
import csv

'''First you must start by reading the files,
I'm separaing these into two different modules for ease of reading'''
def readcsv(csvfile):
    titles = []
    topics = []
    timestamp = []
    gender = []
    with open(csvfile, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            '''I dont believe the .strip function is entirely necessary within ya'lls files 
            because she made them a way where it would remain unneeded, but if you were not to have
            such luxury it can help get rid of needless spacing issues within txt files.'''
            name = ' '+ row[2].strip()[0]+ '. '+ row[3].strip()
            title = row[0].strip() + '.' + name
            titles.append(title)
            timestamp.append(row[5].strip())
            gender.append(row[1].strip())
            topics.append(row[4].strip())
    return titles,timestamp,gender,topics
'''It's not too terrible, the portion of the csv is really where you parse the data you need
as you need it'''
def read_txt(txtfile):
    with open(txtfile, 'r') as file:
        template = file.read()
    return template

def merge(csv,txt):
    memos = []
    topic_ = []
    titles,timestamp,gender,topics = readcsv(csv)
    template = read_txt(txt)
    '''Naturally you can use nested for loops to get the same result,
    however the zip function is made to do exactly what she's asking for in many regards as it can
    process multiple lists/tuples/str formations. I'd suggest looking it up and adding it
    to your coding tool kit'''
    for titles,timestamp,gender,topics in zip(titles,timestamp,gender,topics):
        mergedmemo = template.format(name=titles, timestamp=timestamp,gender=gender,topic=topics)
        memos.append(mergedmemo)
        topic_.append(topics)
    return memos,topic_

def main():
    print('Company memos:\n ')
    csv = 'memo.csv'
    txt = 'memo_temp.txt'
    memos,topics = merge(csv,txt)
    repeat = 'y'
    while repeat.lower() == 'y':
        '''As you can see, enumerate is also another useful function, it allows you to use the
        indexing value as a value under the fourloop instead of just an index'''
        for i,topic in enumerate(topics):
            print(f'{i+1}. {topic}')
        choice = input('Which memo would you like to read?')
        try:
            choice = int(choice)
            if 1 <= choice <= len(memos):
                print('---' * 25)
                print(memos[choice - 1])
                print('---' * 25)
            else:
                print('Invalid choice!')
        except ValueError:
            print('Invalid choice! Input must be a number.')
        repeat = input('Would you like to look at another memo ? (y/n): ')


main()