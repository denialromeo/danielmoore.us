import os

# List of filenames to keep
filenames_to_keep = [
    "31rfDo1.jpg", "6MrS7l6.jpg", "7HaNtrz.jpg", "9cEd0v7.jpg", "AkhMREW.jpg",
    "bangs.jpg", "black.jpg", "bond.jpg", "CF4Iars.jpg", "chin.jpg",
    "cioran.png", "cVRaEKD.jpg", "dwayne.jpg", "e7WpR10.png", "eauTUYo.jpg",
    "eboshi.jpg", "f8placi.jpg", "foyle.jpg", "g55WhfM.png", "gbpTFJ5.png",
    "gwXE0Ed.jpg", "hendrix.jpg", "hp2MdWL.png", "invincible.jpg", "jaqen.jpg",
    "jigo.jpg", "khhgNnh.jpg", "khrushchev.jpg", "kPIXsbI.jpg", "l716WKC.jpg",
    "Ld2bhG4.jpg", "lDcaM4o.jpg", "lgACrR3.jpg", "LiDM9Lt.jpg", "livermore.jpg",
    "long.jpg", "murthy.jpg", "NFFu8N2.jpg", "nietzsche.jpg", "OFoEt3E.jpg",
    "pig.jpg", "rabbit.jpg", "roberts.jpg", "rosenberg.jpg", "RYqrmC6.jpg",
    "schopenhauer.jpg", "shining.jpg", "Sq64l3n.jpg", "stallman.png", "takumi.jpg",
    "tiger.jpg", "tiger2.jpg", "TilYjqc.jpg", "Up6GEY4.jpg", "varamyr.jpg",
    "vikrant.jpg", "vogarro.jpg", "vSCpAZc.png", "wyJwnBa.jpg", "YzqRXJI.jpg",
    "Zc7XzDT.jpg", "zVTJc2Q.jpg"
]

directory_path = 'assets/img/imgur'  # Update this path to your directory

# Iterate through the files in the directory
for filename in os.listdir(directory_path):
    # If the file is not in the list of filenames to keep, delete it
    if filename not in filenames_to_keep:
        file_path = os.path.join(directory_path, filename)
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
