import unittest
import shutil
import jsondb

class C(object):
    def __init__(self, arg):
        self.arg = arg

class A(object):
    def __init__(self, arg):
        self.arg = arg

class RelationalDBTest(unittest.TestCase):
    def setUp(self):
        self.db_path = 'test_db'
        self.db = jsondb.JSONdb(self.db_path)

    def tearDown(self):
        shutil.rmtree(self.db_path)

    def test_relational_model_save(self):
        a = A("Hello")
        c = C(a)
        self.db.add(c)
        got_a = self.relget(A, a="Hello")
        self.assertNotEqual(got_a, [], "A has not been saved correctly, althrough c.arg == a")

    def test_relational_model_load(self):
        self.test_relational_model_save()
        got_c = self.relget(C)
        self.assertNotEqual(got_c, [])
        c = got_c[0]
        self.assertNotEqual(c.arg, None)
        self.assertEqual(c.arg.__class__, A)
        self.assertEqual(c.arg.arg, "Hello")
