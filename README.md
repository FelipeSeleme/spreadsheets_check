# spreadsheets_check
This code reads and compares the values between spreadsheets in the financial and accounting sectors of a company.
  
The problem was that the accounting entries needed to be checked against the financial realized in large amounts. Also, 
the data did not have any kind of primary key. The amounts could occur in fractions, spread across different cost centers, 
with no direct relationship between the data in the two spreadsheets. It was necessary to group accounts by sector, 
create a key, calculate totals and differences, then return a third consolidated spreadsheet.