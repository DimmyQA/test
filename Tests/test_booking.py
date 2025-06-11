from services.api_service import APIService
import allure

@allure.epic('First test')
class TestBooking:
    @allure.title('First test')
    def test_get_booking(self):
        with allure.step('Отправка тестового запроса'):
            booking = APIService().get_booking(10)

        with allure.step('Первый assert'):
            assert booking.status_code == 200

        with allure.step('Ответ от сервера'):
            allure.attach(body=booking.text, name='Server response', attachment_type=allure.attachment_type.TEXT)