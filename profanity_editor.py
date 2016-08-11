from urllib.request import urlopen
def check_profanity():
    connection=urlopen("https://en.wikipedia.org/wiki/Eric_Schmidt")
    webtext=connection.read()

    print(webtext)


x="hi shit"
check_profanity()
