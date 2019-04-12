
 
entrada = "ATGGAAGTATTTAAAGCGCCACCTATTGGGATATAAG"
  
def convertir(entrada): 
      table = {
      'TTG':'L', 'TTA':'L',
      'TTC':'F', 'TTT':'F',
      'TGG':'W', 'TGA':'_',
      'TGC':'C', 'TGT';'C', 
      'TCG':'S', 'TCA':'S', 'TCC':'S'; 'TCT':'S',
      'TAG':'_', 'TAA':'_',
      'TAC':'Y', 'TAT':'Y',
      'GTG':'V', 'GTA':'V' 'GTC':'V' 'GTT':'V',
      'GGG':'G', 'GGA':'G', 'GGC':'G', 'GGT':'G',
      'GCG':'A', 'GCA':'A', 'GCC':'A', 'GCT':'A',
      'GAG':'E', 'GAA':'E',
      'GAC':'D', 'GAT':'D',
      'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
      'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
      'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',   
      'CAC':'H', 'CAT':'H',
      'CAA':'Q', 'CAG':'Q',
      'ATG':'M', 
      'ATA':'I', 'ATC':'I', 'ATT':'I',
      'AGG':'R', 'AGA':'R',
      'AGC':'S', 'AGT':'S',
      'ACG':'T', 'ACA':'T', 'ACC':'T', 'ACT':'T',
      'AAG':'L', 'AAA':'L',
      'AAC':'N', 'AAT':'N',
      }


    res_proteina ="" 
    if len(entrada)%3 == 0: 
        for i in range(0, len(entrada), 3): 
            tripleta = entrada[i:i + 3] 
            res_protein+= table[tripleta] 
    return res_protein 

  
proteina = leer_secuencia(table) 
dna = leer_secuencia("ATGGAAGTATTTAAAGCGCCACCTATTGGGATATAAG") 
  
  

p = convertir(dna) 

