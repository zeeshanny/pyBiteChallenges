from io import StringIO
import os
import sys

from challenge4 import enumerate_names_countries

SCRIPT = os.path.join("/tmp", "enumerate_data.py")


class Capturing(list):
    """Neat: capture print output - found here:
       https://stackoverflow.com/a/16571630"""

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


def test_enumerate_names_countries():
    with Capturing() as output:
        enumerate_names_countries()

    expected = ['1. Julian     Australia',
                '2. Bob        Spain',
                '3. PyBites    Global',
                '4. Dante      Argentina',
                '5. Martin     USA',
                '6. Rodolfo    Mexico']

    assert output == expected


def test_pythonic_idioms():
    with open(SCRIPT) as f:
        content = f.read()

    assert "for" in content, "Need a for loop"
    assert "enumerate" in content, "Best to use enumerate here"
    assert "zip" in content, "Best to use zip here"
