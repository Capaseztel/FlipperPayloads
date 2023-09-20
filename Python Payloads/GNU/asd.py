import os 
theme = str(os.popen("gsettings get org.gnome.desktop.interface gtk-theme"))
if "dark" in theme:
    print("dark")
else:
    print(f"cosa rara: {theme}")