from django.test import TestCase
from drone.models import DroneModel, CategoryModel, BrandModel
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile

class DroneModelTestCase(TestCase):
    def setUp(self):
        # Create a temporary image file
        self.temp_image = tempfile.NamedTemporaryFile(suffix=".jpg")

        # Create a simple uploaded file object
        self.image_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',  # Specify the content here, for example a byte array
            content_type='image/jpeg'
        )

    def tearDown(self):
        self.temp_image.close()

    def test_image_upload(self):
        # Create mockup and upload image
        category = CategoryModel.objects.create(title='Test Category')
        brand = BrandModel.objects.create(title='Test Brand')

        my_image_model = DroneModel.objects.create(
            name='Test Image',
            image=self.image_file,
            category=category,
            description='Test',
            equipment=['Test Equipment','Test Equipment'],
            price=0.0,
            status=True,
            brand=brand,
        )
        self.assertTrue(DroneModel.objects.filter(name='Test Image').exists())

        # Check if the image is actually saved
        self.assertEqual(my_image_model.image.name, 'media/drone/test_image.jpg')
