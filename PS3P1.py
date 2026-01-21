#Input phase
STSym= input("Enter Stock ticker symbol: ")
ShrNum= float(input("Enter number of shares: "))
CPrShr= float(input("enter Cost per share: "))
#Process phase
InvAmnt=(ShrNum*CPrShr)
#Output phase
print("Stock Ticket: ", STSym)
print("Investment Amount: ",InvstAmnt)