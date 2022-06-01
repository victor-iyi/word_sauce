import argparse
import nltk

from search import find_word


def run(args: argparse.Namespace) -> None:
    exclude = args.exclude and set(args.exclude)
    words = find_word(word=args.word, n=args.n, exclude=exclude)
    print(f'Found {len(words):,} possible words.')
    print(words)


def main() -> int:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Play the Word Sauce game.'
    )

    parser.add_argument('--word', '-w', type=str, required=True,
                        help='The word list to use.')
    parser.add_argument('-n', type=int, required=True,
                        help='The length of the word to find.')
    parser.add_argument('--exclude', '-e', type=str, nargs='+', default=None,
                        help='Words to exclude from the search.')

    args = parser.parse_args()

    print(f'Word Sauce v0.1')
    print(f'Possible English words: {len(nltk.corpus.words.words()):,} words')

    run(args)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
