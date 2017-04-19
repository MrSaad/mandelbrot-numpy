from PIL import Image
import numpy as np

dimen = 1024
iterations = 80

incr = 3.0/dimen
scale_factor = 255.0/iterations

# initial z and c values
z = np.zeros((dimen, dimen), dtype=np.complex)
X, Y = np.mgrid[-1.5:1.5:incr, -2:1:incr]
c = Y+1j*X

img_data = np.zeros((dimen, dimen), dtype=np.float32)

# do iterations of mandelbrot set
for i in range(iterations):
	
	z = z**2 + c

	# mask for values that have not diverged
	not_diverged = (np.abs(z)<4).astype(np.float32)

	# add non-divergent spots to image data
	img_data += not_diverged

# set non-diverged values to 0
img_data[img_data==img_data.max()] = 0

# Convert to RGB image
img = np.zeros((dimen, dimen, 3), dtype=np.uint8)
img[:, :, 0] = (img_data*scale_factor).astype(np.uint8)

display = Image.fromarray(img, 'RGB')
display.save('out.bmp')
display.show()



