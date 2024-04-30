# 封装的selenium的一些基础浏览器操作方法
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, param):
        """
        打开URL
        :param param:
        :return:
        """
        self.driver.get(param)

    def find_element(self, locator, timeout=10):
        """
        查找元素
        return element
        :param locator:
        :param timeout:
        :return:
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element

    def find_elements(self, locator, timeout=10):
        """
        查找多个元素
        :param locator:
        :param timeout:
        :return:
        """
        elements = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return elements

    def click_element(self, locator):
        """
        点击元素
        :param locator:
        :param timeout:
        :return:
        """
        element = self.find_element(locator)
        element.click()

    def input_text(self, locator, text, timeout=10):
        """
        输入文本
        :param locator:
        :param text:
        :param timeout:
        :return:
        """
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        """
        获取元素的文本
        :param locator:
        :param timeout:
        :return:
        """
        element = self.find_element(locator, timeout)
        return element.text

    def is_element_displayed(self, locator, timeout=10):
        """
        判断元素是否可见
        :param locator:
        :param timeout:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def is_element_enabled(self, locator, timeout=10):
        """
        判断元素是否可用
        :param locator:
        :param timeout:
        :return:
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        return element.is_enabled()

    def is_element_selected(self, locator, timeout=10):
        """
        判断元素是否被选中
        :param locator:
        :param timeout:
        :return:
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_selected(locator)
        )
        return element.is_selected()

    def is_alert_present(self, timeout=10):
        """
        判断是否出现alert弹窗
        :param timeout:
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            return True
        except:
            return False

    def close_alert(self, timeout=10):
        """
        关闭alert弹窗
        :param timeout:
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present()).accept()
            return True

        except:
            return False

    def get_alert_text(self, timeout=10):
        """
        获取alert弹窗的文本
        :param timeout:
        :return:
        """
        try:
            alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            return alert.text
        except:
            return None

    def switch_to_frame(self, locator, timeout=10):
        """
        切换到frame
        :param locator:
        :param timeout:
        :return:
        """
        frame = self.find_element(locator, timeout)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        """
        切换到默认的frame
        :return:
        """
        self.driver.switch_to.default_content()

    def switch_to_window(self, window_name):
        """
        切换到指定的窗口
        :param window_name:
        :return:
        """
        self.driver.switch_to.window(window_name)

    def switch_to_new_window(self):
        """
        切换到新的窗口
        :return:
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_window_handles(self):
        """
        获取所有窗口的句柄
        :return:
        """
        return self.driver.window_handles

    def get_current_window_handle(self):
        """
        获取当前窗口的句柄
        :return:
        """
        return self.driver.current_window_handle

    def get_screenshot(self, filename):
        """
        获取当前页面的截图
        :param filename:
        :return:
        """
        self.driver.save_screenshot(filename)

    def get_title(self):
        """
        获取当前页面的标题
        :return:
        """
        return self.driver.title

    def get_url(self):
        """
        获取当前页面的URL
        :return:
        """
        return self.driver.current_url

    def refresh(self):
        """
        刷新当前页面
        :return:
        """
        self.driver.refresh()

    def back(self):
        """
        后退
        :return:
        """
        self.driver.back()

    def forward(self):
        """
        前进
        :return:
        """
        self.driver.forward()

    def close(self):
        """
        关闭当前窗口
        :return:
        """
        self.driver.close()

    def quit(self):
        """
        关闭所有窗口并退出浏览器
        :return:
        """
        self.driver.quit()

    def execute_script(self, script):
        """
        执行JavaScript脚本
        :param script:
        :return:
        """
        self.driver.execute_script(script)

    def get_element_attribute(self, locator, attribute_name, timeout=10):
        """
        获取元素的属性值
        :param locator:
        :param attribute_name:
        :param timeout:
        :return:
        """
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute_name)

    def get_element_size(self, locator, timeout=10):
        """
        获取元素的尺寸
        :param locator:
        :param timeout:
        :return:
        """
        element = self.find_element(locator, timeout)
        return element.size

    def get_element_location(self, locator, timeout=10):
        """
        获取元素的坐标
        :param locator:
        :param timeout:
        :return:
        """
        element = self.find_element(locator, timeout)
        return element.location

    def get_element_css_value(self, locator, css_property, timeout=10):
        """
        获取元素的CSS属性值
        :param locator:
        :param css_property:
        :param timeout:
        :return:
        """
        element = self.find_element(locator, timeout)
        return element.value_of_css_property(css_property)

    def assert_text(self, param, param1):
        """
        断言文本
        :param param:
        :param param1:
        :return:
        """
        if param == param1:
            print(f"断言成功,{param} == {param1}")
        else:
            print(f"断言失败,{param} != {param1}")
