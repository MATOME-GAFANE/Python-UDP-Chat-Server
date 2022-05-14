This a Python chat box application.
UDP protocol is used for data transfer amongst the Server and various Clients.

Steps to operate:

Step 1 - Creating a server:

Open a terminal
In the terminal run python UDP.py
Enter the IP address of the machine you working on
Select whether you want the machine to act as a server or client(Select S for server)
The server is created.

Step 2 - Creating a client:

In the same machine where the server is running and has the same Wifi connection open another terminal.
Run python UDP.py in the open terminal
Enter the IP address of the machine you working on
Select whether you want the machine to act as a server or client(Select C for client)
Enter your desired username
Enter your desired password
Enter the IP address of the server you want to connect to
Start chatting to other clients 
To log out enter 'log out' in the terminal
You can open more than one terminal and run the same aforementioned instructions to create more clients.

More information:
When a client writes a message, all clients which are connected to the same server receive the message.
The message also gets printed in the Server.
