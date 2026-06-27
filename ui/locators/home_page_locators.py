from selenium.webdriver.common.by import By


class HomePageLocators:

    PLATFORM_BUTTON = (By.XPATH, "//button[text() = 'Platform']")
    SOLUTIONS_BUTTON = (By.XPATH, "//button[text() = 'Solutions']")
    RESOURCES_BUTTON = (By.XPATH, "//button[text() = 'Resources']")
    OPEN_SOURCES_BUTTON = (By.XPATH, "//button[text() = 'Open Source']")
    ENTERPRICE_BUTTON = (By.XPATH, "//button[text() = 'Enterprise']")
    PRICING_BUTTON = (By.XPATH, "(//span[text() = 'Pricing'])[1]")


class SolutionsMenu:
    """Left section"""

    ENTERPRISES = (By.XPATH, "//span[text() = 'Enterprises']")
    SMALL_AND_MEDIUM_TEAMS = (By.XPATH, "//span[text() = 'Small and medium teams']")
    STARTUPS = (By.XPATH, "//span[text() = 'Startups']")
    NONPROFITS = (By.XPATH, "//span[text() = 'Nonprofits']")
    VIEW_ALL_SOLUTIONS = (
        By.XPATH,
        "//li[.//button[text()='Solutions']]//span[text()='View all solutions']",
    )

    """Midle section"""
    APP_MODERNIZATION = (By.XPATH, "//span[text() = 'Enterprise']")
    DEVSECOPS = (By.XPATH, "//span[text() = 'DevSecOps']")
    DEVOPS = (By.XPATH, "(//span[text() = 'DevOps'])[1]")
    CI_CD = (By.XPATH, "//span[text() = 'CI/CD']")
    VIEW_ALL_USE_CASES = (
        By.XPATH,
        "//li[.//button[text()='Solutions']]//span[text()='View all use cases']",
    )

    """Right section"""
    HEALTHCARE = (By.XPATH, "//span[text() = 'Healthcare']")
    FINANCIAL_SERVICES = (
        By.XPATH,
        "//li[.//button[text()='Solutions']]//span[text()='Financial services']",
    )
    MANUFACTURING = (By.XPATH, "//span[text() = 'Manufacturing']")
    GOVERNMENT = (By.XPATH, "//span[text() = 'Government']")
    VIEW_ALL_INDUSTRIES = (
        By.XPATH,
        "//li[.//button[text()='Solutions']]//span[text()='View all industries']",
    )
