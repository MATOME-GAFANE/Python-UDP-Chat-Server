import socket
import threading
import queue
import sys
import random
import os 


#Client code begins
users =[]  

def Client_recieve(socket):                                     #Method used to recieve data from the socket that is later converted from bytes to string
   while True:
      try:
         information = socket.recvfrom(1024) 
         message_recieved = information[0].decode()
         print(message_recieved)  
         
      except:
         pass

def Client_mode(IP_server, IP_client, name):                     #Method allows user to act as client and send messages.  Takes in the server IP, Client IP and the name of the client as arguments.
   clientPort = random.randint(7000,10000)                       #Each User is assigned as random Port Number

   client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
   client_socket.bind((IP_client,clientPort))

   server = (str(IP_server),6000)


   client_socket.sendto(name.encode(),server)
   thread1 =threading.Thread(target=Client_recieve,args=(client_socket,))           #Allows the client to continuously send messages
   thread1.start()
   while True: 
      data = input()
      if data == 'log out':
         data = 'User '+name+' ' + 'has '+ data
         client_socket.sendto(data.encode(),server)
         print("you exited the chat")

         input1 = input("Please enter your password to log back in or enter 'quit' to exit:")   #Prompts user to enter password to log back into the chat
         print()  
         
         
         if(input1 == 'quit'): 
            break 
         else: 
            for user in users:
               if (user[0] == name) and (user[1] == password):
                  continue
               elif(user[0] == name) and (user[1] != password):
                  print("Incorrect password.")
                    #...

      if data!='':     
         data = '$'+name + ']:'+ data 
         client_socket.sendto(data.encode(),server) 
         print('message viewed')
   client_socket.sendto(data.encode(),server)
   client_socket.close()
   os._exit(1)
#Client code ends   



#Server code begins
def Server_recieve(server_socket, packets):   #Method used to receive data from socket (this method is run in a thread to ensure continuous data recieving)
   while True:
      info = server_socket.recvfrom(1024) 
      packets.append(info[0]) 
      packets.append(info[1])


def Server_mode(IP_server):        #Method allows user to act as a Server and monitor the transfer of messages between clients.  Takes the server's IP addres as an argument
   port = 6000
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   server_socket.bind((IP_server, port))
   clients =  [] 
   packets = []
   count = 0
   

   thread2 = threading.Thread(target=Server_recieve,args=(server_socket,packets))
   thread2.start()

   while True:
      while not len(packets) == 0:  #As long as the clients keeps communicating, the server will run
         data = packets[0] 
         addr = packets[1] 
         packets.pop(0) 
         packets.pop(0) 
         
         if addr not in clients:   #checking if the address exists in the clients list, if not it is appended to the list  
            clients.append(addr) 
               
         data = data.decode() 
         if data[-1:-5] == ('quit'): #If the message entered by the client ends with 'quit' the client is removed from the clients receiving messages
               clients.pop(addr) 
               
         print(data) 
         for client in clients:
            if client!=addr: 
               server_socket.sendto(data.encode(),client)         
   server_socket.close()
#Server code ends





if __name__ == '__main__': 
   
   os.system("tput setaf 6")                                         #Centres the text inside the title variable (similar to a heading)
   title = ("\t Welcome to Chat Box  \n")
   print(title)
   print()

   user_IP = input("Please enter IP address:")                       #Prompts user to enter their IP Address
   print()
   response = input("Please enter the letter if you want to be a server (S) or a client (C):")   #Asks user to indicate whether they are client or a server
   print()

   if(response == "S"):
      os.system("tput setaf 6")
      on = ("\t Server Running... \n") 
      print(on)
      print() 
      print("Now clients can request to your server :)") 
      Server_mode(user_IP) 
      
   elif (response == "C"):  
      empty_string = ''
      name = input("Please enter your name:")
      print()
      password = input("Please enter a password: ")
      print()

      print("password saved ") 
      user = [name,password]
      users.append(user) 
      server_IP = input("Enter the server you want to connect to:")   #Prompts the user to enter the IP address they would to connect to
      print()
      os.system("tput setaf 6")
      on = ("\t Client Running... \n")
      print(on)
      print()
      print("Now you can start chatting or enter 'log out' if you want to log out:)")
      Client_mode(server_IP,user_IP,name) 
      
   else:
      print("Invalid response")
