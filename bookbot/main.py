import sys
from stats import count_words, count_chars, sort_counts \
    ,print_sorted_report

def main():
    if len(sys.argv) < 2:
        print('python3 main.py <path_to_book>')
        sys.exit(1)
    bookPath = sys.argv[1]
    print('============ BOOKBOT ============');
    print(f'Analyzing book found at {bookPath}...')
    text = get_book_text(bookPath);
    wordCount = count_words(text);

    print('----------- Word Count ----------')
    print(f"Found {wordCount} total words")

    counts = count_chars(text)
    sortedCounts = sort_counts(counts)
    print_sorted_report(sortedCounts);

def get_book_text(path):
    try:
        with open(path, 'r', encoding='utf-8') as text:
            return text.read()
    except FileNotFoundError:
        print('File not found')
    except PermissionError:
        print("You don't have permission to read this file.")
    except Exception as e:
        (f'An unexpected error occurred: {e}')

# entrypoint
main();

