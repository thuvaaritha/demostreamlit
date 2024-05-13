import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import requests

# Function to retrieve protein data from UniProt
def get_protein_data(uniprot_id, pattern=None):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"  # Fetch protein sequence in FASTA format
    response = requests.get(url)
    protein_sequence = ''
    for line in response.iter_lines():
        line = line.decode("utf-8")
        if not line.startswith('>'):  # Skip header lines
            protein_sequence += line.strip()
    protein_data = {"ID": uniprot_id}  # Initialize with the UniProt ID
    if pattern:
        matches = []
        pattern_length = len(pattern)
        for i in range(len(protein_sequence) - pattern_length + 1):
            if protein_sequence[i:i + pattern_length] == pattern:
                matches.append(i)
        protein_data["Pattern Matches"] = matches
    return protein_data

# Function to display protein characteristics
def display_protein_characteristics(protein_data):
    st.subheader("Protein Characteristics")
    st.write(f"UniProt ID: {protein_data['ID']}")
    if 'Pattern Matches' in protein_data:
        st.write(f"Pattern Matches: {protein_data['Pattern Matches']}")
    else:
        st.write("No matches found for the pattern.")
    # Other characteristics display code remains the same...

# Main function
def main():
    st.title("Protein Data Retrieval and Analysis")
    search_query = st.text_input("Enter UniProt ID to search:")
    pattern = st.text_input("Enter pattern to search in protein sequence (optional):")
    if st.button("Retrieve Data"):
        if search_query:
            protein_data = get_protein_data(search_query, pattern)
            display_protein_characteristics(protein_data)
        else:
            st.write("Please enter a UniProt ID.")

if __name__ == "__main__":
    main()
