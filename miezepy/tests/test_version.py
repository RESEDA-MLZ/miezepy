import unittest
import miezepy

class Test_launch(unittest.TestCase):


    def test_launch_version(self):
        self.assertEqual(miezepy.__version__,'0.5.0')


    # @unittest.skipIf(platform == "linux" or platform == "linux2",
    #                 reason="requires xbc")
    # def test_launch_blank_gui(self):
    #     app = Mieze(GUI = True)
    #     self.assertTrue(app.success)