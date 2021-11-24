import logging


class ModuleFilter(logging.Filter):
    def __init__(self, module=None, loglevel=None):
        self.module = module
        self.loglevel = loglevel


    def filter(self, record):
        if self.module is None:
            return True

        if self.module not in record.module:
            return True

        if self.loglevel is not None:
            if self.loglevel not in record.levelname:
                return True

        return False


def modulefilter(module=None,loglevel=None):
    return ModuleFilter(module,loglevel)
