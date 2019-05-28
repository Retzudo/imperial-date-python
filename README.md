[![Build Status](https://travis-ci.org/Retzudo/imperial-date-python.svg?branch=master)](https://travis-ci.org/Retzudo/imperial-date-python)

This class somewhat implements the [Imperial Dating System](http://warhammer40k.wikia.com/wiki/Imperial_Dating_System).
It's only able to handle dates and completely ignores time.


## Usage

```python
from datetime import date
from imperialdate import ImperialDate

# Create an Imperial Date for today
imperial_date = ImperialDate()

# You can pass date objects
imperial_date = ImperialDate(date(2016, 1, 2))

# You can specify a date class (see WH40k wiki entry)
imperial_date = ImperialDate(date_class=9)
imperial_date = ImperialDate(date(2016, 1, 2), date_class=9)

# The class implements __str__
print("By the Emperor's grace it is {}".format(imperial_date))

# The imperial_date property cotains a tuple of the individual components
date_class, year_fraction, millennium = imperial_date.imperial_date

# You can also compare dates
if ImperialDate(date(2016, 1, 1)) < ImperialDate(date(2016, 1, 2)):
  print('The flow of time is still in order.')

# The regular date is still stored in the instance and can be replaced anytime
regular_date = imperial_date.regular_date
imperial_date.regular_date = date(2017, 12, 31)

# The date class too
date_class = imperial_date.date_class
imperial_date.date_class = 0
```
