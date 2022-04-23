import enum


class DefinitionImage(enum.Enum):
    D1 = [100, 100]  # Temporary
    D2 = [200, 200]  # Temporary
    D3 = [300, 300]  # Temporary
    SD = [400, 400]
    HD = [500, 500]
    FHD = [600, 600]
    UHD = [700, 700]


class DefinitionVideo(enum.Enum):
    D1 = [213, 142]  # Temporary
    D2 = [320, 213]  # Temporary
    D3 = [480, 320]  # Temporary
    SD = [720, 480]
    HD = [1280, 720]
    FHD = [1920, 1080]
    UHD = [3840, 2160]
