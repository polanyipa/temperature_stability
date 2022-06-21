import socket
SCU_IP = "172.22.2.113"
SCU_PORT = 10100
UDP_MAX_TX_SIZE = 32768


def read(s, cmnd):
    """ Send command cmd to MDBE and get the answer.
        If there is no answer or error -> return False
        otherwise True.
    """
    s.send(cmnd)
    raw_data = []
    data = s.recv(UDP_MAX_TX_SIZE)
    if not data:
        print('ERROR: no data received')
        return False
    if data.find(b'[ERR]') != -1:
        print(data)
        return False
    return data


if __name__ == '__main__':

    sock_arg = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_arg.bind(('', SCU_PORT))
    sock_arg.settimeout(5)
    try:
        sock_arg.connect((SCU_IP, SCU_PORT))
    except socket.error:
        print(str('Could not connect to IP: {0} at port {1}').format(SCU_IP, SCU_PORT))
        sys.exit(0)

    cmd = b'scu.version'
    print(read(sock_arg, cmd))

    sock_arg.close()
