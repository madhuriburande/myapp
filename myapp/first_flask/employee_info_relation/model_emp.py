# from first_flask import db

#######--------use code for one to one relationship -----------------####
# class Employeeinfo(db.Model):  ## class name
#     __tablename__ = 'emp'  ## table name by using orm
#     id = db.Column('empid', db.Integer, primary_key=True)  ## in table column name like empid,empname etc.
#     username = db.Column('empname', db.String(45), index=True, unique=True)
#     email = db.Column('emp_email', db.String(45), unique=True)
#     password = db.Column('pwd', db.String(120))
#     emp_detail= db.relationship('EmpDetails', backref='emp', lazy=True, uselist=False, cascade='all,delete')
#
#     #addresses=db.relationship('Address',secondary=emp_addresses,backref='user',lazy=,cascade='all,delete')
#     def to_representation(self):
#         if self.emp_detail:
#             emp_detail= self.emp_detail.to_representation()
#         else:
#             emp_detail = {}
#         return {
#             'username': self.username,
#             'email': self.email,
#             'password': self.password,
#             'emp_detail': emp_detail
#         }
# ##### user for one to one relationship ------------------###
# class EmpDetails(db.Model):
#     __tablename__="emp_details"
#     id=db.Column('id',db.Integer,primary_key=True,autoincrement=True)
#     age=db.Column('emp_age',db.Integer,nullable=True)
#     emp_id=db.Column('emp_id',db.Integer,db.ForeignKey('emp.empid'),nullable=False)
#
#     def to_representation(self):
#         return {
#             'age':self.age
#         }
#
### -----------------------use code for many to many relationship ------------------##

from first_flask import db
emp_addresses=db.Table('emp_addresses',
                       db.Column('emp_id',db.Integer,db.ForeignKey('emp.empid'),primary_kay=True),
                       db.Column('address_id',db.Integer,db.ForeignKey('address.id'),primary_kay=True)
                       )

class Employeeinfo(db.Model):  ## class name
    __tablename__ = 'emp'  ## table name by using orm
    id = db.Column('empid', db.Integer, primary_key=True)  ## in table column name like empid,empname etc.
    username = db.Column('empname', db.String(45), index=True, unique=True)
    email = db.Column('emp_email', db.String(45), unique=True)
    password = db.Column('pwd', db.String(120))
    emp_detail= db.relationship('EmpDetails', backref='emp', lazy=True, uselist=False, cascade='all,delete')
    addresses=db.relationship('Address',secondary=emp_addresses,backref='emp',lazy='joined',cascade='all,delete')


    def to_representation(self):
        if self.emp_detail:
            emp_detail= self.emp_detail.to_representation()
        else:
            emp_detail = {}
        address=[x.to_representation() for x in self.addresses]
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'emp_detail': emp_detail,
            'address':address
        }

class EmpDetails(db.Model):
    __tablename__="emp_details"
    id=db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    age=db.Column('emp_age',db.Integer,nullable=True)
    emp_id=db.Column('emp_id',db.Integer,db.ForeignKey('emp.empid'),nullable=False)

    def to_representation(self):
        return {
            'age':self.age
        }

class Address(db.Model):
    __tablename__='address'
    id=db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    city=db.Column('city',db.String(120),nullable=True)

    def to_representation(self):
        return {
            'city':self.city
        }
