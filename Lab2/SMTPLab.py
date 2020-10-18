from socket import *
import sys


msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"


# Choose a mail server (e.g. Google mail server) and call it mailServer
mailServer = 'localhost'  # using private testing SMTP server
mailPort = 1010  # port number


# Create socket called clientSocket and establish a TCP connection with mailServer
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
recv = clientSocket.recv(1024).decode()
print('Conn cmd response: ' + recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response.
heloCommand = 'HELO Server\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print('HELO cmd response: ' + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: <TeamCCD@SJSUcmpe.edu>\r\n'  # From address
clientSocket.send(mailFromCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print('MAIL FROM cmd response: ' + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server')


# Send RCPT TO command and print server response.
# rcptToCommand = 'RCPT TO: <raymond.chin@sjsu.edu>\r\n'  # To address
rcptToCommand = 'RCPT TO: <' + input('Recipient email address: ') + '>\r\n'
clientSocket.send(rcptToCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print('RCPT TO cmd response: ' + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server')


# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
print(dataCommand)
clientSocket.send(dataCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print('DATA cmd response: ' + recv1)
if recv1[:3] != '354':
    print('354 reply not received from server')


# Send message data.
subject = input('Enter subject: ')
print('Enter message body. When finished, press \'Enter, Ctrl + d\':\n')
message = sys.stdin.read()
# Message ends with a single period.
# clientSocket.send((subject + msg + endmsg).encode())
clientSocket.send((
                          "From: " + mailFromCommand[12:-3] + "\r\n" +
                          "Subject: " + subject + "\r\n" +
                          "To: " + rcptToCommand[10:-3] + "\r\n" +
                          "\n" + message + endmsg).encode())
recv1 = clientSocket.recv(1024).decode()
print('MESSAGE CONTENT response: ' + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server')


# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
print(quitCommand)
clientSocket.send(quitCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print('QUIT cmd response: ' + recv1)
if recv1[:3] != '221':
    print('221 reply not received from server')
    pass

clientSocket.close()  # close socket; unsafe

# enable for script
# if __name__ == '__main__':
#     main()

