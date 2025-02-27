from m5labfunctions import read_csv, calc_product_totals, calc_cust_totals, write_prod_csv, write_prod_txt, write_cust_txt, write_cust_csv

def main():
    # read_csv()
    products = calc_product_totals()
    write_prod_csv(products)
    write_prod_txt(products)
    customers = calc_cust_totals()
    write_cust_csv(customers)
    write_cust_txt(customers)
    


if __name__ == "__main__":
    main()