# munyit IRC bot 

######## modules needed
import socket
import time
import threading
import configparser
#import syscommand

#sysc = syscommand.syscommand.news
########
myc = ['help','changenick']
class munyit(object):

    def __init__(self):
        ### load bot config here
        config = configparser.ConfigParser()
        if config.read("config.ini"):
            
            self.nick = config['config']['nick']
            self.server = config['config']['server']
            self.port = int(config['config']['port'])
            self.chan = config['config']['chan']

        #### done config
        

    def _connect(self):
        ###  connect bot here
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((self.server, self.port))
        self.irc.send(str("NICK " + self.nick + "\r\n").encode())
        self.irc.send(str("USER " + self.nick + " 8 *:munyitbot munyitBot v1.0!\r\n").encode())
        ### done connect

    def _run(self):
        ### run bot in While
        while True:
            buff = self.irc.recv(4096).decode("UTF-8")
            data = buff.split("\r\n")
            print(data)
            for each in data:
                
                if "PING :" in each:
                    pong = each.split(":")[1]
                    self.irc.send(str("PONG :" + pong + "\r\n").encode())
                if "004" in each:
                    self.irc.send(str("JOIN " + self.chan + "\r\n").encode())
                    
                if "PRIVMSG " in each:
                    findc = each.split(" ")
                    print(findc)
                    print(findc[3].strip(":"))
                    if findc[3].strip(":") in myc:
                        self.irc.send(str("PRIVMSG #tess :ooo kau cakap " + findc[3].strip(":") + "\r\n").encode())

"""
                if 'PRIVMSG ' in each:
                    whomsgme = each.split(" ")
                    if '#' in whomsgme[2]:
                        #mm = syscommand.news
                        self.irc.send(str("PRIVMSG " + whomsgme[2] + " :diam la kau " + sysc + "\r\n").encode())
                    else:
                        thenick = whomsgme[0].split("!")[0]
                        print(thenick)
                        self.irc.send(str("PRIVMSG " + thenick.strip(':') + " :what kau budu\r\n").encode())
                """

######## main function 
def main():
    bot = munyit()
    bot._connect()
    try:
        bot._run()
    except Exception:
        print(Exception)

if __name__ == "__main__":
    main()
