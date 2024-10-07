import requests

# Base URL for UniProt API
base_url = 'https://www.uniprot.org/uniprot/'

# Function to fetch and parse the description line from FASTA
def fetch_description(accession):
    url = f'{base_url}{accession}.fasta'
    response = requests.get(url)
    if response.status_code == 200:
        fasta_data = response.text
        description_line = fasta_data.split('\n')[0]
        return description_line
    else:
        return f'Error: {response.status_code} for accession {accession}'

# Read fasta file and get the accessions for every protein, get the description line and write back
# to a new fasta file.

with open('contaminants-202105_uniprot.fasta', 'r') as file:
    f = open('contaminants-202105_uniprot_description.fasta', 'w')
    # Read the contaminants file
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            id_arr = line.split('|')[1]
            accession = id_arr.replace("CONTAMINANT_", "")
            # Fetch the description line
            description = fetch_description(accession)
            description = description.split(' ')[1:]
            accession = line + ' ' + ' '.join(description)
            f.write(f'{accession}\n')
        else:
            f.write(f'{line}\n')

f.close()