import os 
theme = str(os.popen("gsettings get org.gnome.desktop.interface gtk-theme"))
if "dark" in theme.lower():
    print("dark")
else:
    print(f"cosa rara: {theme}")