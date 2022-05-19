from ultrobot import LOGS


def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_module = [
        basename(f)[:-3] for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_module


ALL_MODULE = sorted(__list_all_modules())
LOGS.info("Asistan modülleri yükleniyor: %s", str(ALL_MODULE))
__all__ = ALL_MODULE + ["ALL_MODULE"]
