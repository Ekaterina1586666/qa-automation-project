import pytest
import requests

# Пример теста API для проверки логистического сервиса
def test_shipment_status():
    # URL вашей системы (заглушка)
    url = "https://api.example.com/shipments/SHP-001"
    response = requests.get(url)
    
    # Проверяем, что запрос прошел успешно
    assert response.status_code == 200
    # Проверяем, что в ответе есть поле статуса
    assert "status" in response.json()
