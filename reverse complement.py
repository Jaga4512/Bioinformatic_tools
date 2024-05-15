DNA = []
print("Enter / Paste your  DNA sequences (press Enter to finish):")
while True:
    line = input()
    if line == "":
        break
    DNA.append(line)
result = ''.join(DNA)
compdna = ''.join([{'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}[i] for i in result])
reversecomp = compdna[::-1]
print(f"Complementory DNA:  {compdna}")
print(f"Reverse complementory DNA:  {reversecomp}")