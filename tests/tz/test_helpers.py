import pytest

from pendulum.tz import timezone
from pendulum.tz.timezone import Timezone, FixedTimezone
from pendulum.tz.zoneinfo.exceptions import InvalidTimezone


def test_timezone_with_name():
    tz = timezone("Europe/Paris")

    assert isinstance(tz, Timezone)
    assert tz.name == "Europe/Paris"


def test_timezone_with_invalid_name():
    with pytest.raises(InvalidTimezone):
        timezone("Invalid")


def test_timezone_with_offset():
    tz = timezone(-19800)

    assert isinstance(tz, FixedTimezone)
    assert tz.name == "-05:30"
