from datetime import datetime


BASE_FORMAT = "%Y-%m-%dT%H:%M:%S"
ISO8601_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
TEST_FORMAT = "%Y_%m_%d__%H_%M_%S"


def parse_datetime(date_time: str, fmt: str = BASE_FORMAT) -> datetime:
    """ Convert the input string of datetime to the formatted datetime. """
    return datetime.strptime(date_time, fmt)


def format_datetime(date_time: datetime, fmt: str = TEST_FORMAT) -> str:
    """ Convert the input datetime or unix timestamp to the formatted string. """
    return date_time.strftime(fmt)
