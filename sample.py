import time
from selenium import webdriver
import info

#For using MsEdge
# Make sure to add msedgedriver to your path
browser = webdriver.Edge(executable_path='msedgedriver.exe')

#Bestbuy RTX 3080 page
browser.get("https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432400.p?skuId=6432400")

# Sample in-stock
#browser.get("https://www.bestbuy.com/site/microsoft-surface-book-3-13-5-touch-screen-pixelsense-2-in-1-laptop-intel-core-i7-16gb-memory-256gb-ssd-platinum/6408384.p?skuId=6408384")
#browser.get("https://www.bestbuy.com/site/xtreme-personal-care-2ozhand-sanitizer-gel/6415196.p?skuId=6415196")

buyButton = False

while not buyButton:

    try:
        # If this works then the button is not pytopen
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")

        # Button isn't open restart the script
        print("Button isn't ready yet.")

        # Refresh page after a delay
        time.sleep(1)
        browser.refresh()

    except:
        
        addToCartBtn = browser.find_element_by_class_name("btn-primary")

        # Click the button and end the script
        print("Button was clicked.")
        addToCartBtn.click()

        # Go to cart page
        browser.get("https://www.bestbuy.com/cart")

        # Click on Checkout Button
        browser.implicitly_wait(2)
        checkoutBtn = browser.find_element_by_class_name("btn-lg")
        checkoutBtn.click()

        # Enter log-in info
        username = browser.find_element_by_id("fld-e")
        username.send_keys(info.email)
        password = browser.find_element_by_id("fld-p1")
        password.send_keys(info.password)

        # Click Sign-in Button
        signInBtn = browser.find_element_by_class_name("btn-secondary")
        signInBtn.click()

        # Enter CVV for Card
        browser.implicitly_wait(2)
        cvv = browser.find_element_by_id("credit-card-cvv")
        cvv.send_keys(info.cvv)

        # Place the order
        placeOrderBtn = browser.find_element_by_class_name("btn-lg")
        placeOrderBtn.click()
        buyButton = True