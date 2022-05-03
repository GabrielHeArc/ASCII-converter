from ascii_converter import main_image
from settings import DefinitionImage

if __name__ == "__main__":
    path = "images/lena.png"
    main_image(path, DefinitionImage.HD, gray=True)
