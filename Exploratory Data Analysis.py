import pandas as pd
import sqlite3

# creating database connection
conn = sqlite3.connect('inventory.db')

# checking tables present in the database
tables = pd.read_sql_query("  select * from sqlite_master where type ='table' ",conn)
tables

for table in tables['name']:
    print('-'*50, f'{table}','-'*50)
    print('count of records: ', pd.read_sql(f"select count(*) as count from {table}",conn)['count'].values[0])
    print(pd.read_sql(f"select * from {table} limit 5",conn))

   # Save sales table to variable
    if table == "sales":
        sales = pd.read_sql(f"SELECT * FROM {table}", conn)

purchases = pd.read_sql_query("select * from purchases where VendorNumber = 4466", conn)
purchases.columns

sales = pd.read_sql_query("select * from sales where VendorNo = 4466", conn)
sales.columns

purchase_prices = pd.read_sql_query("select * from purchase_prices where VendorNumber = 4466", conn)
purchase_prices.columns

vendor_invoice = pd.read_sql_query("select * from vendor_invoice where VendorNumber = 4466", conn)
vendor_invoice.columns

purchases.groupby(['Brand','PurchasePrice'])[['Quantity','Dollars']].sum()

sales.groupby('Brand')[['SalesDollars','SalesPrice','SalesQuantity']].sum()

freight_summary = pd.read_sql_query("""
SELECT VendorNumber, SUM(Freight) AS FreightCost
FROM vendor_invoice
GROUP BY VendorNumber
""", conn)

pd.read_sql_query("""
SELECT 
    p.VendorNumber,
    p.VendorName,
    p.Brand,
    p.PurchasePrice,
    pp.Volume,
    pp.Price AS ActualPrice,
    SUM(p.Quantity) AS TotalPurchaseQuantity,
    SUM(p.Dollars) AS TotalPurchaseDollars
FROM purchases p
JOIN purchase_prices pp
    ON p.Brand = pp.Brand
WHERE p.PurchasePrice > 0
GROUP BY p.VendorNumber, p.VendorName, p.Brand
ORDER BY TotalPurchaseDollars
""", conn)

pd.read_sql_query("""
SELECT 
    VendorNo,
    Brand,
    SUM(SalesDollars) AS TotalSalesDollars,
    SUM(SalesPrice) AS TotalSalesPrice,
    SUM(SalesQuantity) AS TotalSalesQuantity,
    SUM(ExciseTax) AS TotalExciseTax
FROM sales
GROUP BY VendorNo, Brand
ORDER BY TotalSalesDollars
""", conn)

vendor_sales_summary = pd.read_sql_query("""
WITH FreightSummary AS (
    SELECT VendorNumber, SUM(Freight) AS FreightCost
    FROM vendor_invoice
    GROUP BY VendorNumber
),

PurchaseSummary AS (
    SELECT 
        p.VendorNumber,
        p.VendorName,
        p.Brand,
        pp.Description,          
        p.PurchasePrice,
        pp.Volume,
        pp.Price AS ActualPrice,
        SUM(p.Quantity) AS TotalPurchaseQuantity,
        SUM(p.Dollars) AS TotalPurchaseDollars
    FROM purchases p
    JOIN purchase_prices pp
        ON p.Brand = pp.Brand
    WHERE p.PurchasePrice > 0
    GROUP BY 
        p.VendorNumber, p.VendorName, p.Brand, pp.Description  
),

SalesSummary AS (
    SELECT 
        VendorNo,
        Brand,
        SUM(SalesDollars) AS TotalSalesDollars,
        SUM(SalesPrice) AS TotalSalesPrice,
        SUM(SalesQuantity) AS TotalSalesQuantity,
        SUM(ExciseTax) AS TotalExciseTax
    FROM sales
    GROUP BY VendorNo, Brand
)

SELECT
    ps.VendorNumber,
    ps.VendorName,
    ps.Brand,
    ps.Description,
    ps.PurchasePrice,
    ps.ActualPrice,
    ps.Volume,
    ps.TotalPurchaseQuantity,
    ps.TotalPurchaseDollars,
    ss.TotalSalesQuantity,       
    ss.TotalSalesDollars,
    ss.TotalSalesPrice,
    ss.TotalExciseTax,
    fs.FreightCost
FROM PurchaseSummary ps
LEFT JOIN SalesSummary ss
    ON ps.VendorNumber = ss.VendorNo
    AND ps.Brand = ss.Brand
LEFT JOIN FreightSummary fs
    ON ps.VendorNumber = fs.VendorNumber
ORDER BY ps.TotalPurchaseDollars DESC
""", conn)

vendor_sales_summary.isnull().sum()

vendor_sales_summary.dtypes

vendor_sales_summary['VendorName'].unique()
vendor_sales_summary['Volume'] = vendor_sales_summary['Volume'].astype('float64')
vendor_sales_summary.fillna(0, inplace=True)
vendor_sales_summary['VendorName'] = vendor_sales_summary['VendorName'].str.strip()
vendor_sales_summary['GrossProfit'] = vendor_sales_summary['TotalSalesDollars'] - vendor_sales_summary['TotalPurchaseDollars']
vendor_sales_summary['ProfitMargin'] = (vendor_sales_summary['GrossProfit'] / vendor_sales_summary['TotalSalesDollars']) * 100
vendor_sales_summary['StockTurnover'] = vendor_sales_summary['TotalSalesQuantity'] / vendor_sales_summary['TotalPurchaseQuantity']
vendor_sales_summary['SalestoPurchaseRatio'] = vendor_sales_summary['TotalSalesDollars'] / vendor_sales_summary['TotalPurchaseDollars']
vendor_sales_summary.columns
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE vendor_sales_summary (
    VendorNumber INT,
    VendorName VARCHAR(100),
    Brand INT,
    Description VARCHAR(100),
    PurchasePrice DECIMAL(10,2),
    ActualPrice DECIMAL(10,2),
    Volume DECIMAL(10,2),
    TotalPurchaseQuantity INT,
    TotalPurchaseDollars DECIMAL(15,2),
    TotalSalesQuantity INT,
    TotalSalesDollars DECIMAL(15,2),
    TotalSalesPrice DECIMAL(15,2),
    TotalExciseTax DECIMAL(15,2),
    FreightCost DECIMAL(15,2),
    GrossProfit DECIMAL(15,2),
    ProfitMargin DECIMAL(15,2),
    StockTurnover DECIMAL(15,2),
    SalesToPurchaseRatio DECIMAL(15,2),
    PRIMARY KEY (VendorNumber, Brand)
);
""")
pd.read_sql_query("SELECT * FROM  vendor_sales_summary ",conn)
vendor_sales_summary.to_sql('vendor_sales_summary',conn, if_exists = 'replace', index = 'false')