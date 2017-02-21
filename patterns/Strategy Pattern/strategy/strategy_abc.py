import abc


class AbsStrategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calculate(self, order):
        """Calculate shipping cost"""
