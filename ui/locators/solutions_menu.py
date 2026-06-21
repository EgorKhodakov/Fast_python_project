from selenium.webdriver.common.by import By

class SolutionsMenu:

    ENTERPRISES = (By.XPATH, "//span[text() = 'Enterprises']")
    SMALL_AND_MEDIUM_TEAMS = (By.XPATH, "//span[text() = 'Small and medium teams']")
    STARTUPS = (By.XPATH, "//span[text() = 'Startups']")
    NONPROFITS = (By.XPATH, "//span[text() = 'Nonprofits']")
    VIEW_ALL_SOLUTIONS = (By.XPATH, "//li[.//button[text()='Solutions']]//span[text()='View all solutions']")

    APP_MODERNIZATION = (By.XPATH, "//span[text() = 'Enterprise']")
    DEVSECOPS = (By.XPATH, "//span[text() = 'DevSecOps']")
    DEVOPS = (By.XPATH, "(//span[text() = 'DevOps'])[1]")
    CI_CD = (By.XPATH, "//span[text() = 'CI/CD']")
    VIEW_ALL_USE_CASES = (By.XPATH, "//li[.//button[text()='Solutions']]//span[text()='View all use cases']")

    HEALTHCARE = (By.XPATH, "//span[text() = 'Healthcare']")
    FINANCIAL_SERVICES= (By.XPATH, "//li[.//button[text()='Solutions']]//span[text()='Financial services']")
    MANUFACTURING = (By.XPATH, "//span[text() = 'Manufacturing']")
    GOVERNMENT = (By.XPATH, "//span[text() = 'Government']")
    VIEW_ALL_INDUSTRIES = (By.XPATH, "//li[.//button[text()='Solutions']]//span[text()='View all industries']")




