#!/usr/bin/env python

#package imports
import detectionformats.filter

#stdlib imports
import unittest

class TestFilter(unittest.TestCase):
    HIGHPASS = 3.2
    LOWPASS = 1.5
    JSONSTRING = '{"HighPass": 3.2, "LowPass": 1.5}'
    DICT = {"HighPass": 3.2, "LowPass": 1.5}

    def test_init(self):
        # Empty init
        filter = detectionformats.filter.Filter()

        try:
            filter.highPass
            self.assertTrue(False)
        except AttributeError:
            self.assertTrue(True)
            pass

        try:
            filter.lowPass
            self.assertTrue(False)
        except AttributeError:
            self.assertTrue(True)
            pass

        filter = detectionformats.filter.Filter(self.HIGHPASS,
            self.LOWPASS)

        try:
            filter.highPass
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)
            pass

        self.assertEqual(filter.highPass, self.HIGHPASS)

        try:
            filter.lowPass
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)
            pass

        self.assertEqual(filter.lowPass, self.LOWPASS)

    def test_toJSON(self):
        filter = detectionformats.filter.Filter(self.HIGHPASS,
            self.LOWPASS)
        self.assertEqual(filter.toJSONString(), self.JSONSTRING)

    def test_fromJSON(self):
        filter = detectionformats.filter.Filter()
        filter.fromJSONString(self.JSONSTRING)

        self.assertEqual(filter.highPass, self.HIGHPASS)
        self.assertEqual(filter.lowPass, self.LOWPASS)

    def test_toDict(self):
        filter = detectionformats.filter.Filter(self.HIGHPASS,
            self.LOWPASS)
        self.assertEqual(filter.toDict(), self.DICT)

    def test_fromDict(self):
        filter = detectionformats.filter.Filter()
        filter.fromDict(self.DICT)

        self.assertEqual(filter.highPass, self.HIGHPASS)
        self.assertEqual(filter.lowPass, self.LOWPASS)

    def test_isValid(self):
        filter = detectionformats.filter.Filter(self.HIGHPASS,
            self.LOWPASS)
        self.assertTrue(filter.isValid())

    def test_isEmpty(self):
        filter = detectionformats.filter.Filter()
        self.assertTrue(filter.isEmpty())

        filter = detectionformats.filter.Filter(self.HIGHPASS,
            self.LOWPASS)
        self.assertFalse(filter.isEmpty())

if __name__ == '__main__':
    unittest.main()
