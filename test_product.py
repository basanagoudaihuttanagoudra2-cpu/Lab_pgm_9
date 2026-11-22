from product import product_details
def test_product_details():
    result = product_details("P101", "Laptop", "10", "50000")
    expected = "Product ID: P101\nProduct Name: Laptop\nQuantity: 10\nPrice: 50000"
    assert result == expected
