import enum


class DefinitionImage(enum.Enum):
    D1 = [100, 0]
    D2 = [200, 0]
    D3 = [300, 0]
    SD = [400, 0]
    HD = [500, 0]


class DefinitionVideo(enum.Enum):
    D1 = [213, 142]  # Temporary
    D2 = [320, 213]  # Temporary
    D3 = [480, 320]  # Temporary
    SD = [720, 480]
    HD = [1280, 720]
    FHD = [1920, 1080]
    UHD = [3840, 2160]
