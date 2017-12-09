## Generates the banner for the Toolkit program

from pyfiglet import Figlet

banner = Figlet(font = 'ogre')

print banner.renderText('The Toolkit')

banner = Figlet(font = 'big')
print banner.renderText('The Toolkit')

banner = Figlet(font = 'larry3d')
print banner.renderText('The Toolkit')

banner = Figlet(font = 'doom')
print banner.renderText('The Toolkit')
