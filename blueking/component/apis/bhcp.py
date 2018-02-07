from ..base import ComponentAPI


class CollectionsBHCP(object):
    """Collections of BHCP APIS"""

    def __init__(self, client):
        self.client = client

        self.get_ip = ComponentAPI(
            client = self.client, method='GET', path='/api/c/compapi/bhcp/get_ip/',
            description="test",
        )




