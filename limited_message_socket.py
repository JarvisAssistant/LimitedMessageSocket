import socket

class LimitedMessageSocket:
	MSG_LEN = 2048
	def __init__(self, server_address=None, ext_socket=None):
		self.socket = ext_socket
		if not self.socket:
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.server_address = server_address
	
	def connect(self):
		self.socket.connect(self.server_address)
	
	def listen(self):
		self.socket.bind(self.server_address)
		self.socket.listen()
	
	def accept(self):
		client_socket, _ = self.socket.accept()
		return client_socket
	
	def close(self):
		self.socket.close()
	
	def send(self, message):
		return self.socket.send(message.encode())
	
	def receive(self):
		return self.socket.recv(LimitedMessageSocket.MSG_LEN).decode()

