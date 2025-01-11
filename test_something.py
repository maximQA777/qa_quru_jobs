
from selene import browser, have , be

def test_negative(open_browser):
        browser.element('[name="q"]').should(be.blank).type('fdfsdfdsfadwdweafasf').press_enter()
        browser.element('[class="card-section"]').should(have.text('По запросу fdfsdfdsfadwdweafasf ничего не найдено. '))

def test_browser(open_browser):
        browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
        browser.element('[class="IsZvec"]').should(have.text('s core strength is its user-oriented API, which abstracts the complexity of working with Selenium WebDriver'))
        browser.element('[class="LC20lb MBeuO DKV0Md"]').click()






