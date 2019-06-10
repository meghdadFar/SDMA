

def calculate_monthly(sum, num_months, int_rate):
    yearly_interest = sum*float(int_rate/100)
    overall_interest = yearly_interest*(num_months/12)
    monthly = (sum + overall_interest)/float(num_months)
    return monthly, overall_interest


def print_all(sum):

    print '\n--------------------------------------'
    print '\t\t\t', sum, '\t\t'
    print '--------------------------------------\n'

    five_monthly, five_overall = calculate_monthly(sum, 60, 3.21)
    four_monthly, four_overall = calculate_monthly(sum, 48, 3.21)
    three_monthly, three_overall = calculate_monthly(sum, 36, 3.21)

    print 'months \t monthly \t overall_interest'

    print '60 \t\t ', '{0:.2f}'.format(five_monthly), '\t\t', '{0:.2f}'.format(five_overall)

    print '48 \t\t ', '{0:.2f}'.format(four_monthly), '\t\t', '{0:.2f}'.format(four_overall)

    print '36 \t\t ', '{0:.2f}'.format(three_monthly), '\t\t', '{0:.2f}'.format(three_overall)



print_all(8000)
print_all(9000)
print_all(10000)
print_all(11000)
print_all(12000)