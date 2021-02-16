from pymysql import connect


class Database:
    def __init__(self):
        try:
            self.db = connect(
                db='person',
                user='root',
                password='',
                host='localhost'
            )
            self.cr = self.db.cursor()
        except:
            print('Error in Connection to DB')


class StudentInsert(Database):
    def __init__(self, name, family, code, birth, addr):
        Database.__init__(self)
        data = (name, family, code, birth, addr)
        query = """INSERT INTO info(name, family, code, birth, address)
        VALUES
        (%s,%s,%s,%s,%s)"""

        self.cr.execute(query, data)
        self.db.commit()


class StudentDelete(Database):
    def __init__(self, id):
        Database.__init__(self)
        data = (id)
        query = "DELETE FROM info WHERE id=%s"

        self.cr.execute(query, data)
        self.db.commit()


class StudentUpdate(Database):
    def __init__(self, name, family, code, birth, addr, id):
        Database.__init__(self)

        data = ( name, family, code, birth, addr, id)
        query = "UPDATE info SET name =%s, family=%s, code=%s, birth=%s, address=%s WHERE id=%s"
        
        self.cr.execute(query, data)
        self.db.commit()


class StudentSelect(Database):
    def __init__(self):
        Database.__init__(self)

        query = "SELECT * FROM info"

        self.cr.execute(query)
        self.result = self.cr.fetchall()

    def get(self):
        return self.result


class StudentGet(Database):
    def __init__(self, id):
        Database.__init__(self)

        query = "SELECT * FROM info WHERE id=%s" %id

        self.cr.execute(query)
        self.result = self.cr.fetchall()

    def get(self):
        return self.result


class StudentSearch(Database):
    def __init__(self, name, family):
        Database.__init__(self)

        name = '%' + name +'%'
        family = '%' + family +'%'

        data = (name, family)

        query = """SELECT * FROM info
        WHERE name LIKE %s AND family LIKE %s"""

        self.cr.execute(query, data)
        self.result = self.cr.fetchall()

    def get(self):
        return self.result


class GradeInsert(Database):
    def __init__(self, studenId, math, physics,chemistry, history, programming):
        Database.__init__(self)
        data = (studenId, math, chemistry,physics, history, programming)
        query = """INSERT INTO grade
        (studentId, math,chemistry,  physics, history, programming)
        VALUES
        (%s,%s,%s,%s,%s,%s)"""
        
        self.cr.execute(query, data)
        self.db.commit()

        
class GradeSelect(Database):
    def __init__(self):
        Database.__init__(self)

        query = "SELECT * FROM grade"

        self.cr.execute(query)
        self.result = self.cr.fetchall()

    def get(self):
        return self.result


class GradeSearch(Database):
    def __init__(self, studenId):
        Database.__init__(self)
        data = (studenId,)
        query = "SELECT * FROM grade WHERE studentId=%s"
        
        self.cr.execute(query, data)
        self.result = self.cr.fetchall()

    def get(self):
        return self.result
