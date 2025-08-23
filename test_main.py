"""from navigation import Navigation
from signup import Signup
from login import Login
from cart import Cart
import time

from view_cart import ViewCart
from checkout import Checkout

# Visit Website
nav = Navigation()
nav.open_site("https://demoblaze.com/index.html")

# Perform Signup step
signup = Signup(nav.driver)
nav.click_signup()
time.sleep(1)
signup.type_username("Sharjeel")
signup.type_password("Test@123")
signup.click_signup_button()
nav.refresh_page()

# Perform Login Step
login = Login(nav.driver)
nav.click_login()
time.sleep(1)
login.type_username("Sharjeel")
login.type_password("Test@123")
login.click_login_button()

# Add product to cart step
cart = Cart(nav.driver)
cart.add_product("Samsung galaxy s6")

# View Cart step
view_cart = ViewCart(nav.driver)
view_cart.open_cart()

#checkout/ place order step
checkout = Checkout(nav.driver)
checkout.place_order(
    name="Sharjeel Malik",
    country="Pakistan",
    city="Lahore",
    credit_card="4242424242424242",
    month="08",
    year="2026"
)

nav.assert_title("STORE")
nav.quit()"""

from navigation import Navigation
from signup import Signup
from login import Login
from cart import Cart
from view_cart import ViewCart
from checkout import Checkout
import time

def test_full_checkout_flow():
    nav = Navigation()
    nav.open_site("https://demoblaze.com/index.html")

    signup = Signup(nav.driver)
    nav.click_signup()
    time.sleep(1)
    signup.type_username("Sharjeel")
    signup.type_password("Test@123")
    signup.click_signup_button()
    nav.refresh_page()

    login = Login(nav.driver)
    nav.click_login()
    time.sleep(1)
    login.type_username("Sharjeel")
    login.type_password("Test@123")
    login.click_login_button()

    cart = Cart(nav.driver)
    cart.add_product("Samsung galaxy s6")

    view_cart = ViewCart(nav.driver)
    view_cart.open_cart()

    checkout = Checkout(nav.driver)
    checkout.place_order(
        name="Sharjeel",
        country="Pakistan",
        city="Lahore",
        credit_card="123456789",
        month="08",
        year="2025"
    )

    nav.assert_title("STORE")
    nav.quit()





