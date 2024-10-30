import unittest
import requests


class CastingAgencyTestCase(unittest.TestCase):
    URL = "http://127.0.0.1:5000/"
    token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZaU0NzODhvckxzR0ZTc0lRUW9kdSJ9.eyJpc3MiOiJodHRwczovL2Rldi0wcGtxdXgwbHIwdnpueXRjLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NmYxODJiNTJkZTFjMWZlYTQ1ODRlYzkiLCJhdWQiOlsiY2FzdGluZ19hZ2VuY3kiLCJodHRwczovL2Rldi0wcGtxdXgwbHIwdnpueXRjLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MzAxMjM4ODIsImV4cCI6MTczMDIxMDI4Miwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImF6cCI6InVaMkhPU0JCZE1iM0ZVMDNyYWxzQ25VV2dQcjA5dTBIIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.-B3HP4rVJz06To7X7mtHuk4bq1Mqhbc4Cqca6-VhEzlvVqrGvkhMCTzlTpAWHCPlHUn8TFVMrGhYRZP0lHFEyoRNGxnQMxmwFJjV32BcCsQwigFhqHkJcG-0ycD3nZLx8SEXa8ZUtAUXWqsn8sBszed4blgTWxCNcBf8k22D4ydy-cKwFzbbQygZojM3gMGV4IQ1jP75metdstmNoBy1Ub2PuPUgALPc8f6-fEMY7oHjXs6QKAdlEM6YJJ5sv83BEAUx-124Xsu89HqlQXNnG0x2s1v8Pg3iDUjf9E0AJQPgPiFHuMB5yinZ6rcO4VUsS70G-ir_9H-MDzkLE0hwSw"

    # actor
    def test_create_actor(self):
        resp = requests.post(
            url=self.URL + "create-actor",
            json={"id": -1, "age": "21", "gender": False, "name": "linh"},
            headers={"Authorization": "Bearer " + self.token},
        ).json()
        self.assertEqual(resp["success"], True)
        self.assertEqual(resp["data"]["update_count"], 1)

    def test_update_actor(self):
        resp = requests.patch(
            url=self.URL + "update-actor",
            json={"id": 1, "age": "21", "gender": False, "name": "linh ham"},
            headers={"Authorization": "Bearer " + self.token},
        ).json()
        self.assertEqual(resp["success"], True)
        self.assertEqual(resp["data"]["update_count"], 1)

    def test_get_actors(self):
        resp = requests.get(
            self.URL + "actors",
            headers={"Authorization": "Bearer " + self.token},
        ).json()
        self.assertEqual(resp["success"], True)
        self.assertEqual(len(resp["data"]), 1)

    def test_get_actor_by_id(self):
        resp = requests.get(
            self.URL + "actors/1",
            headers={"Authorization": "Bearer " + self.token},
        ).json()
        self.assertEqual(resp["success"], True)
        self.assertEqual(resp["data"]["id"], 1)

    def test_delete_actor(self):
        resp = requests.delete(
            self.URL + "actors/1",
            headers={"Authorization": "Bearer " + self.token},
        ).json()
        self.assertEqual(resp["success"], True)
        self.assertEqual(resp["data"]["delete_count"], 1)

    # movie
    def test_create_movie(self):
        resp = requests.post(
            url=self.URL + "create-movie",
            json={
                "id": -1,
                "title": "titanic",
                "release_date": "2024-10-08T17:00:00.000Z",
            },
            headers={"Authorization": "Bearer " + self.token},
        ).json()
        self.assertEqual(resp["success"], True)
        self.assertEqual(resp["data"]["update_count"], 1)

    def test_update_movie(self):
        resp = requests.patch(
            url=self.URL + "update-movie",
            json={
                "id": 1,
                "title": "titanic1",
                "release_date": "2024-10-08T17:00:00.000Z",
            },
            headers={"Authorization": "Bearer " + self.token},
        ).json()
        self.assertEqual(resp["success"], True)
        self.assertEqual(resp["data"]["update_count"], 1)

    def test_get_movies(self):
        resp = requests.get(
            self.URL + "movies",
            headers={"Authorization": "Bearer " + self.token},
        ).json()
        self.assertEqual(resp["success"], True)
        self.assertEqual(len(resp["data"]), 1)

    def test_get_movie_by_id(self):
        resp = requests.get(
            self.URL + "movies/1",
            headers={"Authorization": "Bearer " + self.token},
        ).json()
        self.assertEqual(resp["success"], True)
        self.assertEqual(resp["data"]["id"], 1)

    def test_delete_movie(self):
        resp = requests.delete(
            self.URL + "movies/1",
            headers={"Authorization": "Bearer " + self.token},
        ).json()
        self.assertEqual(resp["success"], True)
        self.assertEqual(resp["data"]["delete_count"], 1)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
