import unnitest
from datetime import datetime

class TestBaseModel(unittest.TestCase):
     def initialize(self):
         self.real_model = BaseModel()
         self.assertIsInstance(real_model.id, str)
         self.assertIsInstance(real_model.created_at, datetime)
         self.assertIsInstance(real_model.upsated_at, datetime)

    def test_save_way(self):

