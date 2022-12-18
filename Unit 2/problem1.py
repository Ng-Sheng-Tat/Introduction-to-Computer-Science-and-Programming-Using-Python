### problem 1

### Testing function
def payFun(balance,annualInterestRate,monthlyPaymentRate):
    
    monthlyInterestRate = annualInterestRate/12.0
    totalPay = 0
    
    for i in range(1,13):
        
        minMonPay = balance * monthlyPaymentRate 
        totalPay += minMonPay
        balance = balance - minMonPay 
        balance = balance * (1 + monthlyInterestRate)

        print('Month: ' + str(i), end=" ")
        # print('Minimum monthly payment: ' +  '%.2f' % minMonPay) 
        print('Remaining balance: ' + '%.2f' % balance )
    print('Total paid: ' + '%.2f' % totalPay)
    print('Remaining balance: ' + '%.2f' % balance)

payFun(484, 0.2, 0.04)

### Answer Submissions
monthlyInterestRate = annualInterestRate/12.0
totalPay = 0

for i in range(1,13):

    minMonPay = balance * monthlyPaymentRate 
    totalPay += minMonPay
    balance = balance - minMonPay 
    balance = balance * (1 + monthlyInterestRate)

print('Remaining balance: ' + '%.2f' % balance)