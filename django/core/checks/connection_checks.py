from django.core import mail
from django.core.checks import Error, register


def get_all_connections():
    """
    the idea is to test other connections like db/caching etc?
    they will have to implement the check() method
    """
    return [mail.get_connection()]


@register('connections')
def check_all_connections(app_configs=None, **kwargs):
    errors = []
    for connection in get_all_connections():
        try:
            result = connection.check()
        except:
            msg = "The '%s.check' class method is not implemented."
            Error(msg % connection.__name__, id='connections.E001')
        if result is not None:
            errors.append(result)
    return errors
