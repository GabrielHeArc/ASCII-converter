import enum


class DefinitionImage(enum.Enum):
    """Definition image for ASCII conversion

    Args:
        enum (int): Width of image
    """
    D1 = 100
    D2 = 200
    D3 = 300
    SD = 400
    HD = 500


class DefinitionVideo(enum.Enum):
    """Definition video for ASCII conversion

    Args:
        enum (int): Width of video
    """
    D1 = 213
    D2 = 320
    D3 = 480
    SD = 720
    HD = 1280
    FHD = 1920
    UHD = 3840
