from Zoomba.MobileLibrary import MobileLibrary
import unittest
from appium import webdriver
from unittest.mock import MagicMock
from appium.webdriver.common.touch_action import TouchAction
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'Helpers'))
from webdriverremotemock import WebdriverRemoteMock


class TestInternal(unittest.TestCase):

    def test_import_defaults(self):
        MobileLibrary()

    def test_import_overrides(self):
        MobileLibrary(timeout=10, run_on_failure='Capture Page Screenshot')

    def test_wait_for_and_input_text_simple(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_for_and_clear_text(mock_desk, "some_locator")
        mock_desk.clear_text.assert_called_with("some_locator")

    def test_wait_for_and_click_element(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_for_and_click_element(mock_desk, "some_locator")
        mock_desk.click_element.assert_called_with("some_locator")

    def test_wait_for_and_click_text(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_for_and_click_text(mock_desk, "some_text")
        mock_desk.click_text.assert_called_with("some_text", False)

    def test_wait_for_and_click_text_exact(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_for_and_click_text(mock_desk, "some_text", True)
        mock_desk.click_text.assert_called_with("some_text", True)

    def test_wait_for_and_click_button(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_for_and_click_button(mock_desk, "some_button")
        mock_desk.click_button.assert_called_with("some_button")

    def test_wait_for_and_input_password(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_for_and_input_password(mock_desk, "some_locator", "some_text")
        mock_desk.input_password.assert_called_with("some_locator", "some_text")

    def test_wait_for_and_input_text(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_for_and_input_text(mock_desk, "some_locator", "some_text")
        mock_desk.input_text.assert_called_with("some_locator", "some_text")

    def test_wait_for_and_input_value(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_for_and_input_value(mock_desk, "some_locator", "some_value")
        mock_desk.input_value.assert_called_with("some_locator", "some_value")

    def test_wait_for_and_long_press(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_for_and_long_press(mock_desk, "some_locator", 1000)
        mock_desk.long_press.assert_called_with("some_locator", 1000)

    def test_wait_until_element_contains(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_until_element_contains(mock_desk, "some_locator", 'test_text')
        mock_desk.element_should_contain_text.assert_called_with("some_locator", 'test_text', None)

    def test_wait_until_element_does_not_contain(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_until_element_does_not_contain(mock_desk, "some_locator", 'test_text')
        mock_desk.element_should_not_contain_text.assert_called_with("some_locator", 'test_text', None)

    def test_wait_until_element_is_enabled(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_until_element_is_enabled(mock_desk, "some_locator")
        mock_desk.element_should_be_enabled.assert_called_with("some_locator")

    def test_wait_until_element_is_disabled(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_until_element_is_disabled(mock_desk, "some_locator")
        mock_desk.element_should_be_disabled.assert_called_with("some_locator")

    def test_drag_and_drop(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        TouchAction.move_to = MagicMock()
        TouchAction.release = MagicMock()
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.drag_and_drop(mock_desk, "some_locator", "some_other_locator")
        mock_desk._platform_dependant_press.assert_called()
        TouchAction.move_to.assert_called_with(unittest.mock.ANY)
        TouchAction.release.assert_called()

    def test_drag_and_drop_ios(self):
        mock_desk = MagicMock()
        mock_desk._get_platform = MagicMock(return_value='ios')
        webdriver.Remote = WebdriverRemoteMock
        TouchAction.move_to = MagicMock()
        TouchAction.release = MagicMock()
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.drag_and_drop(mock_desk, "some_locator", "some_other_locator")
        mock_desk._platform_dependant_press.assert_called()
        TouchAction.move_to.assert_called_with(unittest.mock.ANY)
        TouchAction.release.assert_called()

    def test_drag_and_drop_missing_source(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._element_find.side_effect = ValueError
        MobileLibrary.open_application(mock_desk, 'remote_url')
        self.assertRaises(ValueError, MobileLibrary.drag_and_drop, mock_desk, "some_locator", "some_other_locator")

    def test_drag_and_drop_missing_target(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._element_find.side_effect = [True, ValueError]
        MobileLibrary.open_application(mock_desk, 'remote_url')
        self.assertRaises(ValueError, MobileLibrary.drag_and_drop, mock_desk, "some_locator", "some_other_locator")

    def test_drag_and_drop_with_offset(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        TouchAction.move_to = MagicMock()
        TouchAction.release = MagicMock()
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.drag_and_drop_by_offset(mock_desk, "some_locator", x_offset=100, y_offset=100)
        mock_desk._platform_dependant_press.assert_called()
        TouchAction.move_to.assert_called_with(x=unittest.mock.ANY, y=unittest.mock.ANY)
        TouchAction.release.assert_called()

    def test_drag_and_drop_with_offset_ios(self):
        mock_desk = MagicMock()
        mock_desk._get_platform = MagicMock(return_value='ios')
        webdriver.Remote = WebdriverRemoteMock
        TouchAction.move_to = MagicMock()
        TouchAction.release = MagicMock()
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.drag_and_drop_by_offset(mock_desk, "some_locator", x_offset=100, y_offset=100)
        mock_desk._platform_dependant_press.assert_called()
        TouchAction.move_to.assert_called_with(x=unittest.mock.ANY, y=unittest.mock.ANY)
        TouchAction.release.assert_called()

    def test_drag_and_drop_with_offset_missing_locator(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._element_find.side_effect = ValueError
        MobileLibrary.open_application(mock_desk, 'remote_url')
        self.assertRaises(ValueError, MobileLibrary.drag_and_drop_by_offset, mock_desk, "some_locator",
                          x_offset=100, y_offset=100)

    def test_scroll_up(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk.get_current_context = MagicMock(return_value="Web")
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.scroll_up(mock_desk, "some_locator")
        mock_desk._element_find()._execute.assert_called()

    def test_scroll_up_native_app(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._current_application().execute_script = MagicMock()
        mock_desk.get_current_context = MagicMock(return_value="NATIVE")
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.scroll_up(mock_desk, "some_locator")
        mock_desk._current_application().execute_script.assert_called()

    def test_scroll_up_to_text(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk.get_current_context = MagicMock(return_value="Web")
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.scroll_up_to_text(mock_desk, "some_locator")
        mock_desk._element_find_by_text()._execute.assert_called()

    def test_scroll_up_to_text_native_app(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._current_application().execute_script = MagicMock()
        mock_desk.get_current_context = MagicMock(return_value="NATIVE")
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.scroll_up_to_text(mock_desk, "some_locator")
        mock_desk._current_application().execute_script.assert_called()

    def test_scroll_up_to_text_last_option(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._current_application().execute_script = MagicMock(side_effect=ValueError)
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.scroll_up_to_text(mock_desk, "some_locator")
        mock_desk._scroll_to_text.assert_called()

    def test_scroll_down(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk.get_current_context = MagicMock(return_value="Web")
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.scroll_down(mock_desk, "some_locator")
        mock_desk._element_find()._execute.assert_called()

    def test_scroll_down_native_app(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._current_application().execute_script = MagicMock()
        mock_desk.get_current_context = MagicMock(return_value="NATIVE")
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.scroll_down(mock_desk, "some_locator")
        mock_desk._current_application().execute_script.assert_called()

    def test_scroll_down_to_text(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk.get_current_context = MagicMock(return_value="Web")
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.scroll_down_to_text(mock_desk, "some_locator")
        mock_desk._element_find_by_text()._execute.assert_called()

    def test_scroll_down_to_text_native_app(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._current_application().execute_script = MagicMock()
        mock_desk.get_current_context = MagicMock(return_value="NATIVE")
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.scroll_down_to_text(mock_desk, "some_locator")
        mock_desk._current_application().execute_script.assert_called()

    def test_scroll_down_to_text_last_option(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._current_application().execute_script = MagicMock(side_effect=ValueError)
        mock_desk._is_text_present.side_effect = [False, True]
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.scroll_down_to_text(mock_desk, "some_locator")
        mock_desk._scroll_to_text.assert_called()

    def test_wait_for_and_tap(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_for_and_tap(mock_desk, "some_locator")
        mock_desk.tap.assert_called_with("some_locator", None, None, 1)

    def test_wait_for_and_tap_multiple(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_for_and_tap(mock_desk, "some_locator", count=4)
        mock_desk.tap.assert_called_with("some_locator", None, None, 4)

    def test_wait_for_and_tap_override_defaults(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        MobileLibrary.open_application(mock_desk, 'remote_url')
        MobileLibrary.wait_for_and_tap(mock_desk, "some_locator", x_offset=200, y_offset=100, count=4,
                                       error='some_error', timeout='10s')
        mock_desk.tap.assert_called_with("some_locator", 200, 100, 4)

    def test_capture_page_screenshot(self):
        mock_desk = MagicMock()
        mock_desk._get_screenshot_paths = MagicMock(return_value=['path', 'link'])
        MobileLibrary.capture_page_screenshot(mock_desk)
        mock_desk._get_screenshot_paths.assert_called()

    def test_capture_page_screenshot_else_case(self):
        mock_desk = MagicMock()
        mock_desk._get_screenshot_paths = MagicMock(return_value=['path', 'link'])
        del mock_desk._current_application().get_screenshot_as_file
        MobileLibrary.capture_page_screenshot(mock_desk, 'filename')
        mock_desk._get_screenshot_paths.assert_called()

    def test_save_appium_screenshot(self):
        mock_desk = MagicMock()
        MobileLibrary.save_appium_screenshot(mock_desk)
        mock_desk.capture_page_screenshot.assert_called()

    def test_wait_until_page_contains_private(self):
        mock_desk = MagicMock()
        MobileLibrary._wait_until_page_contains(mock_desk, 'some_text', 5)
        mock_desk._wait_until.asser_called_with('some_text', 5)

    def test_wait_until_page_contains_element_private(self):
        mock_desk = MagicMock()
        MobileLibrary._wait_until_page_contains_element(mock_desk, 'some_element', 5)
        mock_desk._wait_until.assert_called_with(5, "Element 'some_element' did not appear in "
                                                    "<TIMEOUT>", unittest.mock.ANY, 'some_element')

    def test_platform_dependant_press_private(self):
        mock_desk = MagicMock()
        mock_desk._is_ios = MagicMock(return_value=False)
        MobileLibrary._platform_dependant_press(mock_desk, MagicMock(), 'some_element')

    def test_platform_dependant_press_ios_private(self):
        mock_desk = MagicMock()
        mock_desk._is_ios = MagicMock(return_value=True)
        MobileLibrary._platform_dependant_press(mock_desk, MagicMock(), 'some_element')

    def test_platform_dependant_press_delay_set_private(self):
        mock_desk = MagicMock()
        mock_desk._is_ios = MagicMock(return_value=True)
        MobileLibrary._platform_dependant_press(mock_desk, MagicMock(), 'some_element', delay=500)

    def test_element_find_by_text_ios(self):
        mock_desk = MagicMock()
        mock_desk._is_ios = MagicMock(return_value=True)
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._element_find = MagicMock()
        MobileLibrary._element_find_by_text(mock_desk, "some_text")
        mock_desk._element_find.assert_called_with('some_text', True, False)

    def test_element_find_by_text_ios_exact(self):
        mock_desk = MagicMock()
        mock_desk._is_ios = MagicMock(return_value=True)
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._element_find = MagicMock(return_value=False)
        MobileLibrary._element_find_by_text(mock_desk, "some_text", True)
        mock_desk._element_find.assert_called_with('//*[@value="some_text" or @label="some_text"]', True, True)

    def test_element_find_by_text_ios_not_exact(self):
        mock_desk = MagicMock()
        mock_desk._is_ios = MagicMock(return_value=True)
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._element_find = MagicMock(return_value=False)
        MobileLibrary._element_find_by_text(mock_desk, "some_text", False)
        mock_desk._element_find.assert_called_with('//*[contains(@label,"some_text") or contains(@value, "some_text") '
                                                   'or contains(text(), "some_text")]', True, True)

    def test_element_find_by_text_android_exact(self):
        mock_desk = MagicMock()
        mock_desk._is_ios = MagicMock(return_value=False)
        mock_desk._is_android = MagicMock(return_value=True)
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._element_find = MagicMock(return_value=False)
        MobileLibrary._element_find_by_text(mock_desk, "some_text", True)
        mock_desk._element_find.assert_called_with('//*[@text="some_text"]', True, True)

    def test_element_find_by_text_android_not_exact(self):
        mock_desk = MagicMock()
        mock_desk._is_ios = MagicMock(return_value=False)
        mock_desk._is_android = MagicMock(return_value=True)
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._element_find = MagicMock(return_value=False)
        MobileLibrary._element_find_by_text(mock_desk, "some_text", False)
        mock_desk._element_find.assert_called_with('//*[contains(@text,"some_text")]', True, True)

    def test_is_text_visible(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._element_find_by_text().is_displayed = MagicMock(return_value=True)
        result = MobileLibrary._is_text_visible(mock_desk, "some_text")
        self.assertTrue(result)

    def test_is_text_visible_not_found(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._element_find_by_text = MagicMock(return_value=None)
        result = MobileLibrary._is_text_visible(mock_desk, "some_text")
        self.assertIsNone(result)

    def test_scroll_to_text_ios_visible_no_scroll(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._is_android = MagicMock(return_value=False)
        mock_desk._is_ios = MagicMock(return_value=True)
        mock_desk._is_text_visible = MagicMock(return_value=True)
        result = MobileLibrary._scroll_to_text(mock_desk, "some_text", "up")
        self.assertTrue(result)

    def test_scroll_to_text_android_visible_no_scroll(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._is_ios = MagicMock(return_value=False)
        mock_desk._is_android = MagicMock(return_value=True)
        mock_desk._is_text_present = MagicMock(return_value=True)
        result = MobileLibrary._scroll_to_text(mock_desk, "some_text", "up")
        self.assertTrue(result)

    def test_scroll_to_text_ios_scroll(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._is_android = MagicMock(return_value=False)
        mock_desk._is_ios = MagicMock(return_value=True)
        mock_desk._is_text_visible = MagicMock(side_effect=[False, True])
        result = MobileLibrary._scroll_to_text(mock_desk, "some_text", "up")
        self.assertTrue(result)

    def test_scroll_to_text_android_scroll(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._is_android = MagicMock(return_value=True)
        mock_desk._is_ios = MagicMock(return_value=False)
        mock_desk._is_text_present = MagicMock(side_effect=[False, True])
        result = MobileLibrary._scroll_to_text(mock_desk, "some_text", "down")
        self.assertTrue(result)

    def test_scroll_to_text_bad_direction(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._is_android = MagicMock(return_value=True)
        mock_desk._is_ios = MagicMock(return_value=False)
        mock_desk._is_text_present = MagicMock(return_value=False)
        self.assertRaises(AssertionError, MobileLibrary._scroll_to_text, mock_desk, "some_text", "sideways")

    def test_scroll_to_text_not_found(self):
        mock_desk = MagicMock()
        webdriver.Remote = WebdriverRemoteMock
        mock_desk._is_android = MagicMock(return_value=True)
        mock_desk._is_ios = MagicMock(return_value=False)
        mock_desk._is_text_present = MagicMock(return_value=False)
        self.assertRaises(AssertionError, MobileLibrary._scroll_to_text, mock_desk, "some_text", "up")
