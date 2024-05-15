DNA = []
print("Enter / Paste your  DNA sequences (press Enter to finish):")
while True:
    line = input()
    if line == "":
        break
    DNA.append(line)
result = ''.join(DNA).upper()
mRNA = ''.join([{'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}[i] for i in result])
print(f"mRNA sequence is:  {mRNA}")
