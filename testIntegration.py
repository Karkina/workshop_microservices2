import unittest
import requests


class SiteTest(unittest.TestCase):

    def test_getById(self):
        url = 'http://127.0.0.1:8000/snippets/1'
        result = [
            {
                "id": 1,
                "nom": "Societe",
                "montant": "800.00",
                "code": "L5484514",
                "devise": "Eur",
                "zone": "Europe",
                "brower": "Bidule",
                "lender": "Machin",
                "status": "Closing"
            }]
        response = requests.get(url)

        assert (response == result)

    def test_getDealsNumber(self):
        result = 2
        response = requests.get('http://127.0.0.1:8000/snippets/dealsNumber/')
        assert (response == result)
if __name__ == '__main__':
    unittest.main()
