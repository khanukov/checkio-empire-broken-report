from checkio_referee import RefereeCodeGolf
from checkio_referee import covercodes


import settings_env
from tests import TESTS

# TODO Golf


class Referee(RefereeCodeGolf):
    DEFAULT_MAX_CODE_LENGTH = 150
    BASE_POINTS = 15
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "golf"
    ENV_COVERCODE = {
        "python_2": covercodes.py_2_str,
        "python_3": None,
        "javascript": None
    }
