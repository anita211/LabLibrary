INSERT INTO books (title, author, publication_year) VALUES
  ('Livro 1', 'Autor 1', 2020),
  ('Livro 2', 'Autor 2', 2021),
  ('Livro 3', 'Autor 3', 2019);

INSERT INTO Loan (loan_date, expected_return_date, status, id_book, id_user)
  VALUES ('2023-11-14', '2023-11-21', 'BORROWED', 1, 1);

INSERT INTO Loan (loan_date, expected_return_date, status, id_material, id_user)
  VALUES ('2023-11-14', '2023-11-21', 'BORROWED', 2, 2);
  
  