import os, webbrowser

#Open a web browser with a designated URL which the
#user inputs.

#create a while loop for the application to run until
#the user finishes executing their inputs.

#Will not load "shady" sites, if I have time


#Python 2.7.x

run_program = True
print("\n\n\nUse the terminal to load up a link to your web browser!\n\n\n")

while run_program:
    #prompt user to input a website link
    webDirectory = raw_input("Please enter a website link below.\nExample: (google)\n").lower()
    #I'm not sure if it's required to implement an HTTPS extension but I wil
    #implement it for security reasons
    hasHTTPS = "https://"
    #Just to make things easier, I'll hard code the domain names
    domainNames = ['.com', '.gov', '.edu', '.net', '.us', '.co', '.org']
    #create a test case
    dName = raw_input("What is the domain name?\nExample: (.com, .gov, .edu, .net, .us, .co, .org)\n")

    check = True

    while check:
        if dName == domainNames[0]:
            print("Checking link...")
            webName = hasHTTPS + webDirectory + dName
            check = False
        elif dName == domainNames[1]:
            print("Checking link...")
            webName = hasHTTPS + webDirectory + dName
            check = False
        elif dName == domainNames[2]:
            print("Checking link...")
            webName = hasHTTPS + webDirectory + dName
            check = False
        elif dName == domainNames[3]:
            print("Checking link...")
            webName = hasHTTPS + webDirectory + dName
            check = False
        elif dName == domainNames[4]:
            print("Checking link...")
            webName = hasHTTPS + webDirectory + dName
            check = False
        elif dName == domainNames[5]:
            print("Checking link...")
            webName = hasHTTPS + webDirectory + dName
            check = False
        elif dName == domainNames[6]:
            print("Checking link...")
            webName = hasHTTPS + webDirectory + dName
            check = False
        else:
            print("Invalid link... Check if the domain name is available.")
            check = True

    print("Website typed: " + webName + "\n\n\n")

    user_browser = raw_input("Which browser would you like to use?\nAvailable browsers below...\nChrome, Firefox, Safari (Mac OSX), Edge (Windows)\nMUST BE CASE SENSITIVE\n")

    browserApps = ["Chrome", "Firefox" , "Safari", "Edge"]

    check2 = True
    while check2:
        if user_browser == browserApps[0]:
            print("Loading " + str(browserApps[0]) + "...")
            webbrowser.get(str(browserApps[0]).lower()).open(webName)
            print("Success!")
            check2 = False
        elif user_browser == browserApps[1]:
            print("Loading " + str(browserApps[1]) + "...")
            webbrowser.get(str(browserApps[1]).lower()).open(webName)
            print("Success!")
            check2 = False
        elif user_browser == browserApps[2]:
            print("Loading " + str(browserApps[2]) + "...")
            webbrowser.get(str(browserApps[2]).lower()).open(webName)
            print("Success!")
            check2 = False
        elif user_browser == browserApps[3]:
            print("Loading " + str(browserApps[3]) + "...")
            webbrowser.get('windows-default').open(webName)
            print("Success!")
            check2 = False
        else:
            print("Invalid web browser... Choose another one.")
            check2 = True
            run_program = True

    run_program = False

exit();
