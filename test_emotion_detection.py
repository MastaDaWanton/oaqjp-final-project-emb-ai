"""
    Unit tests for the emotion_detector function 
    in the EmotionDetection module.
    This test suite verifies that the emotion_detector 
    function correctly identifies the dominant emotion 
    from a given text input. Each test case checks 
    for a specific emotion.
"""

import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_emotion_detector_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(['dominant_emotion'], "joy")

    def test_emotion_detector_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(['dominant_emotion'], "anger")

    def test_emotion_detector_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(['dominant_emotion'], "disgust")

    def test_emotion_detector_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(['dominant_emotion'], "sadness")

    def test_emotion_detector_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(['dominant_emotion'], "fear")

if __name__ == '__main__':
    unittest.main()
