import socket

def send_simple_message():
    simple_message = b"Hello, UDP!"  # Message à envoyer

    # Créer un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #server_address = ("10.0.2.2", 9000)   # Adresse et port du serveur
    server_address = ("10.0.2.16", 5000)   # Adresse et port du serveur

    try:
        # Envoyer le message
        sock.sendto(simple_message, server_address)
        print("Message envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi du message : {e}")
    finally:
        sock.close()

# Exemple d'utilisation
send_simple_message()