import re
import argparse


def convert_uniprot_accession(accession):
    # Remove '_p_target' and replace 'sp|' with 'ENTRAP_sp|ENTRAP_'
    modified_accession = re.sub(r'_p_target', '', accession)
    modified_accession_arr = modified_accession.split('|')
    if len(modified_accession_arr) != 3:
        raise ValueError(f"Invalid UniProt accession: {accession}")
    if '>sp' != modified_accession_arr[0]:
        raise ValueError(f"Invalid UniProt accession: {accession}")
    modified_accession_arr[1] = 'ENTRAP_' + modified_accession_arr[1]
    modified_accession_arr[2] = 'ENTRAP_' + modified_accession_arr[2]
    modified_accession = '|'.join(modified_accession_arr)

    return modified_accession


def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Remove any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:  # Proceed if the line is not empty
                if "_p_target" in line:
                    line = convert_uniprot_accession(line)
                outfile.write(line + '\n')


def main():
    parser = argparse.ArgumentParser(description="Convert UniProt accessions in a file.")
    parser.add_argument('input_file', help="Path to the input file containing UniProt accessions.")
    parser.add_argument('output_file', help="Path to the output file to save converted accessions.")

    args = parser.parse_args()

    process_file(args.input_file, args.output_file)


if __name__ == "__main__":
    main()