"""
MIT License

Copyright (c) 2022-present japandotorg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import datetime
import time
from collections.abc import Callable, Mapping, Sequence
from decimal import Decimal
from typing import Any, TypeVar
from typing_extensions import TypeAlias

_EscaperMapping: TypeAlias = Mapping[type[object], Callable[..., str]] | None
_T = TypeVar("_T")

def escape_item(val: object, charset: object, mapping: _EscaperMapping = ...) -> str: ...
def escape_dict(val: Mapping[str, object], charset: object, mapping: _EscaperMapping = ...) -> dict[str, str]: ...
def escape_sequence(val: Sequence[object], charset: object, mapping: _EscaperMapping = ...) -> str: ...
def escape_set(val: set[object], charset: object, mapping: _EscaperMapping = ...) -> str: ...
def escape_bool(value: bool, mapping: _EscaperMapping = ...) -> str: ...
def escape_int(value: int, mapping: _EscaperMapping = ...) -> str: ...
def escape_float(value: float, mapping: _EscaperMapping = ...) -> str: ...
def escape_string(value: str, mapping: _EscaperMapping = ...) -> str: ...
def escape_bytes_prefixed(value: bytes, mapping: _EscaperMapping = ...) -> str: ...
def escape_bytes(value: bytes, mapping: _EscaperMapping = ...) -> str: ...
def escape_str(value: str, mapping: _EscaperMapping = ...) -> str: ...
def escape_None(value: None, mapping: _EscaperMapping = ...) -> str: ...
def escape_timedelta(obj: datetime.timedelta, mapping: _EscaperMapping = ...) -> str: ...
def escape_time(obj: datetime.time, mapping: _EscaperMapping = ...) -> str: ...
def escape_datetime(obj: datetime.datetime, mapping: _EscaperMapping = ...) -> str: ...
def escape_date(obj: datetime.date, mapping: _EscaperMapping = ...) -> str: ...
def escape_struct_time(obj: time.struct_time, mapping: _EscaperMapping = ...) -> str: ...
def Decimal2Literal(o: Decimal, d: object) -> str: ...
def convert_datetime(obj: str | bytes) -> datetime.datetime | str: ...
def convert_timedelta(obj: str | bytes) -> datetime.timedelta | str: ...
def convert_time(obj: str | bytes) -> datetime.time | str: ...
def convert_date(obj: str | bytes) -> datetime.date | str: ...
def through(x: _T) -> _T: ...

convert_bit = through

encoders: dict[type[object], Callable[..., str]]
decoders: dict[int, Callable[[str | bytes], Any]]
conversions: dict[type[object] | int, Callable[..., Any]]
Thing2Literal = escape_str
