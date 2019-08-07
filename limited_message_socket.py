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
		self.socket.send(message.encode())
		'''
		totalsent = 0
		while totalsent < LimitedMessageSocket.MSG_LEN:
			sent = self.socket.send(msg[totalsent:])
			if not sent:
				raise RuntimeError('socket connection broken')
			totalsent += sent
		'''
	
	def receive(self):
		return self.socket.recv(LimitedMessageSocket.MSG_LEN).decode()
		'''
		chunks = []
		bytes_recd = 0
		while bytes_recd < LimitedMessageSocket.MSG_LEN:
			chunk = self.socket.recv(
					min(LimitedMessageSocket.MSG_LEN - bytes_recd, 2048))
			if chunk == b'':
				raise RuntimeError('socket connection broken')
			chunks.append(chunk)
			bytes_recd += len(chunk)

		return b''.join(chunks)
		'''

