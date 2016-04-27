import socket
HOST = socket.gethostbyname(socket.gethostname())     # Endereco IP do Servidor
PORT = 50000         # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
resposta=tcp.recv(1024)
if resposta=="ack":
	print resposta
	print 'Para sair use CTRL+X\n'
	msg = raw_input()
	while msg <> '\x18':
		tcp.send (msg)
		print "numero de mensagens enviadas:",tcp.recv(1024)
		msg = raw_input()
	tcp.close()

