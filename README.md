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

A program to play the mobile game "Word Sauce".

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
$ python main.py -w tlepoi -n 4
Word Sauce v0.1
Possible English words: 236,736 words
Possible English words: 236,736 words
Searching for 4-letter word in 360 possible words.

Found 23 possible words.
{'peto', 'piet', 'pelt', 'tipe', 'teli', 'topi', 'pole', 'ilot', 'lite', 'teil', 'tope', 'plot', 'olpe', 'tile', 'pile', 'poet', 'polt', 'pote', 'lope', 'toil', 'tole', 'poil', 'lote'}
```

If you require a prompt, then run `prompt.py` instead.

```sh
$ python prompt.py
Word Sauce v0.1
Enter the scrambled word: tlepoi
Length of the word to find: 4
Possible English words: 236,736 words
Searching for 4-letter word in 360 possible words.

Found 23 possible words.
{'tipe', 'plot', 'lote', 'pote', 'piet', 'pile', 'pole', 'toil', 'olpe', 'teil', 'tope', 'tile', 'topi', 'lite', 'polt', 'lope', 'poet', 'peto', 'teli', 'pelt', 'poil', 'ilot', 'tole'}
```

## Contribution

You are very welcome to modify and use them in your own projects.

Please keep a link to the [original repository]. If you have made a fork with substantial modifications that you feel may be useful, then please [open a new issue on GitHub][issue] with a link and short description.

[original repository]: https://https://github.com/victor-iyi/word_sauce
[issue]: https://github.com/victor-iyi/word_sauce/issues

## License (Apache 2.0)

This project is opened under the [Apache 2.0](./LICENSE) which allows very broad use for both private and commercial purposes.

A few of the images used for demonstration purposes may be under copyright. These images are included under the "fair useage" laws.
