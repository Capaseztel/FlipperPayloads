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
print("Versión de Ubuntu:", ubuntu_version)