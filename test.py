try:
    from io import StringIO
    from app import app
    import unittest
    from pyunitreport import HtmlTestRunner
    
    

except Exception as e:
    print("some modules are missing { } ".format(e))


class FlaskTest(unittest.TestCase):
    #check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/db")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


#check if content return is application/jso
def test_index_content(self):
    tester = app.test_client(self)
    response = tester.get("/db")
    self.assertEqual(response.content_type, "application/json")


# check for data returned
def test_index_data(self):
    tester = app.test.client(self)
    response = tester.get("/db")
    self.assertTrue(b'Message' in response.data)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))
