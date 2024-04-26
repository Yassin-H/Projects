import csv
from urllib.parse import urlparse
import os

def extract_lexical_features(url):
    parsed_url = urlparse(url)
    lexical_features = {
        'URL_length': len(url),
        'Has_http': 1 if parsed_url.scheme == 'http' else 0,
        'Has_https': 1 if parsed_url.scheme == 'https' else 0,
        'Count_dots': url.count('.'),
        'Count_dashes': url.count('-'),
        'Count_underscores': url.count('_'),
        'Count_slashes': url.count('/'),
        'Count_ques': url.count('?'),
        'Count_non_alphanumeric': sum(1 for c in url if not c.isalnum()),
        'Count_digits': sum(1 for c in url if c.isdigit()),
        'Count_letters': sum(1 for c in url if c.isalpha()),
        'Count_params': len(parsed_url.params.split(';')),
        'Has_php': 1 if 'php' in url else 0,
        'Has_html': 1 if 'html' in url else 0,
    }
    return lexical_features

def process_csv(input_csv_file, output_folder):
    output_csv_file = os.path.join(output_folder, "lexical_features.csv")
    with open(input_csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        lexical_feature_keys = extract_lexical_features(header[0]).keys()
        header.extend(lexical_feature_keys)

        rows = [header]

        for row in reader:
            url = row[0]
            lexical_features = extract_lexical_features(url)
            row.extend(lexical_features[key] for key in lexical_feature_keys)
            rows.append(row)

    # Writing results to a new CSV file
    with open(output_csv_file, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Output CSV file created successfully:", output_csv_file)

if __name__ == "__main__":
    input_csv_file = input("Enter the path of the input CSV file: ")
    output_folder = input("Enter the path for the output folder: ")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    process_csv(input_csv_file, output_folder)


