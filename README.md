# PILSkinMC

PILSkinMC is a basic Minecraft player skin renderer for Python's PIL (Pillow) library.

## Table of Contents

* [Install](#install)
* [How it works?](#how-it-works)
* [Positioning](#positioning)
* [Skin type (poses)](#skin-type-poses)
* [Scaling](#scaling)

## Install

To install from PyPi

```sh
# Linux/mac
python3 -m pip install PILSkinMC

# Windows
py -3 -m pip install PILSkinMC
```

## How it works?

The library uses an isometric grid view to render skins with added shading to give a simple yet effective 3D look. Once imported you can simply paste in a pre-loaded skin file as such.

```py
image = Image.new('RGBA', (400, 400))
skin = Image.open('skin.png').convert('RGBA')

paste_skin(image, skin, xy=(20, 20))
```

## Positioning

The xy coordinates will be at the top left of the rendered model, if you require help with more complicated positioning you can use the `skin_get_bbox()` function to get the bounding box of the full model.

## Skin type (poses)

By default the `paste_skin()` function will presume skins are of the wide 4px arm variant, this can be changed by parsing in a `pose` which can be one of 4:

* `PILSkinMC.poses.SLIM`
* `PILSkinMC.poses.WIDE`
* `PILSkinMC.poses.SLIM_GRUM`
* `PILSkinMC.poses.SLIM_GRUM`

*(yes I added custom poses for Grum/Dinnerbone variants)*

## Scaling

By default the `paste_skin()` function will render skins at a scale of `64`, this is the size of the theoretical isometric grid that the skin is being rendered off of. To change it simply parse a `scale` with any integer value.

**Note:** It is recommended to only use scales that are powers of 2 (4, 8, 16, 32, 64, 128, etc) as irregular values can sometimes cause gaps in the resulting image.

The scale option can also be used in the `skin_get_bbox()` function to get the bbox with the desired scaling.
