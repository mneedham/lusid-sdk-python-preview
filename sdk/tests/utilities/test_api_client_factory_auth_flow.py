import unittest
from lusid import InstrumentsApi, ResourceListOfInstrumentIdTypeDescriptor
from lusid.utilities import ApiClientFactory
from utilities import CredentialsSource
from unittest.mock import patch

source_config_details, config_keys = CredentialsSource.fetch_credentials(), CredentialsSource.fetch_config_keys()


class ApiFactory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a configured API client
        cls.secrets = CredentialsSource.secrets_path()

    def validate_api(self, api):
        result = api.get_instrument_identifier_types()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, ResourceListOfInstrumentIdTypeDescriptor)
        self.assertGreater(len(result.values), 0)

    def test_get_api_with_access_token_env_var(self):

        factory = ApiClientFactory()
        api = factory.build(InstrumentsApi)
        self.assertIsInstance(api, InstrumentsApi)
        self.validate_api(api)

    def test_get_api_with_access_token_as_param(self):

        factory = ApiClientFactory(token=source_config_details["access_token"])
        api = factory.build(InstrumentsApi)
        self.assertIsInstance(api, InstrumentsApi)
        self.validate_api(api)

    def test_get_api_with_secrets_file_as_param(self):

        factory = ApiClientFactory(api_secrets_filename=self.secrets)
        api = factory.build(InstrumentsApi)
        self.assertIsInstance(api, InstrumentsApi)
        self.validate_api(api)

    def test_get_api_with_none_string_token_param(self):

        factory = ApiClientFactory(token="None")
        api = factory.build(InstrumentsApi)
        self.assertIsInstance(api, InstrumentsApi)
        self.validate_api(api)

    def test_get_api_with_none_token_param(self):

        factory = ApiClientFactory(token=None)
        api = factory.build(InstrumentsApi)
        self.assertIsInstance(api, InstrumentsApi)
        self.validate_api(api)

    def test_get_api_with_none_secrets_file(self):

        factory = ApiClientFactory(api_secrets_filename=None)
        api = factory.build(InstrumentsApi)
        self.assertIsInstance(api, InstrumentsApi)
        self.validate_api(api)
