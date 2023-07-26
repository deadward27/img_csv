from PIL import Image
import pandas as pd

df = pd.read_csv('data.csv')
img_arr = df.to_numpy()

img = Image.fromarray(img_arr.astype('bool'))

img.show()


