def newsletter_sign_up(name, email):
  if name != "":
    if email != "":
      u = User(name, email)
      newsletter.add(u)    
    else:
      print("The e-mail can't be empty!")
  else:
    print("The name can't be empty!")
