__slots__ = ['poses', 'paste_skin', 'skin_get_bbox']
__version__ = '1.0.1'

import numpy
from PIL import Image, ImageEnhance
from typing import Union

from . import poses

_DEFAULT_SCALE = 64


def _iso_coords(x: Union[int | float], y: Union[int | float], scale: int) -> tuple[int | float, int | float]:
    """Finds the relative xy coords of an isometric grid point."""
    iso_x = (x - y) * scale / 2
    iso_y = (x + y) * scale / 4
    return iso_x, iso_y

def _find_coeffs(source: list[tuple[int | float]], target: list[tuple[int | float]]) -> list[float]:
    """Im not explaining what this does as I don't even fully understand it...
    I literally just based this off a random StackOverflow post I saw about this :p"""
    matrix = []
    
    for (x, y), (u, v) in zip(target, source):
        matrix.append([x, y, 1, 0, 0, 0, -u*x, -u*y])
        matrix.append([0, 0, 0, x, y, 1, -v*x, -v*y])
    
    A = numpy.array(matrix, dtype=float)
    B = numpy.array(source).reshape(8)
    
    coeffs, *_ = numpy.linalg.lstsq(A, B, rcond=None)
    return coeffs.tolist()

def paste_skin(image: Image.Image, skin: Image.Image, xy: tuple[int], scale: int = _DEFAULT_SCALE, pose: list = poses.WIDE) -> None:
    """Paste an isometric view of the defined skin onto the defined image.

    Args:
        image (Image.Image): Image to paste onto.
        skin (Image.Image): Skin image to paste.
        xy (tuple[int]): Position to paste at.
        scale: (int): Scale to render at, recommended to be a power of 2. Defaults to 64.
        pose (list, optional): Pose for the skin, also used to define skin type (SLIM/WIDE). Defaults to poses.WIDE.
    """
    for skin_pos, dest_pos, shading in pose:
        # Crop skin part and calculate its own coords
        part = skin.crop(skin_pos)
        p_coords = [(0, 0), (part.width, 0), part.size, (0, part.height)]
        
        # Shading for a slightly more 3D look
        if shading > 0: part = ImageEnhance.Brightness(part).enhance(1 - (shading / 100))
        
        # Calculate position to paste part at
        _pos = [_iso_coords(*xy, scale=scale) for xy in dest_pos]
        pos = [(round(x + xy[0]), round(y + xy[1])) for x, y, in _pos]
        
        min_x = round(min(x for x, _ in pos))
        min_y = round(min(y for _, y in pos))
        max_x = round(max(x for x, _ in pos))
        max_y = round(max(y for _, y in pos))
        
        local_pos = [(x - min_x, y - min_y) for x, y in pos]
        coeffs = _find_coeffs(p_coords, local_pos)
        
        # Warp and paste part
        with part.transform((max_x - min_x, max_y - min_y),
                            method=Image.Transform.PERSPECTIVE,
                            data=coeffs,
                            resample=Image.Resampling.NEAREST) as warped:
            # Funny workaround for PIL's annoying transparency
            with image.crop((min_x, min_y, max_x, max_y)) as region:
                blended = Image.alpha_composite(region, warped)
                image.paste(blended, (min_x, min_y))
                
                blended.close()
                region.close()
                warped.close()

        part.close()

def skin_get_bbox(scale: int = _DEFAULT_SCALE) -> tuple[int]:
    """Get the bounding box of a skin render based on its scale

    Args:
        scale (int, optional): Scale for rendering skin at. Defaults to 64.

    Returns:
        tuple[int]: Bounding box of skin render.
    """
    # 12.55, 7.35 is the very bottom right coord for all poses
    iso_x, iso_y = _iso_coords(12.55, 7.35, scale=scale)
    
    return (0, 0, iso_x, iso_y)
