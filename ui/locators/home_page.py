from selenium.webdriver.common.by import By

class MainPageLocators():

    PLATFORM_BUTTON  = (By.XPATH, "//button[text() = 'Platform']")
    SOLUTIONS_BUTTON = (By.XPATH, "//button[text() = 'Solutions']")
    RESOURCES_BUTTON = (By.XPATH, "//button[text() = 'Resources']")
    OPEN_SOURCES_BUTTON = (By.XPATH, "//button[text() = 'Open Source']")
    ENTERPRICE_BUTTON = (By.XPATH, "//button[text() = 'Enterprise']")
    PRICING_BUTTON = (By.XPATH, "(//span[text() = 'Pricing'])[1]")