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
import nltk.corpus
from word_sauce.search import find_word


def prompt() -> int:
    print('Word Sauce v0.1')

    word = input('Enter the scrambled word: ')
    n = int(input('Length of the word to find: '))

    words = find_word(word=word, n=n)

    print(f'Possible English words: {len(nltk.corpus.words.words()):,} words')
    print(f'Found {len(words):,} possible words.')
    print(words)

    return 0


if __name__ == '__main__':
    raise SystemExit(prompt())
