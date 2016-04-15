import os
import subprocess
import datetime
import sys
import argparse

def main():
    opts = parse_argus()
    LOG_HOME = '/Users/pc/log/disk/'
    FILE = LOG_HOME+'log.txt'
    p = subprocess.Popen(['/usr/local/sbin/smartctl','-a','/dev/disk1','-s','on'],stdout=subprocess.PIPE)
    c = p.communicate()
    log_file = open(FILE,'w')
    os.chdir(LOG_HOME)
    log_file.writelines(c[0])
    os.system('git diff -w')
    log_file.close()
    today = datetime.date.today()
    note = str(today.year)+str(today.month)+str(today.day)
    if opts[0] != 'n' :
        os.system('git commit -am %s'%(note))
        
    #print c[0]
    #print log_file.read()

def parse_argus():
    parser = argparse.ArgumentParser(description='sum the integers at the command line')
    parser.add_argument('strs', metavar='str', nargs='+', type=str, help='an integer to be summed')
    parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'), help='the file where the sum should be written')
    args = parser.parse_args()
    return args.strs[0]

main()
