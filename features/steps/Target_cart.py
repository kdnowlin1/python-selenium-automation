from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page for cart')
def open_target_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def click_cart_icon(context):
    cart = context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
    cart.click()
    sleep(2)

@then('Verify "Your cart is empty" message is shown')
def verify_empty_cart(context):
    empty_cart = context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    assert empty_cart.is_displayed(), "Cart empty message is not shown"