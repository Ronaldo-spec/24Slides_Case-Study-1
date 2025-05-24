# TC04 - Login with Google account


open_browser()

open_url("https://24slides.com/login")

button_click("login with Google")

if oauth_success_and_redirect():
  print("Google Login Success")
else:
  print("Google Login Failed")
  print("Login Failed")