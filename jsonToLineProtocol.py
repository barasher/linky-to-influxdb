import argparse
import json
import os
import sys
import datetime
import pytz

RET_OK=0
RET_CONF_FAILURE=1
RET_EXEC_FAILURE=2

parisTz = pytz.timezone('Europe/Paris')

def buildLine(strDate, amount, location):
    parsedDate = parisTz.localize(datetime.datetime.strptime(strDate, '%d/%m/%Y %H:%M'))
    return "linky,location={} conso={} {}".format(location, amount, round(parsedDate.timestamp() * 1000000000))

def convert(sourcePath, location, refDate=None):
    try: 
        with open(sourcePath) as source:
            data = json.load(source)
            if refDate is None:
                d = datetime.datetime.now() - datetime.timedelta(days=1)
            else:
                d = refDate
            d.replace(second=0, microsecond=0)
            strD = d.strftime('%d/%m/%Y')
            for curHour in data['hourly']:
                strH = "{} {}".format(strD, curHour['time'])
                print("{}".format(buildLine(strH, curHour['conso'], location)))
    except IOError as e:
        print("Error when opening source file: {}", e)
        return RET_EXEC_FAILURE
    except json.JSONDecodeError as e:
        print("Error when decoding source file: {}", e)
        return RET_EXEC_FAILURE
    finally:
        source.close()
    return RET_OK

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', required=True, help='Source file')
parser.add_argument('-l', '--location', required=True, help='Location identifier')
parser.add_argument('-d', '--date', required=False, help='Concerned date (format dd/mm/yyyy)')
args = parser.parse_args()

if not os.path.exists(args.source):
    print("Source '{}' does not exist".format(args.source))
    sys.exit(RET_CONF_FAILURE)

if args.date is not None:
    d = datetime.datetime.strptime(args.date, "%d/%m/%Y")
else:
    d=None
ret=convert(args.source, args.location, d)
sys.exit(ret)
