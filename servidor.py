import json
import socket
HOST = ''              # Endereco IP do Servidor
PORT = 30000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
contador=0
user="lucas"
password="1234"
while True:
    con, cliente = tcp.accept()
    con.send("ack")
    msg=con.recv(1024)
    users=msg.split(" ")
    if(users[0]==user and users[1]==password):
		con.send("500")
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
    if(users[0]!=user or users[1]!=password):
		con.send("501")
		tcp.close()
		exit()
		
		
