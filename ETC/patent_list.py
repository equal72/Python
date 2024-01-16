def extract_info(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.read().split('\n')

    info = []
    title, patent_number, date_of_patent, inventors = None, None, None, None

    for line in data:
        if line.startswith('Title:'):
            title = line.replace('Title:', '')
        if line.startswith('Title:  '):
                title = line.replace('Title:', '')
        elif line.startswith('Patent number: '):
            patent_number = line.replace('Patent number: ', '')
        elif line.startswith('Publication number: '):
            patent_number = line.replace('Publication number: ', '')
        elif line.startswith('Date of Patent: '):
            date_of_patent = line.replace('Date of Patent: ', '')
        elif line.startswith('Inventors: '):
            inventors = line.replace('Inventors: ', '')
            info.append(f"{title}, {patent_number}, {date_of_patent}, {inventors}")
            title, patent_number, date_of_patent, inventors = None, None, None, None

    return info

def write_to_file(output_file, data):
    with open(output_file, 'w', encoding='utf-8') as file:
        for item in data:
            file.write("%s\n" % item)

info = extract_info('inputfile.txt')
write_to_file('outputfile.txt', info)
