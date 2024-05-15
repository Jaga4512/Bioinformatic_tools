def find_orf_and_translate(sequence):

  start_codon = "AUG"
  stop_codons = ["UAA", "UAG", "UGA"]
  codon_table = {
      "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
      "UCU": "S", "UCC": "S", "UCG": "S", "UCU": "S",
      "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
      "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
      "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
      "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
      "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
      "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
      "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
      "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
      "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
      "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
      "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
      "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
      "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
  }

  # Find the starting index of the ORF
  start_index = sequence.find(start_codon)
  if start_index == -1:
    return "No ORF found"

  # Find the ending index of the ORF
  for i in range(start_index + 3, len(sequence), 3):
    codon = sequence[i:i+3]
    if codon in stop_codons:
      end_index = i + 3
      break
  else:
    return "No ORF found"

  # Check if the ORF length is divisible by 3
  orf_length = end_index - start_index
  if orf_length % 3 != 0:
    return "No ORF found"

  # Translate the ORF to protein sequence
  protein_sequence = ""
  for i in range(start_index, end_index, 3):
    codon = sequence[i:i+3]
    amino_acid = codon_table.get(codon)
    if amino_acid is None:
      return "Invalid mRNA sequence"
    if amino_acid == "Stop":
      break
    protein_sequence += amino_acid

  return protein_sequence

# Example usage
sequence = input("Please enter your sequence: ")
protein_sequence = find_orf_and_translate(sequence)
print(protein_sequence)  # Output: LPF
