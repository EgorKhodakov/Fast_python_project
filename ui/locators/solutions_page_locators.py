from selenium.webdriver.common.by import By

class SolutionsLocators:

    SOLUTIONS = (By.XPATH, "//a[text()='Solutions']")
    BY_USE_CASE = (By.XPATH, "//a[text()='By use case']")

    UP_START_FREE_TRIAL = (By.XPATH, "(//span[text()='Start a free trial'])[1]")
    UP_CONTACT_SALES = (By.XPATH, "(//span[text()='Contact sales'])[1]")

    EXPLORE_GITHUB_ADVANCED_SECURITY = (By.XPATH, "//a[text()='Explore GitHub Advanced Security")

    DOWN_START_FREE_TRIAL = (By.XPATH, "(//span[text()='Start a free trial'])[2]")
    DOWN_CONTACT_SALES = (By.XPATH, "(//span[text()='Contact sales'])[2]")

    """Additional Resources"""
    DEVOPS_TIPS = (By.XPATH, "//a[text()='DevOps tips for Engineering leaders']")
    SHIP_SECURE = (By.XPATH, "//a[text()='Ship secure software fast']")
    CD_CD_SOLUTION_DEMO = (By.XPATH, "//a[text()='CI/CD Solution Demo ']")
