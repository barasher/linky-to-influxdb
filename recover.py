import argparse
import subprocess
import sys
import datetime
from dateutil.relativedelta import relativedelta

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--date', required=True, help='Day (dd/mm/aaaa)')
    parser.add_argument('-c', '--count', required=True, help='Day number')
    args = parser.parse_args()

    curDate = datetime.datetime.strptime(args.date, '%d/%m/%Y')
    for x in range(int(args.count)):
      subprocess.run(["./innerRecover.sh", curDate.strftime('%d/%m/%Y')])
      curDate = curDate + relativedelta(days=1)

if __name__ == '__main__':
    sys.exit(main())
