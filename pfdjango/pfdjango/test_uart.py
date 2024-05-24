import serial
import time

# Liste de ports
# Linux
port_list = ["/dev/ttyACM0"]
# WINDBLOWS
# port_list = ["COM11"]

test_string = "D"

def send_uart(port, msg):
    # Init du port
    print("Lecture de port: " + port)
    serialPort = serial.Serial(port, 9600, timeout = 2)
    time.sleep(2) # Tres important, sinon l'arduino ne recoit pas le char
    
    # Envoi du string "test_string"
    bytes_sent = serialPort.write(msg.encode('utf-8'))
    print("Envoi de " + str(bytes_sent) + " octets")
    
    # Lecture du string de retour
    string_de_retour = serialPort.read(bytes_sent).decode('utf-8')
    
    # Verification du string de retour
    if string_de_retour == msg:
        print("Recu " + str(len(string_de_retour)) + " octets identiques. Le port " + port + " fonctionne bien!\n")
        print("String recu: " + string_de_retour)
    else:
        print("Recu des donnes incorrectes: " + string_de_retour + " sur le port serie " + port + " boucle \n")
            
        # Fermeture du port
    serialPort.close()
    return string_de_retour
        
for port in port_list:
    try:        
        send_uart(port, test_string)
    except IOError:
        print("Erreur sur " + port + "\n")
