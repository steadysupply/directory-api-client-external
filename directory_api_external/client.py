from directory_api_external.supplier import SupplierAPIClient
from directory_api_external.base import BaseAPIClient


class DirectoryAPIExternalClient(BaseAPIClient):

    def __init__(self, base_url=None, api_key=None):
        self.supplier = SupplierAPIClient(base_url, api_key)
        super().__init__(base_url, api_key)
