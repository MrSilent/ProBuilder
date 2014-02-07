# This file allows you to programmatically create blocks in Craft.
# Please use this wisely. Test on your own server first. Do not abuse it.

import requests
import socket
import sqlite3
import sys
import time

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 4080

EMPTY = 0
GRASS = 1
SAND = 2
STONE = 3
BRICK = 4
WOOD = 5
CEMENT = 6
DIRT = 7
PLANK = 8
SNOW = 9
GLASS = 10
COBBLE = 11
LIGHT_STONE = 12
DARK_STONE = 13
CHEST = 14
LEAVES = 15
CLOUD = 16
TALL_GRASS = 17
YELLOW_FLOWER = 18
RED_FLOWER = 19
PURPLE_FLOWER = 20
SUN_FLOWER = 21
WHITE_FLOWER = 22
BLUE_FLOWER = 23
STEEL = 63
STEEL_BLUE = 62
WHITE = 61
LAVENDER = 60
TURQOISE = 59
INDIGO = 58
ROYAL_BLUE = 57
DENIM = 56
SHIRONERI = 55
TAN = 54
RUST = 53
TAUPE = 52
BROWN = 51
MAROON = 50
MIDNIGHT_BLUE = 49
BLACK = 48
KHAKI = 47
OLIVE = 46
HOT_PINK = 45
PINK = 44
RED = 43
PURPLE = 42
DARK_GREY = 41
LIGHT_GREY = 40
NAVY = 39
CHARCOL = 38
REA = 37
PINE = 36
CYAN = 35
DROID_GREEN = 34
LIGHT_GREEN = 33
YELLOW = 32

OFFSETS = [
    (-0.5, -0.5, -0.5),
    (-0.5, -0.5, 0.5),
    (-0.5, 0.5, -0.5),
    (-0.5, 0.5, 0.5),
    (0.5, -0.5, -0.5),
    (0.5, -0.5, 0.5),
    (0.5, 0.5, -0.5),
    (0.5, 0.5, 0.5),
]

def sphere(cx, cy, cz, r, fill=False, fx=False, fy=False, fz=False):
    result = set()
    for x in range(cx - r, cx + r + 1):
        if fx and x != cx:
            continue
        for y in range(cy - r, cy + r + 1):
            # if y < cy:
            #     continue # top hemisphere only
            if fy and y != cy:
                continue
            for z in range(cz - r, cz + r + 1):
                if fz and z != cz:
                    continue
                inside = False
                outside = fill
                for dx, dy, dz in OFFSETS:
                    ox, oy, oz = x + dx, y + dy, z + dz
                    d2 = (ox - cx) ** 2 + (oy - cy) ** 2 + (oz - cz) ** 2
                    d = d2 ** 0.5
                    if d < r:
                        inside = True
                    else:
                        outside = True
                if inside and outside:
                    result.add((x, y, z))
    return result

def circle_x(x, y, z, r, fill=False):
    return sphere(x, y, z, r, fill, fx=True)

def circle_y(x, y, z, r, fill=False):
    return sphere(x, y, z, r, fill, fy=True)

def circle_z(x, y, z, r, fill=False):
    return sphere(x, y, z, r, fill, fz=True)

def cylinder_x(x1, x2, y, z, r, fill=False):
    x1, x2 = sorted((x1, x2))
    result = set()
    for x in range(x1, x2 + 1):
        result |= circle_x(x, y, z, r, fill)
    return result

def cylinder_y(x, y1, y2, z, r, fill=False):
    y1, y2 = sorted((y1, y2))
    result = set()
    for y in range(y1, y2 + 1):
        result |= circle_y(x, y, z, r, fill)
    return result

def cylinder_z(x, y, z1, z2, r, fill=False):
    z1, z2 = sorted((z1, z2))
    result = set()
    for z in range(z1, z2 + 1):
        result |= circle_z(x, y, z, r, fill)
    return result

def cone_y(x, y, z, r, fill=False):
    result = set()
    for y in range(y, y+r):
        result |= circle_y(x, y, z, r, fill)
        y += 1
        r -= 1
    return result

def cuboid(x1, x2, y1, y2, z1, z2, fill=True):
    x1, x2 = sorted((x1, x2))
    y1, y2 = sorted((y1, y2))
    z1, z2 = sorted((z1, z2))
    result = set()
    a = (x1 == x2) + (y1 == y2) + (z1 == z2)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                n = 0
                n += x in (x1, x2)
                n += y in (y1, y2)
                n += z in (z1, z2)
                if not fill and n <= a:
                    continue
                result.add((x, y, z))
    return result

def pyramid2(x1, x2, y1, y2, z1, z2, fill=False):
    x1, x2 = sorted((x1, x2))
    y1, y2 = sorted((y1, y2))
    z1, z2 = sorted((z1, z2))
    result = set()
    xrng = len(range(x1, x2))
    yrng = len(range(y1, y2))
    zrng = len(range(z1, z2))
    if xrng >= zrng:
        lrgr = xrng
    elif xrng < zrng:
        lrgr = zrng
    if yrng >= lrgr:
        if yrng / (lrgr / 2) > 1:
            yi = yrng / (lrgr / 2)
            while x2 >= x1 and z2 >= z2:
                result |= cuboid(x1, x2, y1, y1+yi, z1, z2, fill)
                y1, x1, x2, z1, z2 = y1 + yi, x1 + 1, x2 - 1, z1 + 1, z2 - 1
        elif yrng / (lrgr / 2) <= 1:
            while x2 >= x1 and z2 >= z2:
                result |= cuboid(x1, x2, y1, y1, z1, z2, fill)
                y1, x1, x2, z1, z2 = y1 + 1, x1 + 1, x2 - 1, z1 + 1, z2 - 1
    return result

def pyramid(x1, x2, y, z1, z2, fill=False):
    x1, x2 = sorted((x1, x2))
    z1, z2 = sorted((z1, z2))
    result = set()
    while x2 >= x1 and z2 >= z2:
        result |= cuboid(x1, x2, y, y, z1, z2, fill)
        y, x1, x2, z1, z2 = y + 1, x1 + 1, x2 - 1, z1 + 1, z2 - 1
    return result

def upyramid(x1, x2, y, z1, z2, fill=False):
    x1, x2 = sorted((x1, x2))
    z1, z2 = sorted((z1, z2))
    result = set()
    while x2 >= x1 and z2 >= z2:
        result |= cuboid(x1, x2, y, y, z1, z2, fill)
        y, x1, x2, z1, z2 = y - 1, x1 + 1, x2 - 1, z1 + 1, z2 - 1
    return result

def get_identity():
    query = (
        'select username, token from identity_token where selected = 1;'
    )
    conn = sqlite3.connect('auth.db')
    rows = conn.execute(query)
    for row in rows:
        return row
    raise Exception('No identities found.')

class Client(object):
    def __init__(self, host, port):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((host, port))
        self.authenticate()
    def authenticate(self):
        username, identity_token = get_identity()
        url = 'https://craft.michaelfogleman.com/api/1/identity'
        payload = {
            'username': username,
            'identity_token': identity_token,
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200 and response.text.isalnum():
            access_token = response.text
            self.conn.sendall('A,%s,%s\n' % (username, access_token))
        else:
            raise Exception('Failed to authenticate.')
    def set_block(self, x, y, z, w):
        self.conn.sendall('B,%d,%d,%d,%d\n' % (x, y, z, w))
    def set_blocks(self, blocks, w):
        key = lambda block: (block[1], block[0], block[2])
        for x, y, z in sorted(blocks, key=key):
            self.set_block(x, y, z, w)
    def bitmap(self, sx, sy, sz, d1, d2, data, lookup):
        x, y, z = sx, sy, sz
        dx1, dy1, dz1 = d1
        dx2, dy2, dz2 = d2
        for row in data:
            x = sx if dx1 else x
            y = sy if dy1 else y
            z = sz if dz1 else z
            for c in row:
                w = lookup.get(c)
                if w is not None:
                    self.set_block(x, y, z, w)
                x, y, z = x + dx1, y + dy1, z + dz1
            x, y, z = x + dx2, y + dy2, z + dz2

##def get_client():
##    default_args = [DEFAULT_HOST, DEFAULT_PORT]
##    args = sys.argv[1:] + [None] * len(default_args)
##    host, port = [a or b for a, b in zip(args, default_args)]
##    client = Client(host, int(port))
##    return client

def main():
    client = client(host, int(port))
    set_block = client.set_block
    set_blocks = client.set_blocks
##    i = 1
##    while i < 105:
##        set_blocks(cuboid(-89, -60, i, i, 30, -30, fill=True), LIGHT_STONE)
##        i += 4
##    time.sleep(10)
##    set_blocks(pyramid(-182, -172, 12, 22, 148, 138, fill=False), EMPTY)
##    time.sleep(3)

if __name__ == '__main__':
    main()
