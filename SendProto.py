from  ATAKMessage_pb2  import TestMessage
import socket


def send_protobuf_message(uid, latitude, longitude, altitude, message_type, label, description):
    # Créer une instance du message TestMessage
    test_message = TestMessage()
    test_message.uid = uid
    test_message.latitude = latitude
    test_message.longitude = longitude
    test_message.altitude = altitude
    test_message.type = message_type
    test_message.label = label
    test_message.description = description

    # Sérialiser le message en bytes
    serialized_message = test_message.SerializeToString()

    # Envoyer le message via un socket (exemple avec UDP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #server_address = ("239.2.3.1", 6969)  # Adresse multicast et port
    server_address = ("10.0.2.15", 5000)  # Adresse multicast et port

    try:
        # Envoyer le message sérialisé
        sock.sendto(serialized_message, server_address)
        print("Message envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi du message : {e}")
    finally:
        sock.close()

# Exemple d'utilisation
send_protobuf_message(
    uid="unique-id-123",
    latitude=34.0522,
    longitude=-118.2437,
    altitude=100.0,
    message_type="a-f-G-U-C",
    label="Test Location",
    description="This is a test message."
)