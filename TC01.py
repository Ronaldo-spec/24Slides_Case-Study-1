# TC01 - Login with valid email/password

open_browser()

open_url("https://24slides.com/login")

fill_field("input email", "user_valid@example.com")
fill_field("input password", "password_valid")

click("login")

if loaded_succesfully() and url_is("dashboard" or "templates"):
  print("Login Success")
else:
  print("Login Failed")