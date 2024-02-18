product_data = []

# Open file
with open('product_data.txt') as file:
    for line in file:
        product_id, product_name, product_price, product_category = line.strip().split(',')
        product_data.append({
            'ID': int(product_id),
            'Name': product_name,
            'Price': float(product_price),
            'Category': product_category
        })

print(product_data)
print("Full Product Data\n")


# Insert: Add New Product 
# example
new_product = {'ID': 1001, 'Name': 'New Product', 'Price': 35.99, 'Category': 'Books'}
product_data.append(new_product)
print(product_data[-5:])
print("Product inserted:", new_product, "\n")


# Update: Modify existing product details
def update_product(products, product_id, updated_attributes):
    for product in products:
        if product['ID'] == product_id:
            for key, value in updated_attributes.items():
                product[key] = value
            break
    return product_id
# example
product_ID = update_product(product_data, 1001, {'Price': 59.99, 'Category': 'Electronics'})
print(product_data[-5:])
print("Product updated:", product_ID, "\n")


# Delete: Remove products while preserving data structure integrity.
def delete_product(products, product_id):
    for i, product in enumerate(products):
        if product['ID'] == product_id:
            x = products[i]
            del products[i]
            break
    return x
# example
product_ID = delete_product(product_data, 1001)
print(product_data[-5:])
print("Product deleted:", product_ID, "\n")


# Search for Product by ID
def search_product(products, product_id):
    for product in products:
        if product['ID'] == product_id:
            return product
    return None
# example
result = search_product(product_data, 69525)
if result:
    print("Product found:", result, "\n")
else:
    print("Product was not found.\n")


# Sorting Algorithm - Bubble Sort
def bubble_sort(arr, key='Price'):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (arr[j][key] > arr[j + 1][key]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

# Sort products by price in ascending order
bubble_sort(product_data, key='Price')

# Print sorted product data
for product in product_data:
    print(f"ID: {product['ID']}, Name:{product['Name']}, Price: {product['Price']:.2f}")

