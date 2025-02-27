import csv
# read the file
def read_csv():
    # open the file and rename it to file
    with open("sales.csv", "r") as file:
        # create csv reader object
        reader = csv.reader(file)
        # loop thru file and print all rows
        for row in reader:
            print(row)
    return reader

def calc_product_totals():
    products = {}
    # open the file and rename it to file
    with open("sales.csv", "r") as file:
        # create csv reader object
        reader = csv.reader(file)
        next(reader) # skips the header
        for row in reader:
            # adds key:value pair if not already there
            if row[2] not in products:
                products[row[2]] = float(row[4]) * float(row[5])
            # updates value if key is already there
            else:
                products[row[2]] += float(row[4]) * float(row[5])
        # display info
        prod = "Product ID"
        cost = "Total Sales"
        print(f"{prod:<15}{cost}")
        print("- " * 14)
        for key, value in products.items():
            print(f"{key:<15}${value:.2f}")
        print("- " * 14)
        return products

def write_prod_csv(x):
    data_to_write = [{"ProdID": key, "Total Sales": f"${value:,.2f}"} for key, value in x.items()]
    with open("total_sales.csv", "w", newline="") as file: 
        column_names = ["ProdID", "Total Sales"]
        writer = csv.DictWriter(file, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(data_to_write)

def write_prod_txt(x):
    data_to_write = [f"ProdID: {key}, Total Sales: ${value:,.2f}" for key, value in x.items()]
    with open("total_sales.txt", "w") as file:
        for line in data_to_write:
            file.write(line + "\n")
        

        
def calc_cust_totals():
    customers = {}
    # open the file and rename it to file
    with open("sales.csv", "r") as file:
        # create csv reader object
        reader = csv.reader(file)
        next(reader) # skips the header
        for row in reader:
            if row[3] not in customers:
                customers[row[3]] = float(row[4]) * float(row[5])
            else:
                customers[row[3]] += float(row[4]) * float(row[5])
        prod = "Customer ID"
        cost = "Total Sales"
        print(f"{prod:<15}{cost}")
        print("- " * 14)
        for key, value in customers.items():
            print(f"{key:<15}${value:.2f}")
        print("- " * 14)
        return customers

def write_cust_csv(x):
    data_to_write = [{"CustID": key, "Total Sales": f"${value:,.2f}"} for key, value in x.items()]
    with open("cus_total.csv", "w", newline="") as file: 
        column_names = ["CustID", "Total Sales"]
        writer = csv.DictWriter(file, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(data_to_write)

def write_cust_txt(x):
    data_to_write = [f"CustID: {key}, Total Sales: ${value:,.2f}" for key, value in x.items()]
    with open("cus_total.txt", "w") as file:
        for line in data_to_write:
            file.write(line + "\n")
