import sys
import re
import translate
import csv


def translation_filter(pack):
    ru = pack[0].rstrip(' ').rstrip('.')

    return len(ru) > 0


def unpack_translation(pack):
    en = pack[1].rstrip('.')
    ru = pack[0].rstrip(' ').rstrip('.')

    return en, ru


def divide_in_chunks(arr, el_count):
    start = 0
    end = el_count
    length = len(arr)

    while end < length:
        print(start, end)
        yield arr[start:end]
        start = end
        end += el_count

    yield arr[start:]


def translate_to_csv(source, output, source_lang, output_lang):
    words = set()
    words_arr = []
    with open(source, 'r') as file:
        for line in file:
            temp_words = re.split('[\W]', line)
            for word in temp_words:
                word = word.lower()
                if word is not None and not word.isdigit() and len(word) > 2 and word not in words:
                    words.add(word)
                    words_arr.append(word)

    translations = []

    for chunk in divide_in_chunks(words_arr, 100):
        translation_string = ". ".join(chunk)

        translated_result = translate.translator(source_lang, output_lang, translation_string)

        translations.extend(map(unpack_translation,
                                filter(translation_filter, translated_result[0])))

    with open(output, 'w+', encoding='utf-8') as result_csv:
        csv_writer = csv.writer(result_csv, delimiter=',', lineterminator="\n")
        csv_writer.writerows(translations)


def main(params):
    assert len(params) == 4

    source, output, source_lang, output_lang = params
    translate_to_csv(source, output, source_lang, output_lang)


if __name__ == "__main__":
    main(sys.argv[1:])
else:
    translate_to_csv('f:/book.txt', 'translation.csv', 'en', 'uk')
