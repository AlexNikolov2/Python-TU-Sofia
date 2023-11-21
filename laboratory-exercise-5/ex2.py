def calculate_tax_rate(income):
    
    if (income <= 10000):
            tax_rate = 0.1
    elif (income > 10000 and income <= 20000):
            tax_rate = 0.15
    elif (income > 20000 and income <= 30000):
            tax_rate = 0.2
    else:
            tax_rate = 0.25
    return tax_rate

def print_tax_info(income, tax_rate):
    tax = int(income) * tax_rate
    print('income', income)
    print('tax rate', tax_rate)
    print('tax', tax)
income = float(input('set income'))
print_tax_info(income, calculate_tax_rate(income))
        
        
            