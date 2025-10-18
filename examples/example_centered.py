"""
An example of rendering a player skin to the center of an image using skin_get_bbox
"""
from PIL import Image, ImageDraw
from PILSkinMC import poses, paste_skin, skin_get_bbox

image = Image.new('RGBA', (400, 400))
draw = ImageDraw.Draw(image)

skin_slim = Image.open('skins/slim.png').convert('RGBA')

bbox = skin_get_bbox(scale=64)
offset = tuple(int(image_dim / 2 - (_bbox[0] + _bbox[1]) / 2)
               for image_dim, _bbox in zip(image.size, [(bbox[0], bbox[2]), (bbox[1], bbox[3])]))
paste_skin(image, skin_slim, xy=offset, scale=64, pose=poses.SLIM)

image.show()
