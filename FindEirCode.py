from playwright.sync_api import sync_playwright

# Input Fields
address = input("Please Enter in Address: ")
headless = input("Display Browser yes or no? ").lower()

with sync_playwright() as p:
    
    # Display Browser
    if headless == "yes":
        browser = p.firefox.launch(headless=False)
    else:
        browser = p.firefox.launch(headless=True)
        print("Processing Request")
    
    #Open up Page
    page = browser.new_page()

    #Got to Website
    page.goto("https://finder.eircode.ie/")
    
    # Pause for a second
    page.wait_for_timeout(1000)

    # Close Cookie Approval
    page.locator("xpath=/html/body/div[2]/div[8]").click()    
    
    # Find Search Query Form and entery in search query
    page.locator(".form-control").fill(address)
    
    #Fie 
    page.click("input[value=Search]")
    
    # Pause for Second
    page.wait_for_timeout(1000)
    
    # Get Output Required
    output = page.wait_for_selector(".E-code-text").inner_text()
    
    # Print Output
    print(output) 

    # Close Browser   
    browser.close()    
