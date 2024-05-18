price = 108.65
#ask customer to enter Amt. or Quantity
choice = input('Enter Q for Quantity Required.A for Amount')
if choice == 'A':
    Amt = float(input('Enter Amount in whole no :'))
    Quantity = Amt/price
    print('Quantity dispensed',Quantity)
elif choice == 'Q':
    Quantity = float(input('Enter Quantity in whole no :'))
    Amt = Quantity*price
    print('Amount to be paid:',Amt)





