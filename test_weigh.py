import unittest
from app import weigh 


class TestWeigh(unittest.TestCase):

  def test_get_url_correctness(self):
    #Assert
    self.assertNotEqual(True, weigh.Weigh().get_url(url='https://www.npr.org/sections/live-updates-protests-for-racial-justice/2020/07/08/889215893/transcripts-of-police-body-cams-show-floyd-pleaded-20-times-that-he-couldnt-brea'))

  def test_get_url_accuracy(self):
    self.assertIs('https://www.npr.org/sections/live-updates-protests-for-racial-justice/2020/07/08/889215893/transcripts-of-police-body-cams-show-floyd-pleaded-20-times-that-he-couldnt-brea', weigh.Weigh().get_url(url='https://www.npr.org/sections/live-updates-protests-for-racial-justice/2020/07/08/889215893/transcripts-of-police-body-cams-show-floyd-pleaded-20-times-that-he-couldnt-brea'))

  


if __name__ == "__main__":
  unittest.main()
