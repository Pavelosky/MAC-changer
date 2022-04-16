#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():

    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='interface to change its Mac address')
    parser.add_option('-m', '--mac', dest='new_mac', help='new MAC address')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error('[-] Specify Interface, use --help for info')
    elif not options.new_mac:
        parser.error('[-] Specify a new mac, use --help for more info')
    return options

def change_mac(interface, new_mac):
    print('[+] Changing MAC address for ' + interface + ' to ' + new_mac)



    # THIS FORMAT IS NOT SAFE
    # subprocess.call("ifconfig " + interface + " down", shell=True)
    # subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    # subprocess.call("ifconfig " + interface + " up", shell=True)
    
    # List format is harder to hack []
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])



def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print('Sorry no mac address')

options = get_arguments()

current_mac = get_current_mac(options.interface)

print('yo' + str(current_mac)) #this is called casting (object turned to string)

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:

    print('[+] MAC adress was successfully changed to ' + current_mac)

else:

    print('[-] MAC address not changed, try again.')
