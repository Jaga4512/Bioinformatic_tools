def find_orf(sequence):

  start_codon = "AUG"
  stop_codons = ["UAA", "UAG", "UGA"]

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

  orf_length = end_index - start_index
  if orf_length % 3 == 0:
    return str(orf_length)
  else:
    return "No ORF found"

sequence = input("Please enter your sequence: ")
orf_length = find_orf(sequence)
print("The ORF length is:", orf_length)  # Output: 9
