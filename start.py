#!/usr/bin/env python

import listener
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="Target ip address")
    parser.add_option("-p", "--port", dest="port", help="Target port address")
    (options, arguments) = parser.parse_args()
    if not options.ip:
        parser.error("\n[-] Please specify ip addresses, use --help for more info.")
    elif not options.port:
        parser.error("\n[-] Please specify port addresses, use --help for more info.")
    return options

options = get_arguments()

target_ip = options.ip
target_port = options.port

my_listener = listener.Listener(target_ip, int(target_port))
my_listener.run()
