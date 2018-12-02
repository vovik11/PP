from routes import app, db
import unittest, os


class FlaskTest(unittest.TestCase):
    def setUp(self):
        TEST_DB = 'test_cardatabase.db'
        project_dir = os.path.dirname(os.path.abspath(__file__))
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(project_dir, TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    """
    def test_no_page(self):
        response = self.app.get('/no')
        self.assertEqual(response.status_code, 200)
    """

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_page_render(self):
        response = self.app.get('/')
        self.assertIn(b'Car Sharing Service', response.data)

    def test_admin_page(self):
        response = self.app.get('/admin')
        self.assertEqual(response.status_code, 200)

    def test_admin_page_render(self):
        response = self.app.get('/admin')
        self.assertIn(b'Admin Page', response.data)

    def test_user_page(self):
        response = self.app.get('/user')
        self.assertEqual(response.status_code, 200)

    def test_user_page_render(self):
        response = self.app.get('/user')
        self.assertIn(b'User Page', response.data)

    def test_booking_page(self):
        response = self.app.get('/booking')
        self.assertEqual(response.status_code, 200)

    def test_booking_page_render(self):
        response = self.app.get('/booking')
        self.assertIn(b'Booking', response.data)

    def test_return_page(self):
        response = self.app.get('/return')
        self.assertEqual(response.status_code, 200)

    def test_return_page_render(self):
        response = self.app.get('/return')
        self.assertIn(b'Done!', response.data)

    def test_showlist_page(self):
        response = self.app.get('/showList')
        self.assertEqual(response.status_code, 200)

    def test_showlist_page_render(self):
        response = self.app.get('/showList')
        self.assertIn(b'Cars', response.data)

    def test_valid_car_added(self):
        response = self.app.post("/add", data=dict(name="Lada", model="Kalina", engine="1.6", passengers="6"))
        self.assertIn(b'Cars', response.data)


if __name__ == '__main__':
    unittest.main()
