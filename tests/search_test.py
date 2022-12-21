# Copyright 2022 Victor I. Afolabi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Set
from typing import Tuple

import pytest
from word_sauce.search import find_word


@pytest.mark.parametrize(
    ('word', 'n', 'expected'),
    (
        ('tests', 4, (3, {'sett', 'test', 'stet'})),
        (
            'apples', 5,
            (
                8, {
                    'apple', 'slape', 'salep', 'saple',
                    'spale', 'speal', 'sepal', 'lapse',
                },
            ),
        ),
        ('lorem', 5, (2, {'morel', 'moler'})),
    ),
)
def test_find_word(
    word: str, n: int, expected: Tuple[int, Set[str]],
) -> None:
    answers = find_word(word, n, None)
    assert len(answers) == expected[0]
    assert answers == expected[1]


@pytest.mark.parametrize(
    ('word', 'n', 'exclude', 'expected'),
    (
        ('tests', 4, {'test'}, (2, {'sett', 'stet'})),
        (
            'apples', 5, {'apple', 'lapse', 'slape'},
            (5, {'salep', 'saple', 'spale', 'speal', 'sepal'}),
        ),
    ),
)
def test_exclude(
    word: str, n: int, exclude: Set[str],
    expected: Tuple[int, Set[str]],
) -> None:
    words = find_word(word, n, exclude)
    assert len(words) == expected[0]
    assert words == expected[1]


@pytest.mark.parametrize(
    ('word', 'n'),
    (
        ('apples', 7),
        ('bananas', 10),
    ),
)
def test_invalid_length(word: str, n: int) -> None:
    with pytest.raises(ValueError):
        find_word(word, n, None)


def test_invalid_word() -> None:
    with pytest.raises(ValueError):
        find_word('', 4, None)


@pytest.mark.parametrize(
    ('word'),
    (
        ('apples'),
        ('bananas'),
    ),
)
def test_length_is_zero(word: str) -> None:
    assert find_word(word, 0, None) == set()
