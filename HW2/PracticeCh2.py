#Given a DNA Genome

DNA="CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"

#Return all integer(s) i minimizing skew(prefixi(Text)) over all values of i (from 0 to | Genome|)

complement = { 'A':'T', 'C':'G', 'G':'C', 'T':'A' }
s = "ATCTGTATAACGAATATATACATTATC"
rcs = ''.join( map( lambda c: complement[c] , reversed(s) ) )

print rcs

def fun( r ):
  if r == red:
    return False
  else:
    return True

# Filter a sequence returning only G's or C's
chk = { 'A':False, 'C':True, 'G':True, 'T':False }
s = "ATCTGTATAACGAATATATACATTATC"
filtered_s = filter( lambda c: chk[c] , s )
print filtered_s


# Reduce a sequence to a count of each base pair
bp_counts = { 'A':0, 'C':0, 'G':0, 'T':0 }

def countit( acc, c ) : 
	acc[c] += 1
	return acc


reduce( countit, s, bp_counts )
print bp_counts

#word = 'Python'
#print word[0]  # character in position 0