
def palindrom(text):
  alphanum = ''.join(ch for ch in text if ch.isalnum())
  lower_letters = alphanum.lower()
  list_of_letters = list(lower_letters)
  if (list_of_letters == list_of_letters[::-1]):    
    return True 
  else:
    return False

print(palindrom('Turb22 Burbon,erer'))
print(palindrom('Kajak'))
print(palindrom('kajak'))
print(palindrom('test'))
print(palindrom('kaziu uizak'))
print(palindrom('potop'))
print(palindrom('przypadkowe'))
print(palindrom('Turb022-_ Burbon,ererp'))
print(palindrom('alphanumeric@ 123__'))
print(palindrom('"Kobyła ma mały bok!"'))
