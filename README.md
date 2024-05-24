# projet-final-synthese-de-circuit
pf django: projet final django
a) Module de lecture et renvoie USB ou UART dans MCU (Arduino ou autre) et de control des DELs: projet-final-arduino/projet-final-arduino.ino<br>
b) Librairie d'envoi et de reception des octets par UART sous Python: test_uart.py<br>
    projet-final/test_uart.py sert de reference seulement, le fichier qui se fait executer par django est  pfdjango/pfdjango/test_uart.py (j'importe la fonction send_uart dans le fichier views.py)<br>
c) Page web avec bouton: pfdjango/templates/index.html<br>
d) Script d'envoi et de reception des octets a l'aide des boutons: views.py<br>
