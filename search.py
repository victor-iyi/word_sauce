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

import itertools
import nltk

from typing import Optional
from typing import Set


def find_word(
    word: str,
    n: int,
    exclude: Optional[Set[str]] = None
) -> Set[str]:
    english_words = nltk.corpus.words.words()
    possible_words = [''.join(w)
                      for w in itertools.permutations(word, n)]

    print(f'Possible English words: {len(english_words):,} words')
    print(f'Searching for {n}-letter word in '
          f'{len(possible_words):,} possible words.\n')

    answers = set()

    for possible_word in possible_words:
        if possible_word in english_words:
            if exclude is not None and possible_word in exclude:
                continue
            answers.add(possible_word)

    return answers
