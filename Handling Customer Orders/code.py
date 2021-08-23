# Libraries Imported
import csv
from os.path import *

# List Declaration goes here
itemNumList = []
itemDescList = []
itemPriceList = []
cNumList = []
cNameList = []
cBalanceList = []
cPasswordList = []

# take customer info file path and read it
fileName = input()
with open(fileName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # break each line of customer info file and append each info to their relevant lists
    for row in csv_reader:
        cNumList.append(row[0])
        cNameList.append(row[1])
        cBalanceList.append(row[2])
        cPasswordList.append(row[3])

# creates dictionary from cNumList as keys with values 0
totalOrdered = dict.fromkeys(cNumList, 0)

# take customer info file path and read it
fileName = input()
with open(fileName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # break each line of customer info file and append each info to their relevant lists
    for row in csv_reader:
        itemNumList.append(row[0])
        itemDescList.append(row[1])
        itemPriceList.append(row[2])

# checks for existence of orders.txt file
while(True):
    transactions = input()
    if(isfile(transactions)):
        break
    else:
        print("Please Enter Valid Path!")

price = 0
with open(transactions) as trans_file:
    for transaction in trans_file:
        if (transaction.startswith("CO")):  # if a line of order starts with CO, it means a new customer
            customerNum = transaction[2:7]  # takes customerNum out of the line
            if customerNum in cNumList:  # checks for customer verification
                ordersPrice = 0
                numOfOrders = int(transaction[7:10])
                ds = transaction[10]
                date = transaction[11:].rstrip()
                date = date[:2] + "/" + date[2:4] + "/" + date[4:] # converts date to dd/mm/yyyy format
                lineNumber = 1

                # to be displayed in both detailed and summary receipt orders
                print("{:>10}:{:>15}".format("Order Date", date))
                customerName = cNameList[cNumList.index(customerNum)]
                print("{:>10}:{:>15}{:>8}{}\n".format("Customer", customerNum, " ",customerName))
                # only to be displayed for detailed orders receipt
                print("1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")
                if (ds == "D"):
                    print("{: >2}{:>3}{:<18}{:<28}{:>10}{:>11}{:>11}{:>4}{:>10}".format("Ln#", " ","Item #",
                                                                                                    "Item Description",
                                                                                                    "Req Date".center(10), "Qty",
                                                                                                    "Price", " ", "Total"))
                # iterate until next customer arrives
                for i in range(numOfOrders):
                    itemOrder = trans_file.readline()
                    # split the order info into 3 parts and assign to variables
                    trans_list = itemOrder.split("^")
                    qty = int(trans_list[0])
                    itemNum = trans_list[1]
                    ordDate = trans_list[2].rstrip()
                    reqDate = ordDate[:2] + "/" + ordDate[2:4] + "/" + ordDate[4:]
                    index = -1

                    try:
                        index = itemNumList.index(itemNum)
                    except:
                        pass
                    if itemNum not in itemNumList:
                        price = 0
                        itemDesc = "*** Item not found ***"
                    else:
                        price = float(itemPriceList[index])
                        itemDesc = itemDescList[index]

                    totalPrice = price * qty  # total price is calculated
                    ordersPrice += totalPrice
                    # display item details, only for detailed receipts
                    if (ds == "D"):
                        print("{: >2}{:>4}{:<18}{:<28}{:>10}{:>11}{:>11}{:>4}{:>10}".format(str(lineNumber).rjust(2)," ",
                                                                                                          itemNum,
                                                                                                          itemDesc,
                                                                                                          reqDate, qty,
                                                                                                          format(price,".2f"),"$",
                                                                                                          format(totalPrice,".2f")))
                        lineNumber += 1

                # order price calculation
                index = cNumList.index(customerNum)
                accountBalance = float(cBalanceList[index])
                totalDue = accountBalance + ordersPrice
                cBalanceList[index] = totalDue

                # display total order price and due amounts in both detail and summary receipts
                if(ds=="D"):
                    print()
                print("{:>66}{:>13}:{:>18}".format(" ", "Total Ordered", format(ordersPrice,".2f")))
                print("{:>66}{:>13}:{:>18}\n".format(" ","Balance", format(accountBalance,".2f")))
                print("{:>66}{:>13}:{:>18}".format(" ","Total Due", format(totalDue, ".2f")))
                print("---------------")

            else:  # if customer is not in csv file then exclude his transactions
                print("Customer number {} is invalid.".format(customerNum))
                print("---------------")
        elif transaction == "EOF": # when EOF occurs break through loop
            break
