def test_calculate_delivery_days():
    """Проверка логики расчета срока доставки"""
    # Если склад в Москве, а точка в СПБ, должно быть 1 день
    route = {"from": "Moscow", "to": "SPB"}
    
    response = requests.get("https://api.example.com/delivery-calc", params=route)
    data = response.json()
    
    assert data["days"] <= 1
    assert data["route_status"] == "active"
