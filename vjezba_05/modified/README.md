```

remember to swap python.exe for anacondas python, maybe some sql shit from previous
exercise aswell...

# "C:\ProgramData\Anaconda3\python.exe" -m pip install mysql-connector
 
name of db: jnkiwavj5
one table is called "sessions" (session_id, data; from previous exercise probably)
table called "users" (id, ime, email, password; as described below)
table calles "subjects" (id, kod, ime, bodovi, godina; as described below)

WARN: these names are case sensitive and should be exact

------------------------------------------

"Podatke o korisniku cuvati u bazi podataka u tablici users.
Tablica ce imati cetiri stupca: 
    id (primarni kljuc),
    ime (varchar 100),
    email (varchar 100 i postaviti ga na razini baze na unique)
    password (binary 64, jer ce sadrzavati hash)."

"Rjecnik subjects iz datoteke subjects.py zamijeniti tablicom „subjects” u bazi podataka.
Tablica ce imati sljedece stupce:
    id (int, AI (autoinkrement), primarni kljuc),
    kod (varchar),
    ime (varchar 100),
    bodovi (int),
    godina (int).
Rucno popuniti tablicu podacima iz rjecnika"

--------------------

subjects = {
    'ip' : { 'name' : 'Introduction to programming' , 'year' : 1, 'ects' : 6 },
    'c1' : { 'name' : 'Calculus 1' , 'year' : 1, 'ects' : 7 },
    'cu' : { 'name' : 'Computer usage' , 'year' : 1, 'ects' : 5 },
    'dmt' : { 'name' : 'Digital and microprocessor technology', 'year' : 1, 'ects' : 6 },
    'db' : { 'name' : 'Databases' , 'year' : 2, 'ects' : 6 },
    'c2' : { 'name' : 'Calculus 2' , 'year' : 2, 'ects' : 7 },
    'dsa' : { 'name' : 'Data structures and alghoritms' , 'year' : 2, 'ects' : 5 },
    'ca' : { 'name' : 'Computer architecture', 'year' : 2, 'ects' : 6 },
    'isd' : { 'name' : 'Information systems design' , 'year' : 3, 'ects' : 5 },
    'c3' : { 'name' : 'Calculus 3' , 'year' : 3, 'ects' : 7 },
    'sa' : { 'name' : 'Server Architecture' , 'year' : 3, 'ects' : 6 },
    'cds' : { 'name' : 'Computer and data security', 'year' : 3, 'ects' : 6 }
    };
    
```