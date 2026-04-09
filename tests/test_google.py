from pages.google_page import GooglePage

def test_google_search(page):
    google = GooglePage(page)

    google.go_to_google()
    google.search("Playwright Python")
    google.wait_for_results()

    assert google.get_results_count() > 0