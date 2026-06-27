from selenium.webdriver.common.by import By

class EnterpriseLocators:

    FIRST_NAME = (By.ID, "form-field-first_name")
    LAST_NAME = (By.ID, "form-field-last_name")
    COMPANY = (By.ID, "form-field-company")
    JOB_TITE = (By.ID, "form-field-job_title")
    WORK_EMAIL = (By.ID, "form-field-work_email")
    NUMBER_OF_DEVELOPERS = (By.ID, "form-field-number_of_developers")
    MESSAGE_FIELD = (By.ID, "form-field-message")
    COUNTRY_LIST = (By.ID, "form-field-country")