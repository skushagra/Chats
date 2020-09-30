from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

BUFSIZ = 512

def handel_client():
	run = True
	while run:
		msg = client.recv(BUFSIZ)
		if msg != bytes("{quit}", "utf8"):
			broadcast(msg, name+":    ")
		else:
			client.send(bytes("{quit}", "utf8"))
			client.close()
			del clients[client]
			broadcast(bytes("%s has left the chat." % name, ))



def accept_incoming_connection(SERVER):
	run = True
	while run:
		try:
			client, addr = SERVER.accept()
			Thread(target=handel_client, args=(client,)).start()
		except Exception as e:
			print("[Failure] ",e)
			run = False


HOST = 'localhost'
PORT = 8000
BUFSIZ = 1024
ADDR = (HOST,PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main___":
	SERVER.listen(5)
	print("Waiting for connection...")
	ACCEPT_THREAD = Thread(target=accept_incoming_connection, (SERVER))
	ACCEPT_THREAD.start()
	ACCEPT_THREAD.join()
	SERVER.close()



