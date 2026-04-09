class GooglePage:

    def __init__(self, page):
        self.page = page

        self.search_input = "input[name='q']"
        self.results = "[data-testid='result']"

    def go_to_google(self):
        self.page.goto("https://duckduckgo.com")

    def search(self, text):
        self.page.locator(self.search_input).fill(text)
        self.page.keyboard.press("Enter")

    def wait_for_results(self):
        self.page.wait_for_selector(self.results)

    def get_results_count(self):
        return self.page.locator(self.results).count()