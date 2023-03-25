import os
import pikepdf
import itertools

# encrypted PDF file
encrypted_pdf_file = "./encrypted_pdf_file.pdf"

# PDF file not encrypted
pdf_file = "./pdf_file.pdf"

# your password charset
charset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# charset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# password len
password_len = 6
permutations = itertools.permutations(charset, password_len)

for p in permutations:
    s = ''.join(p)
    try:
        pdf = pikepdf.open(encrypted_pdf_file,password=s)
        pdf.save(pdf_file)
        print("password is:", s)
        break
    except Exception as e:
        a = 0