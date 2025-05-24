# TC07 - Login with invalid email format

open_browser()

open_url("https://24slides.com/login")

fill_field("input email", "tes123@gmail")
fill_field("input password", "password_valid")

click("login")

if loaded_succesfully() and url_is("dashboard" or "templates"):
  print("Login Success")
else:
  print("Login Failed")
  if muncul_error("Email Field is Empty"):
    print("Fill Required")
  else:
    print("No Message")