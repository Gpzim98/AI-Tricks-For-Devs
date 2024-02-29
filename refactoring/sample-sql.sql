SELECT a, b, (SELECT d FROM Table2 t2 WHERE t2.e = t1.b AND t2.f = 
    (SELECT MAX(f) FROM Table2 WHERE e = t2.e)) as nested_query, g 
    FROM Table1 t1, Table2 WHERE Table1.b = Table2.e AND EXISTS 
    (SELECT * FROM Table3 WHERE Table3.h = Table2.g) AND a IN 
    (SELECT a FROM Table1 WHERE c NOT IN 
    (SELECT c FROM Table4 WHERE Table4.j = Table1.a AND k < NOW())) ORDER BY a;