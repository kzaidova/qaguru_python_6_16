from selene import be, have
from demoqa_form import resource
from selene import browser


class RegistrationPage:

    def register(self, user):
        self.type_first_name(user.first_name)
        self.type_last_name(user.last_name)
        self.type_user_email(user.email)
        self.gender_click(user.gender)
        self.type_user_number(user.mobile)
        self.type_date_of_birth_input(user.date_of_birth)
        self.subjects_input(user.subjects)
        self.hobbies_checkbox_click(user.hobbies)
        self.upload_picture(user.picture)
        self.type_current_address(user.current_address)
        self.state_click(user.state)
        self.city_click(user.city)
        self.submit_click()

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#adplus-anchor').remove()")
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    def type_first_name(self, first_name):
        browser.element('#firstName').should(be.blank).type(first_name)

    def type_last_name(self, last_name):
        browser.element('#lastName').should(be.blank).type(last_name)

    def type_user_email(self, email):
        browser.element('#userEmail').should(be.blank).type(email)

    def gender_click(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def type_user_number(self, number):
        browser.element('#userNumber').type(number)

    def type_date_of_birth_input(self, date):
        year = date.year
        month = date.month - 1
        day = date.strftime('%d')

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select option[value="' + str(month) + '"]').click()
        browser.element(f'.react-datepicker__day--0{day}').should(be.clickable).click()

    def subjects_input(self, subjects):
        browser.element('#subjectsInput').should(be.blank).type(subjects).press_enter()

    def hobbies_checkbox_click(self, hobbies):
        browser.all('.custom-checkbox').element_by(have.exact_text(hobbies)).click()

    def upload_picture(self, file_name):
        browser.element('#uploadPicture').send_keys(resource.path(file_name))

    def type_current_address(self, current_address):
        browser.element('#currentAddress').type(current_address)

    def state_click(self, state):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()

    def city_click(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()

    def submit_click(self):
        browser.element('#submit').click()

    def should_registered_user(self, user):
        full_name = f'{user.first_name} {user.last_name}'
        state_and_city = f'{user.state} {user.city}'
        browser.element('.modal-header').should(have.exact_text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(have.exact_texts(
            full_name,
            user.email,
            user.gender,
            user.mobile,
            user.date_of_birth.strftime("%d %B,%Y"),
            user.subjects,
            user.hobbies,
            user.picture,
            user.current_address,
            state_and_city
        ))