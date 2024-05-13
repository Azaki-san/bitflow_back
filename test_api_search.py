import unittest
from api_search import app


class TestQuartApp(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.app = app
        self.client = self.app.test_client()

    async def test_search_endpoint(self):
        response = await self.client.get('/search?query=test')
        self.assertEqual(response.status_code, 200)
        data = await response.get_json()
        self.assertTrue(isinstance(data, dict))

    async def test_get_info_endpoint(self):
        response = await self.client.get(
            '/get_info?link=http://www.1337x.to/torrent/3994201/Spider-Man-Far-from-Home-2019-WEBRip-1080p-YTS-YIFY/')
        self.assertEqual(response.status_code, 200)
        data = await response.get_json()
        self.assertTrue(isinstance(data, dict))

    async def test_get_info_endpoint_with_error(self):
        response = await self.client.get(
            '/get_info?link=')
        self.assertEqual(response.status_code, 400)
        data = await response.get_json()
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['status'], 'Bad Request')

    async def test_health_endpoint(self):
        response = await self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = await response.get_json()
        self.assertEqual(data['status'], 'Ok')


if __name__ == '__main__':
    unittest.main()
