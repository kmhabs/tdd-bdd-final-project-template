######################################################################
# Web Steps
######################################################################
import logging
from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ID_PREFIX = 'product_'

@when('I visit the "Home Page"')
def step_impl(context):
    context.driver.get(context.base_url)
    context.driver.save_screenshot('home_page.png')

@then('I should see "{message}" in the title')
def step_impl(context, message):
    assert message in context.driver.title

@then('I should not see "{text_string}"')
def step_impl(context, text_string):
    element = context.driver.find_element(By.TAG_NAME, 'body')
    assert text_string not in element.text

@when('I set the "{element_name}" to "{text_string}"')
def step_impl(context, element_name, text_string):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = context.driver.find_element(By.ID, element_id)
    element.clear()
    element.send_keys(text_string)

@when('I select "{text}" in the "{element_name}" dropdown')
def step_impl(context, text, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = Select(context.driver.find_element(By.ID, element_id))
    element.select_by_visible_text(text)

@then('I should see "{text}" in the "{element_name}" dropdown')
def step_impl(context, text, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = Select(context.driver.find_element(By.ID, element_id))
    assert element.first_selected_option.text == text

@then('the "{element_name}" field should be empty')
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = context.driver.find_element(By.ID, element_id)
    assert element.get_attribute('value') == u''

@when('I copy the "{element_name}" field')
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        EC.presence_of_element_located((By.ID, element_id))
    )
    context.clipboard = element.get_attribute('value')
    logging.info('Clipboard contains: %s', context.clipboard)

@when('I paste the "{element_name}" field')
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        EC.presence_of_element_located((By.ID, element_id))
    )
    element.clear()
    element.send_keys(context.clipboard)

@when('I press the "{button}" button')
def step_impl(context, button):
    button_id = button.lower() + '-btn'
    context.driver.find_element(By.ID, button_id).click()

@then('I should see "{name}" in the results')
def step_impl(context, name):
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        EC.text_to_be_present_in_element(
            (By.ID, 'search_results'),
            name
        )
    )
    assert found

@then('I should not see "{name}" in the results')
def step_impl(context, name):
    element = context.driver.find_element(By.ID, 'search_results')
    assert name not in element.text

@then('I should see the message "{message}"')
def step_impl(context, message):
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        EC.text_to_be_present_in_element(
            (By.ID, 'flash_message'),
            message
        )
    )
    assert found

@then('I should see "{text_string}" in the "{element_name}" field')
def step_impl(context, text_string, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        EC.text_to_be_present_in_element_value(
            (By.ID, element_id),
            text_string
        )
    )
    assert found

@when('I change "{element_name}" to "{text_string}"')
def step_impl(context, element_name, text_string):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        EC.presence_of_element_located((By.ID, element_id))
    )
    element.clear()
    element.send_keys(text_string)