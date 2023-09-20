import os 
theme = os.system("gsettings get org.gnome.desktop.interface gtk-theme")
print(theme)