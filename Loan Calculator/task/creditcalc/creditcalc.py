from math import ceil, log, pow, floor
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=['annuity', 'diff'])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if not args.type:
    print("Incorrect parameters")
else:
    type_arg = args.type
    if type_arg == 'diff':
        if args.payment:
            print("Incorrect parameters")
        else:
            principal = int(args.principal)
            interest_rate = float(args.interest)
            periods = int(args.periods)

            interest = (interest_rate / 100) / 12

            sum_diff = 0
            for m in range(1, periods + 1):
                diff_months = ceil((principal / periods) + (interest * (principal - ((principal * (m - 1)) / periods))))

                sum_diff += diff_months
                print("Month {}: payment is {}".format(m, diff_months))

            print()
            over_payment = abs(principal - sum_diff)
            print("Overpayment = {}".format(over_payment))

    else:
        periods = 0
        if args.periods:
            periods = int(args.periods)

        interest_rate = 0.0
        if args.interest:
            interest_rate = float(args.interest)
        else:
            print("Incorrect parameters")
            exit()
        interest = (interest_rate / 100) / 12

        if args.payment and not args.principal:
            payment = int(args.payment)
            principal = floor(payment / (interest * pow(1 + interest, periods) / (pow(1 + interest, periods) - 1)))

            print('Your loan principal = {}!'.format(principal))

            overpayment = abs(principal - (periods * payment))
            print("Overpayment = {}".format(overpayment))

        elif not args.payment and args.principal:
            principal = int(args.principal)

            monthly_payment = ceil(
                principal * (interest * pow(1 + interest, periods) / (pow(1 + interest, periods) - 1)))

            print('Your annuity payment = {}!'.format(monthly_payment))

            overpayment = abs((monthly_payment * periods) - principal)

            print("Overpayment = {}".format(overpayment))
        else:
            payment = int(args.payment)
            principal = int(args.principal)

            periods = ceil(log(payment / (payment - interest * principal), 1 + interest))

            year = periods // 12
            month = periods % (year * 12)

            if year > 0 and month > 0:
                print("It will take {} years and {} months to repay this loan!".format(year, month))
            elif year == 0 and month > 0:
                print("It will take {}  months to repay this loan!".format(month))
            else:
                print("It will take {} years to repay this loan!".format(year))

            overpayment = abs((year * 12 * payment + month * payment) - principal)

            print("Overpayment = {}".format(overpayment))
