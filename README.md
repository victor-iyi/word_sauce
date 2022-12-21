<!--
 Copyright 2022 Victor I. Afolabi

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->

# Word Sauce

[![style | google](https://img.shields.io/badge/%20style-google-3666d6.svg)](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)
![GitHub](https://img.shields.io/github/license/victor-iyi/word_sauce)

A program to play the mobile game [Word Sauce].

[Word Sauce]: https://www.crazygames.com/game/word-sauce

## Usage

Run the main script with the word and the length of word you're looking to find.

```sh
$ python main.py -h
usage: main.py [-h] --word WORD -n N [--exclude EXCLUDE [EXCLUDE ...]]

Play the Word Sauce game.

options:
  -h, --help            show this help message and exit
  --word WORD, -w WORD  The word list to use. (default: None)
  -n N                  The length of the word to find. (default: None)
  --exclude EXCLUDE [EXCLUDE ...], -e EXCLUDE [EXCLUDE ...]
                        Words to exclude from the search. (default: None)
```

For example:

```sh
$ python main.py -w lorem -n 4
Word Sauce v0.1
Possible English words: 236,736 words
Searching for 4-letter word in 120 possible words.

Found 8 possible words.
{'merl', 'orle', 'mole', 'omer', 'mero', 'more', 'lore', 'role'}
```

If you require a prompt, then run `prompt.py` instead.

```sh
$ python prompt.py
Word Sauce v0.1
Enter the scrambled word: lorem
Length of the word to find: 4
Possible English words: 236,736 words
Searching for 4-letter word in 360 possible words.

Found 8 possible words.
{'merl', 'orle', 'mole', 'omer', 'mero', 'more', 'lore', 'role'}
```

## Troubleshooting

If `nltk` fails to load `corpora/words`, run the following command to download
the resource.

```sh
python3 -m nltk.downloader words
```

For more information, visit <https://www.nltk.org/data.html>.

## Contribution

You are very welcome to modify and use them in your own projects.

Please keep a link to the [original repository]. If you have made a fork with
substantial modifications that you feel may be useful, then please
[open a new issue on GitHub][issue] with a link and short description.

[original repository]: https://https://github.com/victor-iyi/word_sauce
[issue]: https://github.com/victor-iyi/word_sauce/issues

## License (Apache 2.0)

This project is opened under the [Apache 2.0](./LICENSE) which allows very broad
use for both private and commercial purposes.

A few of the images used for demonstration purposes may be under copyright.
These images are included under the "fair useage" laws.
