import qrcode
PRODUCTS = []


def read_from_database():
    f = open("F:\PyLearn7 Projects\Little-Python-projects-PyLearn7-\Assignment7\database.txt", "r")

    for line in f:

        result = line.split(",")
        my_dict = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}

        PRODUCTS.append(my_dict)

    f.close()


def write_to_database():
    f = open("F:\PyLearn7 Projects\Little-Python-projects-PyLearn7-\Assignment7\database.txt", "w")
    str_products = ''
    for product in PRODUCTS:
        str_p = str(product["code"]) + ',' + str(product["name"]) + ',' + str(product["price"]) + ',' + \
                str(product["count"])
        str_products += str_p

    f.write(str_products)
    f.close()


def get_product_code():
    product_code = input("Enter the product code : ")
    return product_code


def qr_code():
    produce_code = get_product_code()
    for product in PRODUCTS:
        if product["code"] == produce_code:
            qr_str = product["code"] + "|" + product["name"] + "|" + product["price"] + "|" + product["count"]
            break

    img = qrcode.make(qr_str)
    img.save("F:\PyLearn7 Projects\Little-Python-projects-PyLearn7-\Assignment7\product_information.png")


def factor(user_basket):
    print("Name\tPrice of one item\tnumber of items")

    total = 0
    for product in user_basket:
        print(product["name"], "\t", product["price"], "\t\t\t\t", str(product["num_product_buy"] * int(product["price"])))
        total += product["num_product_buy"] * int(product["price"])

    print("Total price of basket : {} ".format(total))


def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4 -Search")
    print("5- Show List")
    print("6- Buy")
    print("7- QR_Code")
    print("8- Exit")


def add():
    code = input("Enter code:")
    name = input("Enter name:")
    price = input("Enter price:")
    count = input("Enter count:")
    new_product = {'code': code, 'name': name, 'price': price, 'count': count}
    PRODUCTS.append(new_product)


def edit():
    product_code = get_product_code()

    print("1- Name")
    print("2- Price")
    print("3- Count")
    field = input("Which product field do you want to edit? ")
    edited_field_value = input("Enter edited value: ")

    if field == "1":
        for product in PRODUCTS:
            if product["code"] == product_code:
                product["name"] = edited_field_value
                print("*** Information successfully updated ***")
                break

    elif field == "2":
        for product in PRODUCTS:
            if product["code"] == product_code:
                product["price"] = edited_field_value
                print("*** Information successfully updated ***")
                break

    elif field == "3":
        for product in PRODUCTS:
            if product["code"] == product_code:
                product["count"] = edited_field_value
                print("*** Information successfully updated ***")
                break

    else:
        print("...Enter a number between 1 and 3...")


def remove():
    product_code = get_product_code()

    for product in PRODUCTS:
        if product["code"] == product_code:
            PRODUCTS.remove(product)
            break

    print("+++ The product was successfully removed +++")


def search():
    user_input = input("Type your keyword: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"])
            break
    else:
        print("Not found")


def show_list():
    print("code\tname\tprice\tcount")
    for product in PRODUCTS:
        print(product["code"], product["name"], product["price"], product["count"])


def buy():

    user_basket = []
    key = 0
    while True:

        product_code = get_product_code()
        for product in PRODUCTS:
            if product["code"] == product_code:
                key = 1
                if product["count"] == '0':
                    print("*** we ran out of this product ***")

                elif product["count"] != '0':
                    num_product = int(input("Enter the number of product that you want to buy: "))
                    if int(product["count"]) - num_product <= 0:
                        print("SORRY !!! we just have " + product["count"] + " number of this product :/")

                    else:

                        new_product_count = int(product["count"]) - num_product
                        product["count"] = str(new_product_count)
                        product_copy = product
                        product_copy["num_product_buy"] = num_product
                        user_basket.append(product_copy)
                        print(user_basket)

        if key != 1:
            print("We do not have this product in our store")
        continue_signal = input("Do you want to continue buying? y/n")
        if continue_signal == "y":
            continue
        elif continue_signal == "n":
            factor(user_basket)
            break


print("*** Welcome to Famili store ***")
print("Loading...")
read_from_database()
print("Data Loaded.")

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        qr_code()
    elif choice == 8:
        write_to_database()
        exit(0)
    else:
        print("Enter a number between 1 and 8")
