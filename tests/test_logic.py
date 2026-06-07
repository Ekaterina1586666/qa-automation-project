def test_create_shipment_invalid_data():
    """Проверка, что система не создает поставку с некорректным весом"""
    invalid_data = {"shipment_id": "SHP-999", "weight": -5} # Вес не может быть отрицательным
    
    # Предполагаем, что API возвращает ошибку 400 (Bad Request)
    response = requests.post("https://api.example.com/shipments", json=invalid_data)
    
    assert response.status_code == 400
    assert "error" in response.json()
