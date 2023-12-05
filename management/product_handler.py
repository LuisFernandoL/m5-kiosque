from menu import products


def get_product_by_id(id: int):
    if type(id) != int:
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(product_type: str):
    if type(product_type) != str:
        raise TypeError("product type must be a str")
    new_list = []
    for product in products:
        if product["type"] == product_type:
            new_list.append(product)
    return new_list


def id_order(dict: dict):
    return dict["_id"]


def add_product(menu, **kwargs: dict) -> None:
    if len(menu) == 0:
        kwargs["_id"] = 1
        menu.append(kwargs)
        return kwargs
    if len(menu) >= 1:
        menu.sort(key=id_order)
        last_element = menu[-1]
        new_id = last_element["_id"]+1
        kwargs["_id"] = new_id
        menu.append(kwargs)
        return kwargs


def menu_report():
    total = 0
    item_type = {}
    max_type = []
    product_count = len(products)

    for item in products:
        total += item["price"]
        max_type.append(item["type"])
    average_price = total/product_count

    for element in products:
        prodct_type = element["type"]
        if prodct_type in item_type:
            item_type[prodct_type] += 1
        else:
            item_type[prodct_type] = 1
    common_type = max(set(max_type), key=max_type.count)
    return (f"Products Count: "f'{product_count}'" - Average Price: "f'${round(average_price,2)}'" - Most Common Type: "f'{common_type}'"")
