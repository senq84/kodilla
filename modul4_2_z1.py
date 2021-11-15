
def palindrom(text):
  alphanum = ''.join(ch for ch in text if ch.isalnum())
  lower_letters = alphanum.lower()
  list_of_letters = list(lower_letters)
  if (list_of_letters == list_of_letters[::-1]):    
#    return True 
    print(f'true {text}')
  else:
#    return False
    print('false')

palindrom('Turb22 Burbon,erer')
palindrom('Kajak')
palindrom('kajak')
palindrom('test')
palindrom('kaziu uizak')
palindrom('potop')
palindrom('przypadkowe')
palindrom('Turb022-_ Burbon,ererp')
palindrom('alphanumeric@ 123__')
palindrom('"Kobyła ma mały bok!"')