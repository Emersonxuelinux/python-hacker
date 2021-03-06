# coding=UTF-8
import optparse
import socket

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        print('[+]%d/tcp open' % tgtPort)
        print('[+]' + str(results))
        connSkt.close()
    except:
        print('[-]%d/tcp close' % tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIp = socket.gethostbyname(tgtHost)
    except Exception as e:
        print("[-] Cannot resolve '%s' " % tgtHost)
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIp)
        print('\n[+] Scan Results for:%s' % tgtName[0])
    except:
        print('\n[+] Scan Results for:%s' % tgtIp)
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port' + str(tgtPort))
        connScan(tgtHost, int(tgtPort))

def main():
    parser = optparse.OptionParser('usage%prog -H <target host> -p <target host>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest = 'tgtPort', type='int', help='specify target port')
    options, args = parser.parse_args()
    if options.tgtHost is None or options.tgtPort is None:
        print(parser.usage)
        exit(0)
    else:
        tgtHost = options.tgtHost
        tgtPort = options.tgtPort
    args.append(tgtPort)
    portScan(tgtHost, args)

if __name__ == '__main__':
    main()
