import os
import getpass

def get_ubuntu_version():
    try:
        with open('/etc/os-release', 'r') as os_release_file:
            lines = os_release_file.readlines()
            for line in lines:
                if line.startswith("VERSION="):
                    version_info = line.strip().split("=")[1].strip('"')
                    return version_info
    except FileNotFoundError:
        return "No se pudo encontrar el archivo /etc/os-release"
    except Exception as e:
        return f"Error: {str(e)}"

ubuntu_version = get_ubuntu_version()

user = getpass.getuser()
print("user = " + user)
os.system("cd Imágenes && wget --output-document=pikmin.jpg https://pbs.twimg.com/media/EYzIYbcXgAAf3Gp.jpg")
if ubuntu_version.startswith("20") == True:
    os.system(f"gsettings set org.gnome.desktop.background picture-uri file:///home/{user}/Imágenes/pikmin.jpg")
elif ubuntu_version.startswith("22") ==True:
    theme = str(os.popen("gsettings get org.gnome.desktop.interface gtk-theme").read())
    if "dark" in theme.lower():
        os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark file:///home/{user}/Imágenes/pikmin.jpg")
    else:
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file:///home/{user}/Imágenes/pikmin.jpg")

