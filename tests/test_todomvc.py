from selene import browser, by, query, command
from selene.support.shared import config
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By

from selene_in_action_py13.conditions import match


def test_complete_todo():
    browser.open('/')

    browser.element('.new-todo').wait_until(match.visible)

    browser.element('.new-todo').should(match.blank)

    browser.element('.new-todo').type('a').press_enter()
    # browser.element('.new-todo').perform(command.select_all) вызов дополнительных команд +js
    # browser.element('.save').perform(command.js.click)
    # save = browser.element('.save').with_(click_by_js=True).click()
    # save.click()
    # save.click()
    # save.click()
    browser.element('.new-todo').type('b').press_enter()
    browser.element('.new-todo').type('c').press_enter()

    browser.all('.todo-list>li').with_(timeout=5.0).should(match.size(3))
    # browser.all('.todo-list>li').first.should(match.exact_text('a'))
    # browser.all('.todo-list>li').second.should(match.exact_text('b'))
    # browser.all('.todo-list>li')[2].should(match.exact_text('c'))
    browser.all('.todo-list>li')[-1].should(match.exact_text('c'))
    browser.all('.todo-list>li').should(match.exact_texts('a', 'b', 'c'))
    # browser.all('.todo-list>li').second.element('.toggle').click()
    browser.all('.todo-list>li').element_by(match.exact_text('b')).element(
        '.toggle'
    ).click()
    #browser.element('//*[@id="todo-list"]/li[normalize-space(.)="b"]//*[contains(concat(" ", @class, " "), " toggle "]') XPath
    #browser.all('.todo-list>li').element_by(match.css_class('completed')).should(match.exact_text('b'))
    browser.all('.todo-list>li').by(match.css_class('completed')).should(match.exact_texts('b'))
    browser.all('.todo-list>li').by(match.no.css_class('completed')).should(match.exact_texts('a', 'c'))

    # browser.all('.todo-list>li').with_(timeout=5.0).wait.for_(match.size(3)) или

    # assert len(browser.driver.find_elements(*by.css('.todo-list>li'))) == 3 проверка на selenium
    # WebDriverWait(driver=browser.driver, timeout=3.0).until(lambda driver: len(driver.find_elements(*by.css('.todo-list>li'))) == 3

# def test_complete_todo_selenium(driver, browser):

# driver.get('https://todomvc.com/examples/emberjs/todomvc/dist')
# initial_value = browser.element('.new-todo').get(query.attribute('value')) == ''
# initial_value = browser.element('.new-todo').locate()
# assert driver.find_element(*by.css('.new-todo')).get_attribute('value') == ''

# browser.element('.new-todo').send_keys('a' + Keys.ENTER)
# driver.find_element(*by.css('.new-todo').send_keys('b' + Keys.ENTER))
# driver.find_element(*by.css('.new-todo').send_keys('c' + Keys.ENTER))
