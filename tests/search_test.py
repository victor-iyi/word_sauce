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

import pytest

from word_sauce.search import find_word


@pytest.mark.parametrize(
    ('word, n, exclude, expected'),
    (
        ('tests', 4, None, (3, {'sett', 'test', 'stet'})),
    )
)
def test_find_word(
    word: str, n: int, exclude: set[str],
    expected: tuple[int, set[str]]
) -> None:
    answers = find_word(word, n, exclude)
    assert len(answers) == expected[0]
    assert answers == expected[1]
