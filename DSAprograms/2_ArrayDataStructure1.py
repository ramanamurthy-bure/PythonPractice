'''
Exercise: Array DataStructure
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and got a refund of 200$.Make a correction to
your monthly expense list based on this.
'''

MonthlyExp = [['January',2200],['February',2350],['March',2600],['April',2130],['May',2190]]
extraDoller = int(MonthlyExp[1][1])-int(MonthlyExp[0][1])
print(extraDoller)

totalExpInFirstQrtr = int(MonthlyExp[0][1]) + int(MonthlyExp[1][1]) + int(MonthlyExp[2][1])
print(totalExpInFirstQrtr)

MonthlyExp.append(['June',1980])
print(MonthlyExp)







