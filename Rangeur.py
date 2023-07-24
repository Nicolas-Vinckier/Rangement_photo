import os
import shutil
import datetime

def copier_coller_media(source, destination):
    # Parcours de tous les fichiers et dossiers dans le répertoire source
    for root, dirs, files in os.walk(source):
        for filename in files:
            # Obtenir le chemin complet du fichier
            filepath = os.path.join(root, filename)
            
            # Obtenir la date de création du fichier
            date_creation = datetime.datetime.fromtimestamp(os.path.getctime(filepath))
            
            # Définir les répertoires de destination
            annee = str(date_creation.year)
            mois = date_creation.strftime('%B')
            destination_annee = os.path.join(destination, annee)
            destination_mois = os.path.join(destination_annee, mois)
            destination_doublon = os.path.join(destination, "doublon")
            
            # Vérifier si le fichier est une photo ou une vidéo
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.mp4', '.avi', '.mov')):
                # Vérifier si le répertoire de destination pour l'année existe, sinon le créer
                if not os.path.exists(destination_annee):
                    os.makedirs(destination_annee)
                
                # Vérifier si le répertoire de destination pour le mois existe, sinon le créer
                if not os.path.exists(destination_mois):
                    os.makedirs(destination_mois)
                
                # Définir le chemin de destination
                destination_filepath = os.path.join(destination_mois, filename)
                
                # Vérifier si le fichier existe déjà dans le répertoire de destination
                if os.path.exists(destination_filepath):
                    # Déplacer le fichier dans le répertoire des doublons
                    shutil.move(filepath, os.path.join(destination_doublon, filename))
                else:
                    # Copier le fichier dans le répertoire de destination
                    shutil.copy2(filepath, destination_filepath)

# Exemple d'utilisation
source = "Source_photo"
destination = "Destination_photo"

copier_coller_media(source, destination)