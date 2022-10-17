# This is a sample Python script.
import csv
import re
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fix_glossary(input_filepath, output_filepath):
    input_file = open(input_filepath)
    with open(output_filepath, 'w') as output_file:
        csvwriter = csv.writer(output_file)
        count=0
        while True:
            term = input_file.readline()
            if not term:
                break
            if term != '\n':
                definition = input_file.readline()
                entry = [term.strip(), definition.strip()]
                csvwriter.writerow(entry)
                count +=1
                print(f'Writing term #{count}: {term}')
            else:
                print("Empty line")

    # csvreader = csv.reader(manual_glossary_file)
    # header=next(csvreader)


def fix_questions(input_filepath, output_filepath):
    input_file = open(input_filepath)
    with open(output_filepath, 'w') as output_file:
        csvwriter = csv.writer(output_file, delimiter=";")
        question_line_regex = re.compile('\d+.\s')
        option_line_regex = re.compile('!')
        count=0
        card=""
        options = ['A', 'B', 'C', 'D', 'E', 'F']
        option_count=0
        while True:
            line = input_file.readline()
            if not line:
                card = f'{card}</ul>$'
                entry = [card, "XXXXX"]
                csvwriter.writerow(entry)
                # output_file.write(f'"{card}"')
                count += 1
                print(f'Writing question #{count}:{card}')
                break
            # Line of a question
            if question_line_regex.match(line):
                # Question is finished, then it must be saved.
                if card != "":
                    card = f'{card}</ul>"'
                    entry = [card, "XXXXX"]
                    csvwriter.writerow(entry)
                    #output_file.write(f'"{card}"')
                    count += 1
                    print(f'Writing question #{count}:{card}')
                # Remove the number of question
                line = question_line_regex.sub("", line).strip()
                # Reset the question variable
                card = f'"<p>{line}</p><ul>'
                option_count=0
            # Line corresponding to an option
            elif option_line_regex.match(line):
                # Add the option letter
                line = option_line_regex.sub(f'{options[option_count]}) ', line).strip()
                option_count += 1
                # Append the option to the card
                card = f'{card}<li>{line}</li>'

            else:
                print("################### ERROR LINE ###################")

def fix_questions_2(input_filepath, output_filepath):
    input_file = open(input_filepath)
    with open(output_filepath, 'w') as output_file:
        csvwriter = csv.writer(output_file, delimiter=";")
        question_line_regex = re.compile('^Question [0-9]+:')
        option_line_regex = re.compile('Option [0-9]+:')
        count = 0
        card = ""
        options = ['A', 'B', 'C', 'D', 'E', 'F']
        option_count = 0
        while True:
            line = input_file.readline()
            if not line:
                card = f'{card}</ul>$'
                entry = [card, "XXXXX"]
                csvwriter.writerow(entry)
                # output_file.write(f'"{card}"')
                count += 1
                print(f'Writing question #{count}:{card}')
                break
            # Line of a question
            if question_line_regex.match(line):
                # Question is finished, then it must be saved.
                if card != "":
                    card = f'{card}</ul>"'
                    entry = [card, "XXXXX"]
                    csvwriter.writerow(entry)
                    # output_file.write(f'"{card}"')
                    count += 1
                    print(f'Writing question #{count}:{card}')
                # Remove the number of question
                line = question_line_regex.sub("", line).strip()
                # Reset the question variable
                card = f'"<p>{line}</p><ul>'
                option_count = 0
            # Line corresponding to an option
            elif option_line_regex.match(line):
                # Add the option letter
                line = option_line_regex.sub(f'{options[option_count]}) ', line).strip()
                option_count += 1
                # Append the option to the card
                card = f'{card}<li>{line}</li>'

            else:
                print("################### ERROR LINE ###################")

    # csvreader = csv.reader(manual_glossary_file)
    # header=next(csvreader)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #fix_glossary('/home/rodrigo/Documents/PMP/glossary_delete.txt','/home/rodrigo/Documents/PMP/glossary_fixed.csv')
    #fix_questions('/home/rodrigo/Documents/PMP/mastery_builder_5.txt', '/home/rodrigo/Documents/PMP/mastery_builder_html_5.csv')
    fix_questions_2('/home/rodrigo/Documents/PMP/pmp_questions_2',
                  '/home/rodrigo/Documents/PMP/mastery_builder_html_2.csv')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
