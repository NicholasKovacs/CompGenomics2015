__author__ = 'Yuanbo Wang'
#!/usr/bin/env python
import os
import subprocess

# Directory crawling script.
# Locates contig/scaffold FASTA files and invokes Quast to generate assembly metrics.
# Quast metrics files are generated in the respective assembly directories.

inputDirectory_edena = "/home/sim8/assemblyMagicResults/edena/"
inputDirectory_abyss = "/home/sim8/assemblyMagicResults/abyss/"
inputDirectory_spades = "/home/sim8/assemblyMagicResults/spades/"
folders_edena = [os.path.join(inputDirectory_edena,fn) for fn in next(os.walk(inputDirectory_edena))[1]]
folders_abyss = [os.path.join(inputDirectory_abyss,fn) for fn in next(os.walk(inputDirectory_abyss))[1]]
folders_spades = [os.path.join(inputDirectory_spades,fn) for fn in next(os.walk(inputDirectory_spades))[1]]

for folder in folders_edena:
    filePath = folder + "/_contigs.fasta"
    subprocess.call(["/home/agupta399/installation/quast-2.3/quast.py", "-o", folder, filePath])

for folder in folders_spades:
    filePath = folder + "/scaffolds.fasta"
    subprocess.call(["/home/agupta399/installation/quast-2.3/quast.py", "-o", folder, filePath])

for folder in folders_abyss:
    filePath = folder + "/scaffolds.fa"
    subprocess.call(["/home/agupta399/installation/quast-2.3/quast.py", "-o", folder, filePath])