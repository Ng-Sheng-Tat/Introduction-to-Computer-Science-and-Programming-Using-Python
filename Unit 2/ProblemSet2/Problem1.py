monthlyInterestRate = annualInterestRate/12.0
totalPay = 0

for i in range(1,13):

    minMonPay = balance * monthlyPaymentRate 
    totalPay += minMonPay
    balance = balance - minMonPay 
    balance = balance * (1 + monthlyInterestRate)

print('Remaining balance: ' + '%.2f' % balance)