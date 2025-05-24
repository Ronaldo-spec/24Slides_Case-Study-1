# TC08 - Password field empty

open_browser()

open_url("https://24slides.com/login")

fill_field("input email", "user_valid@example.com")
fill_field("input password", "")

click("login")

if loaded_succesfully() and url_is("dashboard" or "templates"):
  print("Login Success")
else:
  print("Login Failed")
  if muncul_error("Incorrect password"):
    print("Wrong Password")
else:
    print("No Message")