import logging

logger = logging.getLogger(__name__)

def log_lambda(fn):
    def func(*a, **kw):
       logger.info('%s(%s, %s)', fn, a, kw)
       return fn(*a, **kw)
    return func