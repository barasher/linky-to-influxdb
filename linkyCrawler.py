import argparse
import sys
import json
import linkyClient
import os
import datetime
from dateutil.relativedelta import relativedelta


def main():
    """Main function"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', required=True, help='Enedis username')
    parser.add_argument('-p', '--password', help='Enedis password. Can be read form LTI_LINKY_PASS Environment')
    parser.add_argument('-d', '--date', required=False, help='Day (dd/mm/aaaa)')
    args = parser.parse_args()
    if args.password:
        LTI_LINKY_PASS = args.password
    else:
        LTI_LINKY_PASS = os.getenv('LTI_LINKY_PASS')
    start = datetime.date.today() - relativedelta(days=1)
    try:
        if args.date:
            start = datetime.datetime.strptime(args.date, '%d/%m/%Y')
    except Exception as exp:
        print(exp)
        return 1
    end = start + relativedelta(days=1)

    client = linkyClient.LinkyClient(args.username, LTI_LINKY_PASS)

    try:
        client.login()
        client.get_data_per_period(client.PERIOD_HOURLY, start, end)
    except BaseException as exp:
        print(exp)
        return 1
    finally:
        client.close_session()
    print(json.dumps(client.get_data(), indent=2))


if __name__ == '__main__':
    sys.exit(main())
