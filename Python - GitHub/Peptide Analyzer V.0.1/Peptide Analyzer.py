import pandas as pd

peptides_lib = pd.read_excel('Peptides Sample - JAK3.xlsx')


info = peptides_lib.info()
head = peptides_lib.head()

#print(info)
#print(head)

peptides_sequence = peptides_lib['Annotated Amino Acid Sequence']

peptides_lenght = peptides_lib['length (aa)']

peptides_lenght_mean = peptides_lib['length (aa)'].mean()

peptides_lenght_max = peptides_lenght.max()

peptides_lenght_max_seq = peptides_lib[peptides_lib['length (aa)'] == 31 ]['Annotated Amino Acid Sequence']

print(peptides_lenght_max)

