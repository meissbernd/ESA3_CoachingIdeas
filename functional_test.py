from selenium import webdriver


def test_functional_basic():
    """Test if main page of app starts."""
    browser = webdriver.Firefox()
    browser.get("http://localhost:8000")

    assert "Trainingsübungen" in browser.title
    print("OK")
    browser.quit()


if __name__ == "__main__":
    test_functional_basic()
