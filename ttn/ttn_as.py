# The MIT License (MIT)
#
# Copyright (c) 2018 Brent Rubell for Adafruit
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`ttn_as.py`
======================================================
AS920 The Things Network Frequency Plans
* Author(s): Brent Rubell
"""
TTN_FREQS = {0: (0xe6, 0xCC, 0xF4), # 868.1 MHz
             1: (0xe6, 0xD9, 0xC0), # 868.3 MHz
             2: (0xe6, 0x8C, 0xF3), # 863.5 MHz
             3: (0xe6, 0x99, 0xC0), # 867.1 MHz
             4: (0xe6, 0xA6, 0x8D), # 867.3 MHz
             5: (0xe6, 0xB3, 0x5A), # 867.5 MHz
             6: (0xe6, 0xC0, 0x27), # 867.7 MHz
             7: (0xe6, 0x80, 0x27)} # 867.9 MHz
