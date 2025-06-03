from services.api_service import APIService

class TestBooking:
    def test_get_booking(self):
        booking = APIService().get_booking(10)
        assert booking.status_code == 200