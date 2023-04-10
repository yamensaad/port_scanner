import socket

target = "127.0.0.1"


def portscan(port):
    try:
        sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        sock.connect( (target, port) )
        return True
    except:
        return False


print( portscan( 100 ) )

for port in range( 1, 1042 ):
    result = portscan( port )
    if result:
        print( "port {} is opened".format( port ) )
    else:
        print( "port {} is closed".format( port ) )
