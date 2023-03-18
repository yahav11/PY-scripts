
-- switch to the new database
USE bank;

-- create the banking table
CREATE TABLE banking (
  PersonID int,
  CustomerID int,
  Name varchar(255),
  PhoneNumber varchar(20),
  AccountBalance int
);

-- insert data into the banking table
INSERT INTO banking (PersonID, CustomerID, Name, PhoneNumber, AccountBalance)
VALUES (1, 12345, 'Yahav', '052765284', 200);

INSERT INTO banking (PersonID, CustomerID, Name, PhoneNumber, AccountBalance)
VALUES (2, 54321, 'Dani', '052052052', 2500);