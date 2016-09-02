'''
Created on Aug 28, 2016

@author: Adam Garcia
'''
import requests
import sys
import somecomfort
from argparse import RawDescriptionHelpFormatter, ArgumentParser

__version__ = 0.1


def get_power_output(ip, port, user, password):
    r = requests.get('http://{}:{}/arraystatus.xml'.format(ip, port),
                     auth=(user, password))
    output_index = r.text.find('<OutputKWH>') + 11
    power_output = r.text[output_index:r.text.find('<', output_index)]
    return power_output


def main(argv=None):
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)
    desc = "Script to adjust honeywell thermostats based on solar output"
    parser = ArgumentParser(description=desc,
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("ip", metavar="IP",
                        help="IP address of solar array data")
    parser.add_argument("port", metavar="PORT",
                        help="Port for server of solar array data")
    parser.add_argument("user", metavar="HONEYWELL_USERNAME",
                        help="Honeywell portal username")
    parser.add_argument("password", metavar="HONEYWELL_PASSWORD",
                        help="Honeywell portal password")
    parser.add_argument("power", metavar="SOLAR_POWER", default=20000
                        help="The minimum wattage produced by panels to increase AC")
    parser.add_argument("default_ac", metavar="AC_DEFAULT_SETPOINT", default=72
                        help="The default temp set point")
    parser.add_argument("low_ac", metavar="LOWEST_TEMP", default=68,
                        help="The lowest temp to set thermos when solar output is high")
    parser.add_argument('-V', '--version', action='version',
                        version=__version__)

    args = parser.parse_args()
    ip = args.ip
    port = args.port
    user = args.user
    password = args.password
    min_power = args.power
    default_ac = args.default_ac
    low_ac = args.low_ac
    somecomfort.
    current_power = get_power_output(ip, port, user, password)
    if current_power > min_power:
        #TODO SET THE LOW AC SETTING USING SOMECOMFORT HERE
        pass

if __name__ == "__main__":
    sys.exit(main())
    