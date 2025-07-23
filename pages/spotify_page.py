from appium.webdriver.common.appiumby import AppiumBy
from utils.helpers import click_element, send_keys

class SpotifyPage:
    def __init__(self, driver):
        self.driver = driver

    def open_app(self):
        click_element(self.driver, AppiumBy.ACCESSIBILITY_ID, "Spotify")

    def search_song(self, query):
        click_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(25)')
        click_element(self.driver, AppiumBy.ACCESSIBILITY_ID, "Search for something to listen to")
        send_keys(self.driver, AppiumBy.ID, "com.spotify.music:id/query", query)
        click_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.spotify.music:id/title").instance(0)')

    def control_playback(self):
        click_element(self.driver, AppiumBy.ACCESSIBILITY_ID, "Pause")
        click_element(self.driver, AppiumBy.ACCESSIBILITY_ID, "Play")

    def add_to_playlist(self, playlist_name):
        click_element(self.driver, AppiumBy.ACCESSIBILITY_ID, "More options for song All The Stars (with SZA) - From \"Black Panther: The Album\"")
        click_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add to other playlist")')
        click_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(0)')
        send_keys(self.driver, AppiumBy.ACCESSIBILITY_ID, "Add a playlist name", playlist_name)
        click_element(self.driver, AppiumBy.ID, "com.spotify.music:id/continue_button")

    def finalize(self):
        click_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(30)')
        click_element(self.driver, AppiumBy.ACCESSIBILITY_ID, "Now Playing Bar")
