"""Request

import requests

r = requests.get('https://matplotlib.org/stable/users/explain/quick_start.html')
print(r.encoding)
print(r.text)"""

"""Matplotlib

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import ConciseDateFormatter

# fig, ax = plt.subplots()             # Create a figure containing a single Axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
# plt.show()                           # Show the figure.

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
dates = np.arange(np.datetime64('2021-11-15'), np.datetime64('2024-10-22'),
                  np.timedelta64(1, 'h'))
data = np.cumsum(np.random.randn(len(dates)))
ax.plot(dates, data)
ax.xaxis.set_major_formatter(ConciseDateFormatter(ax.xaxis.get_major_locator()))
plt.show()"""

"""Pillow

from PIL import Image
import glob, os

size = 128, 128

for infile in glob.glob("1.jpg",):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")"""