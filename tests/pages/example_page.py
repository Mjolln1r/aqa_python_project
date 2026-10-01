from playwright.sync_api import Page


BASE_URL = "https://example.com"

class ExamplePage:
    def __init__(self, page: Page):
        self.page = page


    def open_url(self):
        return self.page.goto(BASE_URL)


    def get_title(self):
        return self.page.locator("h1")


    def get_more_info_link(self):
        return self.page.get_by_role("link", name="Learn more")
