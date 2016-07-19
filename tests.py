import unittest
from datetime import date
from imperialdate import ImperialDate


class DateTest(unittest.TestCase):
    def test_check_date(self):
        with self.assertRaises(ValueError):
            ImperialDate._check_date('TEST')
        with self.assertRaises(ValueError):
            ImperialDate._check_date(123)

        ImperialDate._check_date(date.today())

    def test_get_millenium_part(self):
        imperial_date = ImperialDate(date(2016, 1, 1))
        self.assertEqual(imperial_date._get_millennium_part(), '016.M3')

        imperial_date = ImperialDate(date(5098, 12, 25))
        self.assertEqual(imperial_date._get_millennium_part(), '098.M6')

    def test_get_year_fraction(self):
        imperial_date = ImperialDate(date(2016, 6, 30))
        year_fraction = imperial_date._get_year_fraction()
        self.assertTrue(490 < year_fraction < 510)

        imperial_date.regular_date = date(2016, 1, 1)
        year_fraction = imperial_date._get_year_fraction()
        self.assertTrue(0 < year_fraction < 5)

    def test_date_class(self):
        imperial_date = ImperialDate()
        with self.assertRaises(ValueError):
            imperial_date.date_class = -1
        with self.assertRaises(ValueError):
            imperial_date.date_class = 13
        with self.assertRaises(ValueError):
            imperial_date.date_class = 'ASDF'

    def test_imperial_date(self):
        imperial_date = ImperialDate(date(4065, 4, 30), 1)

        date_class, year_fraction, milennium = imperial_date.imperial_date
        self.assertEqual(date_class, 1)
        self.assertTrue(0 < year_fraction < 1000)
        self.assertEqual(milennium, '065.M5')

    def test_default_init(self):
        imperial_date = ImperialDate()
        self.assertEqual(imperial_date.regular_date, date.today())

    def test_ordering(self):
        date_one = ImperialDate(date(2016, 1, 1))
        date_two = ImperialDate(date(2017, 4, 5))

        self.assertLess(date_one, date_two)
        self.assertEqual(ImperialDate(), ImperialDate())


if __name__ == '__main__':
    unittest.main()