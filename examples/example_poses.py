"""
Example of all poses in the library.
"""
from PIL import Image, ImageDraw
from PILSkinMC import poses, paste_skin

image = Image.new('RGBA', (400, 700))
draw = ImageDraw.Draw(image)

skin_slim = Image.open('skins/slim.png').convert('RGBA')
skin_wide = Image.open('skins/wide.png').convert('RGBA')

paste_skin(image, skin_slim, (20, 20), scale=64, pose=poses.SLIM)
paste_skin(image, skin_slim, (200, 20), scale=64, pose=poses.SLIM_GRUM)

paste_skin(image, skin_wide, (20, 370), scale=64, pose=poses.WIDE)
paste_skin(image, skin_wide, (200, 370), scale=64, pose=poses.WIDE_GRUM)

image.show()
