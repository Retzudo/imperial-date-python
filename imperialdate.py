"""
Takes a datetime.date object and converts it to
a Warhammer 40,000 lore friendly version.
E. g. 2016-6-23 -> '0 478 016.M3'
"""
from datetime import date
from functools import total_ordering


@total_ordering
class ImperialDate:
    """
    Takes a datetime.date object and converts it to
    a Warhammer 40,000 lore friendly version.
    E. g. 2016-6-23 -> '0 478 016.M3'
    """
    MIN_DATE_CLASS = 0
    MAX_DATE_CLASS = 9

    def __init__(self, d=None, date_class=0):
        self._date = None
        self._date_class = None
        self.date_class = date_class

        if d is None:
            self.regular_date = date.today()
        else:
            self.regular_date = d

    @staticmethod
    def _check_date(d):
        if not isinstance(d, date):
            raise ValueError('Argument must of type datetime.date')

    def _get_millennium_part(self):
        """Construct the millennium part for the date.

        We just take the current year as a string, take
        the last 3 characters, then '.M' and then the remaining
        characters of the date + 1 because millennia are counted
        just like centuries: 2016 = 21st century, 3rd millennium.
        E. g. 2016: '016' + '.M' + '3' = '016.M3'
        If Python supported years > 9999 we could actually
        use dates from the grim, dark future:
        40,999: '999' + '.M' = '999.M41'
        """
        year = str(self._date.year)
        return '{}.M{}'.format(year[-3:], int(year[:-3])+1)

    def _get_year_fraction(self):
        """Calculate the current "position" in this year.

        The number calculated is a number between 0 and 1
        which represents the "position" of the date's day
        in its year where 0 is 1-1, 1 is 12-31 and somewhere
        between June and July should be 0.5.
        We multiply that value by 1000 because we need a number
        between 0 and 1000 for the canonical WH40k date.
        """
        days_this_year = int(date(self._date.year, 12, 31).strftime('%j'))
        day_number = int(self._date.strftime('%j'))

        return (day_number / days_this_year) * 1000

    @property
    def imperial_date(self):
        if date is None:
            return None

        return (
            self.date_class,
            self._get_year_fraction(),
            self._get_millennium_part()
        )

    @property
    def regular_date(self):
        return self._date

    @regular_date.setter
    def regular_date(self, d):
        self._check_date(d)
        self._date = d

    @property
    def date_class(self):
        return self._date_class

    @date_class.setter
    def date_class(self, date_class):
        if (isinstance(date_class, int) and
                ImperialDate.MIN_DATE_CLASS <=
                date_class <= ImperialDate.MAX_DATE_CLASS):
            self._date_class = date_class
        else:
            raise ValueError(
                'Date class must be between {} and {}, was {}'.format(
                    ImperialDate.MIN_DATE_CLASS,
                    ImperialDate.MAX_DATE_CLASS,
                    date_class
                )
            )

    def __str__(self):
        date_class, year_fraction, millennium = self.imperial_date
        return '{} {:0>0} {}'.format(
            date_class,
            int(year_fraction),
            millennium
        )

    def __repr__(self):
        return '<{} {}>'.format(self.__class__, self.__str__())

    def __lt__(self, other):
        return self.regular_date < other.regular_date

    def __eq__(self, other):
        return self.regular_date == other.regular_date
