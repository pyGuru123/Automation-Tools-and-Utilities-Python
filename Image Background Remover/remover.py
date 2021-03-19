import cv2
from PIL import Image, ImageTk


class BackgroundRemover:
	def __init__(self):
		self.image = None

	def load_image(self, img_path, size):
		self.image = cv2.imread(img_path)
		self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
		img = self.display_image(size)
		return img

	def display_image(self, size):
		image = self.image
		h, w = image.shape[:2]
		if not (w <= size[0] and h <= size[1]):
			image = cv2.resize(image, size)
		tkimg = Image.fromarray(image)
		tkimg = ImageTk.PhotoImage(tkimg)

		return tkimg
