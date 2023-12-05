from menu import products


def found_item(id: int):
    for item in products:
        if item["_id"] == id:
            return item

    return {}


def calculate_tab(list):
    total = 0
    for item in list:
        product = found_item(item["_id"])
        total += item["amount"]*product["price"]
    return {'subtotal': f'${round(total,2)}'}
