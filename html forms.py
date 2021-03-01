import mechanicalsoup

browser = mechanicalsoup.Browser()
loginUrl = "http://olympus.realpython.org/login"
loginPage = browser.get(loginUrl)
loginHtml = loginPage.soup

print(loginPage, loginHtml)

form = loginHtml.form
form.select('input')[0]['value'] = 'zapata'
form.select('input')[1]['value'] = 'alexdarias'

subForm = browser.submit(form, loginPage.url)
print(subForm)

title = subForm.soup.title
print(f"Title: {title.text}")

loginPage = browser.get(loginUrl)
logTitle = loginPage.soup.title
print(f"title: {logTitle.text}")

form = loginHtml.form
form.select('input')[0]['value'] = 'wrong'
form.select('input')[1]['value'] = 'password'
errorPage = browser.submit(form, loginPage.url)

print("Login Failed.") if errorPage.text.find("Wrong username or password!") != 1 else print("Login Successful.")