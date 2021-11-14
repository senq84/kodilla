
def palindrom(word):
  list(word)
  list_of_letters = list(word)
  def check_palindrom(list_of_letters):
    if list_of_letters == list_of_letters[::-1]: 
      print('True')
    else:
      print('False')
  check_palindrom(list_of_letters)

palindrom('kajak')
palindrom('test')
palindrom('kaziu')
palindrom('potop')
palindrom('przypadkowe')