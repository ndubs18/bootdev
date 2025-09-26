from stats import count_words, count_chars, sort_counts \
    ,print_sorted_report

BOOK_PATH = 'books/frankenstein.txt'

def main():

    print('============ BOOKBOT ============');
    print(f'Analyzing book found at {BOOK_PATH}...')
    text = get_book_text(BOOK_PATH);
    wordCount = count_words(text);

    print('----------- Word Count ----------')
    print(f"Found {wordCount} total words")

    counts = count_chars(text)
    sortedCounts = sort_counts(counts)
    print_sorted_report(sortedCounts);

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as text:
        return text.read()

# entrypoint
main();

