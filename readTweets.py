
from collections import defaultdict
import twitter
import csv


# Define user
users={
    'name':[None]*twitter.getNum(),
    'tweetPerHour': [None]*twitter.getNum(),
    'numOfFollowers':[None]*twitter.getNum(),
    'numOfRetweets':[None]*twitter.getNum(),
    'date':[None]*twitter.getNum(),
    'hour': [None]*twitter.getNum(),
    'tweets': [None]*twitter.getNum()
}

# Pull from file
list
file=twitter.getFile()
with open(file,encoding='utf-8') as file:


    reader = csv.reader(file, delimiter=' ')



    i=0
    for row in reader:
        list=row


        users['name'][i]=list[0]
        users['tweets'][i]=str(list[3]).encode('ascii','ignore')
        users['numOfFollowers'][i] = int(list[len(list)-2])
        users['numOfRetweets'][i] = int(list[len(list)-1])
        users['date'][i] = list[1]
        s = users['date'][i]
        users['hour'][i] = int(s[13]+s[14])
        users['tweetPerHour'][i] = 0

        i += 1




def getMin(list):
    mi = list[0]
    for i in range(0,len(list)):
        if mi > list[i]:
             mi = list[i]
    return mi

def getMax(list):
    ma = list[0]
    for i in range(0,len(list)):
        if ma < list[i]:
             ma = list[i]
    return ma

def insertion_sort(array, array2, array3, array4, array5, array6,array7):
    for slot in range(1, len(array)):
        value = array[slot]
        value2 = array2[slot]
        value3 = array3[slot]
        value4 = array4[slot]
        value5 = array5[slot]
        value6 = array6[slot]
        value7 = array7[slot]

        test_slot = slot - 1
        while test_slot > -1 and array[test_slot] < value:
            array[test_slot + 1] = array[test_slot]
            array2[test_slot + 1] = array2[test_slot]
            array3[test_slot + 1] = array3[test_slot]
            array4[test_slot + 1] = array4[test_slot]
            array5[test_slot + 1] = array5[test_slot]
            array6[test_slot + 1] = array6[test_slot]
            array7[test_slot + 1] = array7[test_slot]

            test_slot = test_slot - 1
        array[test_slot + 1] = value
        array2[test_slot + 1] = value2
        array3[test_slot + 1] = value3
        array4[test_slot + 1] = value4
        array5[test_slot + 1] = value5
        array6[test_slot + 1] = value6
        array7[test_slot + 1] = value7




length=(len(users['numOfFollowers']))



from collections import Counter

# Part B
insertion_sort(users['hour'],users['name'],users['date'],users['tweetPerHour'],users['numOfRetweets'],users['numOfFollowers'], users['tweets'])
minhour=getMin(users['hour'])
maxhour=getMax(users['hour'])
frequentnameshour=Counter(users['name'])


with open('tweets_perhour.txt','w') as text:

    for elm in range(length):
        # text.write(str(elm + 1) + '. ' + str(users['name'][elm]) + ' ' + str(frequentnames[users['name'][elm]]) + '\n')
        text.write(str(elm + 1) + '. hour: ' + str(users['hour'][elm]) + ' ' + str(users['name'][elm]) + ' ' + str(frequentnameshour[users['name'][elm]]) + '\n')




# Part C
insertion_sort(users['numOfFollowers'],users['name'],users['date'],users['tweetPerHour'],users['numOfRetweets'],users['hour'], users['tweets'])
with open('most_followers.txt','w') as text:

    for elm in range(length):
        text.write(str(elm+1) + '. ' + users['name'][elm] + ' ' + str(users['numOfFollowers'][elm]) + '\n')


# Part D
insertion_sort(users['numOfRetweets'],users['name'],users['date'],users['tweetPerHour'],users['numOfFollowers'],users['hour'], users['tweets'])
with open('most_retweets.txt','w') as text:

    for elm in range(length):
        text.write(str(elm+1) + '. ' + users['name'][elm] + ': ' + str(users['tweets'][elm])[1:] + ' ' + str(users['numOfRetweets'][elm]) + '\n')


# Part A
names=users['name']

frequentnames=Counter(names)

insertion_sort(frequentnames,users['name'],users['date'],users['tweetPerHour'],users['numOfRetweets'],users['hour'], users['tweets'])
with open('most_frequent.txt','w') as text:

    for elm in range(length):
        text.write(str(elm+1) + '. ' + str(users['name'][elm]) + ' ' + str(frequentnames[users['name'][elm]]) +  '\n')

