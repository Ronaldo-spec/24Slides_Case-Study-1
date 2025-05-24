# TC06 - Download template without login

open_url("https://24slides.com/templates/featured")
scroll_to_element("template to list")

template = find_element("template item")

if template:
  element_click(template)

  download_button = find_element("download template")
  if download_button:
    click_button(download_button)
    if pop_up("sign up first") or login_page():
      print("Login or Sign up to Download")
    else:
      print("bug?")
  else:
    print("Button Not Available")
else:
  print("Template Not Found")