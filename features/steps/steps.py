from behave import given, when, then


@given(u'I navigate to login page')
def step_impl(context):
    """
        Navigate to login page and as the web server will run in local when we run
        end to end tests using behave, the url will be http://127.0.0.1:5000/login
    """
    context.browser.get('http://127.0.0.1:5000/login')


@given(u'I enter valid username and password')
def step_impl(context):
    """
        Find the html element using the name attribute and input the required data
        Here entering validusername and validpassword as the step definition says:
        I enter valid username and password
    """
    check= context.browser.find_element_by_id('email').send_keys('admin@blog.com')
    print(check)
    context.browser.find_element_by_id('password').send_keys('password')


@when(u'I click on Submit button')
def step_impl(context):
    """
        Find the input button on the html page which has value = Submit
        and invoke .click()
    """
    context.browser.find_element_by_xpath(f"//input[@type='submit' and @value='Login']").click()


@then(u'login is successful')
def step_impl(context):
    """
        If the login is successful we will be redirected to http://127.0.0.1:5000/index
        and also see the message "Login successful !!" on that page
    """
    assert context.browser.current_url == 'http://127.0.0.1:5000/home'
    assert 'You have been logged in!' in context.browser.page_source


@given(u'I enter invalid username or password')
def step_impl(context):
    """
        Find the html element using the name attribute and input the required data
        Here entering invalidusername and invalidpassword as the step definition says:
        I enter invalid username or password
    """
    context.browser.find_element_by_name('email').send_keys('invalidusername@blog.com')
    context.browser.find_element_by_name('password').send_keys('invalidpassword')


@then(u'login fails')
def step_impl(context):
    """
        If the login is successful we will not be redirected to http://127.0.0.1:5000/index
        but will be on the same page: http://127.0.0.1:5000/login
        and also see the message "Invalid username or password !!" on that page
    """
    assert context.browser.current_url == 'http://127.0.0.1:5000/login'
    assert 'Login Unsuccessful. Please check username and password' in context.browser.page_source
