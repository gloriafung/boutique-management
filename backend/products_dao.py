from sql_connect import get_sql_connection 

def get_all_products(connection): 
    cursor = connection.cursor()
    cnx = mysql.connector.connect(user='root', password='root', 
                              host='127.0.0.1', database='clothing_store') 
                              
    cursor = cnx.cursor() 
    
    query = ("select products.product_id, products.name, products.SKU, products.unit_price, " 
         "products.category_id, products.size_id, size.size, category.category " 
         "from products " 
         "inner join size " 
         "on products.size_id = size.size_id " 
         "inner join category " 
         "on products.category_id = category.category_id") 
         
    cursor.execute(query) 
    
    result = []
    
    for (product_id, name, SKU, unit_price, category_id, size_id, size, category) in cursor: 
        result.append(
            
            { 
                'product_id': product_id, 
                'name': name,
                'SKU': SKU, 
                'unit_price': unit_price,
                'category_id': category_id,
                'size_id': size_id,
                'size': size,
                'category': category 
            }  
        )
        

    return result  

    if __name__ == '__main__': 
        connection = get_sql_connection()
        print(get_all_products(connection)) 