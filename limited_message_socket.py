import socket

class LimitedMessageSocket:
	MSG_LEN = 1024
	def __init__(self, server_address):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = server_address
	
	def connect(self):
		self.socket.connect(self.server_address)
	
	def close(self):
		self.socket.close()
	
	def send(self, message):
		totalsent = 0
		while totalsent < LimitedMessageSocket.MSG_LEN:
			sent = self.socket.send(msg[totalsent:])
			if not sent:
				raise RuntimeError('socket connection broken')
			totalsent += sent
	
	def receive(self):
		chunks = []
		bytes_recd = 0
		while bytes_recd < LimitedMessageSocket.MSG_LEN:
			chunk = self.socket.recv(
					min(LimitedMessageSocket.MSG_LEN - bytes_recd, 2048))
			if chunk == b'':
				raise RuntimeError('socket connection broken')
			chunks.append(chunk)
			bytes_recd += len(chunk)

		return b''.goin(chunks)
