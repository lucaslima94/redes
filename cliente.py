import json
import socket
HOST = socket.gethostbyname(socket.gethostname())     # Endereco IP do Servidor
PORT = 30000         # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
resposta=tcp.recv(1024)
if resposta=="ack":
	print "nome usuario"
	user=raw_input()
	print "senha"
	password=raw_input()
	line=user+' '+password
	tcp.send(line)
	resposta=tcp.recv(1024)
	if(resposta=="500"):
		print "conexao iniciada"
		print 'Para sair use CTRL+X\n'
		msg = raw_input()
		while msg <> '\x18':
			tcp.send (msg)
			print "numero de mensagens enviadas:",tcp.recv(1024)
			msg = raw_input()
		tcp.close()
	if(resposta=="501"):
		print "usuario ou senha incorretos"
		tcp.close()
		exit()
		

