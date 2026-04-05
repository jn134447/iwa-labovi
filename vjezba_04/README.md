steps to recreate on labs:
    - use anacondas python 3.8
    - install the sql shit with:
        $ "path to python.exe of ver 3.11 or before" -m pip install mysql-connector 
    - run xampp:
        1. start apache
        2. start mysql
    - adming panel of mysql:
        1. create new database, name it whatever...
        2. create a new table called "sessions" (the name is very fucking important)
            with 2 rows
        3. one of the rows needs to be named "session_id" (exactly as it fucking says here)
        4. the other row needs to be named "data" (you get the fucking idea)
        5. "session_id" has to be Autonumber, Primary key
        6. "data" has to be Text
        7. should take you like 3 clicks with the mouse to do this
    - website shit:
        1. change the copy-pasted db.py from her example (the one with bigger line count)
            1.1 change the name of database to the one you picked before
            1.2 change the stupid fucking add_to_session() function with ur own website logic
        2. the rest is self explanitory:
            -- PUT info into db:
                if (os.environ["REQUEST_METHOD"].upper() == "POST"):
                    session.add_to_session(params) 
            -- PULL info out of db:
                session_id = session.get_or_create_session_id()
                _,session_data = db.get_session(session_id)
            -- session_data contains a python dictionary btw
        3. keep the params logic cause its required, just remove cookies shit
        4. oh btw db.py relies on session.py, also copy the one from the examples that has the higher line count
    - good job you have the most useless fucking website that can be
        hacked in fucking miliseconds by an AI crawler dropping ur entire database
