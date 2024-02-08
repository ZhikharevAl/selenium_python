
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str) -> None:
        """
        Opens the specified URL in the web browser.
        Args:
        url (str): The URL to be opened.
        Returns:
        None
        """
        self.driver.get(url)
