# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2020 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_fakerequests`
================================================================================

Fake Network Requests helper that retrieves data from a local file.


* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

import json

try:
    from typing import Any
except ImportError:
    pass

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FakeRequests.git"


class Fake_Requests:
    """For faking 'requests' using a local file instead of the network."""

    def __init__(self, filename: str) -> None:
        self._filename = filename

    def json(self) -> Any:
        """json parsed version for local requests."""
        with open(self._filename, "r") as file:
            return json.load(file)

    @property
    def text(self) -> str:
        """raw text version for local requests."""
        with open(self._filename, "r") as file:
            return file.read()
