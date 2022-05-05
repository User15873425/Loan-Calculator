import math
import argparse


def nominal_interest(x):
    res = x / (12 * 100)
    return res


def number_of_payments(loan, payment, interest):
    res = math.ceil(math.log((payment / (payment - nominal_interest(interest) * loan)),
                    1 + nominal_interest(interest)))
    years = math.floor(res / 12)
    months = res - (years * 12)
    overpayment = int((payment * res) - loan)
    if months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")
    print(f"Overpayment = {overpayment}")


def payment_amount(loan, periods, interest):
    res = math.ceil(loan * (nominal_interest(interest) * pow((1 + nominal_interest(interest)),
                            periods)) / (pow((1 + nominal_interest(interest)), periods) - 1))
    overpayment = (res * periods) - loan
    print(f"Your annuity payment = {res}!")
    print(f"Overpayment = {overpayment}")


def loan_principal(payment, periods, interest):
    res = math.floor(payment / ((nominal_interest(interest)) * pow((1 + nominal_interest(interest)),
                     periods) / (pow((1 + nominal_interest(interest)), periods) - 1)))
    overpayment = int((payment * periods) - res)
    print(f"Your loan principal = {res}!")
    print(f"Overpayment = {overpayment}")


def differentiated_payments(loan, periods, interest):
    total = 0
    for current_month in range(periods):
        res = math.ceil((loan / periods) + nominal_interest(interest) * (loan - (loan
                        * ((current_month + 1) - 1)) / periods))
        print(f"Month {current_month + 1}: payment is {res}")
        current_month += 1
        total += res
    print(f"Overpayment = {total - loan}")


parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, required=True)
parser.add_argument('--principal', type=int, required=False)
parser.add_argument('--periods', type=int, required=False)
parser.add_argument('--interest', type=float, required=False)
parser.add_argument('--payment', type=float, required=False)
args = parser.parse_args()

if args.payment is None and args.principal is None or args.payment is None and args.periods is None or args.payment is None and args.interest is None or args.periods is None and args.interest is None:
    print("Incorrect parameters.")
elif args.type == "diff" and args.interest is None:
    print("Incorrect parameters.")
elif args.payment is None and args.type == 'annuity':
    payment_amount(args.principal, args.periods, args.interest)
elif args.principal is None and args.type == 'annuity':
    loan_principal(args.payment, args.periods, args.interest)
elif args.periods is None and args.type == 'annuity':
    number_of_payments(args.principal, args.payment, args.interest)
elif args.payment is None and args.type == 'diff':
    differentiated_payments(args.principal, args.periods, args.interest)
