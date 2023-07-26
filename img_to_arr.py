from PIL import Image
import numpy as np
import pandas as pd

with Image.open("yso.jpg") as img:
    img.load()

# Cause for .csv file each symbol is 1 byte,
# then  for (m,n) res. image size of .csv will be
# s = (2m+1)n

m, n = img.size
s_file = (2*m+1)*n

# For example: our maximum size of file 10 kb
max_size = 1024*10

# Optimize
if s_file <= max_size:
    img = img.convert('1')
elif s_file > max_size:
    # solve eq. (2mx + 1)nx where x is how much we want reduce image res.
    d = n ** 2 + 8 * max_size * m * n
    sol = (-n + d ** (1 / 2)) / (4 * m * n)
    
    img = img.reduce(int(1/sol+1)).convert('1')

# make dataframe of image
arr = np.asarray(img)*1
df = pd.DataFrame(arr)

# write dataframe in .csv format
df.to_csv('data.csv', index=False, header=False)





