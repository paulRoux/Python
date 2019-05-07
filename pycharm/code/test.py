import unittest
from login import app
import json


class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        # 打开测试模式，就会在测试结果里面知道问题的具体地方和情况
        # app.config["TESTING"] = True
        app.testing = True
        self.client = app.test_client()

    def test_empty_all(self):
        ret = self.client.post("/login", data={})
        res = ret.data
        res_dict = json.loads(res)
        self.assertIn("code", res_dict)
        self.assertEqual(res_dict["code"], 1)

    def test_empty_pass(self):
        ret = self.client.post("/login", data={"username": "roux"})
        res = ret.data
        res_dict = json.loads(res)
        self.assertIn("code", res_dict)
        self.assertEqual(res_dict["code"], 1)

    def test_empty_name(self):
        ret = self.client.post("/login", data={"password": "111"})
        res = ret.data
        res_dict = json.loads(res)
        self.assertIn("code", res_dict)
        self.assertEqual(res_dict["code"], 1)

    def test_error(self):
        ret = self.client.post("/login", data={"username": "roux", "password": "1"})
        res = ret.data
        res_dict = json.loads(res)
        self.assertIn("code", res_dict)
        self.assertEqual(res_dict["code"], 2)

    def test_success(self):
        ret = self.client.post("/login", data={"username": "roux", "password": "111"})
        res = ret.data
        res_dict = json.loads(res)
        self.assertIn("code", res_dict)
        self.assertEqual(res_dict["code"], 0)


if __name__ == "__main__":
    unittest.main()
