import socket
HOST = ''              # Endereco IP do Servidor
PORT = 50000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
contador=0
while True:
    con, cliente = tcp.accept()
    con.send("ack")
    print 'Concetado por', cliente
    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg
        contador=contador+1
        con.send(str(contador))
    print 'Finalizando conexao do cliente', cliente
    con.close()
    exit()
