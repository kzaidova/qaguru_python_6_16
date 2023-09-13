import datetime
from demoqa_form.models.pages.registration_page import RegistrationPage
from demoqa_form.data.users import User
import allure


def test_fill_and_submit_form(configure_browser):
    registration_page = RegistrationPage()

    katrin = User(
        first_name='Катрин',
        last_name='Заидова',
        email='newemail@mail.ru',
        gender='Female',
        mobile='9998076767',
        date_of_birth=datetime.date(1995, 8, 24),
        subjects='English',
        hobbies='Reading',
        picture='bear.jpg',
        current_address='Koh Samui, Thailand',
        state="Haryana",
        city="Karnal"
    )
    with allure.step("Open registration page"):
        registration_page.open()
    with allure.step("Fill registration form"):
        registration_page.register(katrin)
    with allure.step("Assert registered and registration info correct"):
        registration_page.should_registered_user(katrin)

