# Projet Final Synthèse de Circuit

## Projet Final Django (pf django)
- Module de lecture et renvoie USB ou UART dans MCU (Arduino ou autre) et de contrôle des DELs:
  - **Fichier Arduino:** `projet-final-arduino/projet-final-arduino.ino`

- Librairie d'envoi et de réception des octets par UART sous Python:
  - **Fichier Python:** `test_uart.py`
    - *Remarque:* `projet-final/test_uart.py` sert de référence seulement, le fichier qui s'exécute par Django est `pfdjango/pfdjango/test_uart.py` (j'importe la fonction `send_uart` dans le fichier `views.py`)

- Page web avec bouton:
  - **Fichier HTML:** `pfdjango/templates/index.html`

- Script d'envoi et de réception des octets à l'aide des boutons:
  - **Fichier Python:** `views.py`
