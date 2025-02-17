import csv

def update_csv_data(csv_file_path, row, payment_info, shipping_info):
    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        
    data[row]["Payment Information"] = payment_info
    data[row]["Shipping Information"] = shipping_info
    
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)