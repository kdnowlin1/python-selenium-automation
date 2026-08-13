from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open main target page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')

@when('Click Sign In')
def click_sign_in(context):
    sign_in = context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')
    sign_in.click()
    sleep(2)

@when('Click Sign In from navigation menu')
def click_sign_in_nav(context):
    sleep(2)

@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    sign_in_form = context.driver.find_element(By.CSS_SELECTOR, '#login')
    assert sign_in_form.is_displayed(), "Sign In form is not displayed"