def count_words(text):
    wordsInArray = text.split(' ')
    return len(wordsInArray);

def count_chars(text):
    counts = {};
    for c in text:
        if c == ' ' or c == '\n':
            continue;
        # counts[c] += 1 if c in counts else 0
        lowerC = c.lower()
        if lowerC in counts:
            counts[lowerC] += 1
        else:
            counts[lowerC] = 1
    return counts

def get_key(item):
    return item['count']

def sort_counts(counts):
    listOfCounts = [];
    for c in counts:
        charCountDict = { 'char': c,
                          'count': counts[c]
                        }
        listOfCounts.append(charCountDict);
    listOfCounts.sort(reverse=True, key=get_key)
    return listOfCounts;

def print_sorted_report(sortedCounts):
    for c in sortedCounts:
        print(f'{c['char']}: {c['count']}')
