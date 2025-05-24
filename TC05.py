# TC05 - Download template after login

open_browser()

open_url("https://24slides.com/login")

fill_field("input email", "user_valid@example.com")
fill_field("input password", "password_valid")

click("login")

if loaded_succesfully() and url_is("dashboard" or "templates"):
  print("Login Success")

  open_url("https://24slides.com/templates/featured")
  scroll_to_element("template to list")

  template = find_element("template item")

  if template:
    element_click(template)

    download_button = find_element("download template")
    if download_button:
      click_button(download_button)
      wait_download()
      print("Download Success")
    else:
      print("Button Not Available")
  else:
    print("Template Not Found")

else:
  print("Login Failed")

