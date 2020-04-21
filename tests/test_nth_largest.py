from typing import (MutableSequence,
                    Tuple)

from hypothesis import given

from quickselect.base import nth_largest
from quickselect.hints import (Domain,
                               Key)
from . import strategies


@given(strategies.elements_lists_with_index, strategies.keys)
def test_properties(elements_with_index: Tuple[MutableSequence[Domain], int],
                    key: Key) -> None:
    elements, index = elements_with_index

    result = nth_largest(elements, index,
                         key=key)

    assert result in elements
    assert sorted(elements,
                  reverse=True,
                  key=key)[index] == result


@given(strategies.elements_lists, strategies.keys)
def test_first(elements: MutableSequence[Domain],
               key: Key) -> None:
    result = nth_largest(elements, 0,
                         key=key)

    assert result == (max(elements)
                      if key is None
                      else max(elements,
                               key=key))


@given(strategies.elements_lists, strategies.keys)
def test_last(elements: MutableSequence[Domain],
              key: Key) -> None:
    result = nth_largest(elements, len(elements) - 1,
                         key=key)

    assert result == (min(elements)
                      if key is None
                      else min(elements,
                               key=key))
