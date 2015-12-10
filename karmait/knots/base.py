import abc


class BaseKnot(abc.ABC):

    @abc.abstractmethod
    def count_karma(self, since=None, until=None):
        pass

    @abc.abstractmethod
    def get_what_have_i_done(self, since=None, until=None):
        pass
