def newsletter_sign_up(name, email):
  if name == "":
    print("The name can't be empty!")
    return
  if email == "":
    print("The e-mail can't be empty!")
    return
  u = User(name, email)
  newsletter.add(u)
