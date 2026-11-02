import unittest
from app import hello_world, welcome_message

class TestHelloWorld(unittest.TestCase):

    def test_hello_world_message(self):
        self.assertEqual(hello_world(), "Hello, DevOps!")

    def test_hello_world_return_type(self):
        self.assertIsInstance(hello_world(), str)

    def test_welcome_message_shashwat(self):
        self.assertEqual(
            welcome_message("Shashwat"),
            "Welcome to DevOps, Shashwat!"
        )

    def test_welcome_message_rahul(self):
        self.assertEqual(
            welcome_message("Rahul"),
            "Welcome to DevOps, Rahul!"
        )

if __name__ == "__main__":
    unittest.main()
