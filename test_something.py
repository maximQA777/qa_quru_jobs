
from selene import browser, have , be

def test_browser(open_browser):
     browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
     browser.element('[data-testid="result"]#r1-0').should(have.text('Selene: User-Oriented Web UI Browser Tests in Python - GitHub'))


def test_error_browser(open_browser):
     browser.element('[name="q"]').should(be.blank).type('kakasha228abvsdasdasdas').press_enter()
     browser.element('#react-layout').should(have.text('результаты не найдены'))





