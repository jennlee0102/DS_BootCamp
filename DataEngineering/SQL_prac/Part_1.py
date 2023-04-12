"""
Part 1.1
Create database as the given schema.
Create three tables.
"""

CREATE_USER_TABLE = """
CREATE TABLE User (
        id INTEGER PRIMARY KEY,
        username VARCHAR,
        password VARCHAR
);
"""

CREATE_PRODUCT_TABLE = """
CREATE TABLE Product (
        id INTEGER PRIMARY KEY,
        product_name VARCHAR,
        product_price INTEGER
);
"""

CREATE_USER_PRODUCT_TABLE = """
CREATE TABLE User_Product (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES User(id),
        FOREIGN KEY (product_id) REFERENCES Product(id)
);
"""


"""
Write SQL.
"""

# 1. List 10 most expensive products (price per each) and include only name of the producs for the result.
SQL_QUERY_1 = """
SELECT Product.ProductName
FROM Product
ORDER BY Product.UnitPrice DESC
LIMIT 10;
"""

# 2. calculate the average age of employees when they were employed
SQL_QUERY_2 = """
SELECT AVG(STRFTIME('%Y', e.HireDate) - STRFTIME('%Y', e.BirthDate))
AS AvgAgeAtHire
FROM Employee e;
"""

# 3.In addition to #1 include the companies that made the products in the query result, with the following columns:
#   product id, product name, unit price, and company name.
SQL_QUERY_3 = """
SELECT p.Id, p.ProductName, p.UnitPrice, s.CompanyName
FROM Product p
JOIN Supplier s ON p.SupplierId = s.Id
ORDER BY p.UnitPrice DESC
LIMIT 10;
"""

# 4. What is the category that has the most types of products? (Only one category name should be outputted)
SQL_QUERY_4 = """
SELECT c.CategoryName
FROM Category c
JOIN Product p ON c.Id = p.CategoryId
GROUP BY c.Id
ORDER BY COUNT(DISTINCT p.ProductName) DESC
LIMIT 1;
"""

# 5. Calculate the average age of employees when employed for each city.
# Include the city name and the average age of employees at the time of employment in the query result.
SQL_QUERY_5 = """
SELECT e.City, AVG(STRFTIME('%Y', e.HireDate) - STRFTIME('%Y',e.BirthDate))
AS AverageAge
FROM Employee e
GROUP BY e.City;
"""

# 6. Who has the most territories among employees?
# Include employee id, employee lastname, and total number of territories in the query result.
SQL_QUERY_6 = """
SELECT e.Id, e.LastName, COUNT(et.TerritoryId) AS TotalTerritories
FROM Employee e
JOIN EmployeeTerritory et ON e.Id = et.EmployeeId
GROUP BY e.Id
ORDER BY TotalTerritories DESC
LIMIT 1;
"""
