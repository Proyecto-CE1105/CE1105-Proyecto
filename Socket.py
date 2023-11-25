import socket, keyboard
from threading import Thread

import pygame


class Socket:
    def __init__(self):
        self.server_address = ('0.0.0.0', 12345)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.conection = True
        self.data = ""

    def receiveControlSignal(self):
        print("Control conectado")
        try:
            while self.conection:
                data, address = self.sock.recvfrom(1024)
                decoded_data = data.decode()
                print(decoded_data)

                self.data = decoded_data


        except socket.error:
            print("ERROR")


    def closeControlConnection(self):
        self.conection = False
        self.sock.close()


    def start_reception_thread(self):
        thread_recepcion = Thread(target=self.receiveControlSignal)
        thread_recepcion.start()


    def setup_socket_and_thread(self):
        self.server_address = ('0.0.0.0', 12345)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.server_address)
        self.conection = True
        self.start_reception_thread()

