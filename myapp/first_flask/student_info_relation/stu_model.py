from first_flask import db
stu_address=db.Table('stu_address',
                       db.Column('stu_id',db.Integer,db.ForeignKey('student.stuid'),primary_kay=True),
                       db.Column('address_id',db.Integer,db.ForeignKey('address.id'),primary_kay=True)
                       )



class Studentinfo(db.Model):
    __tablename__ = 'student'
    id = db.Column('stuid', db.Integer, primary_key=True)
    first_name = db.Column('name', db.String(50), index=True, unique=True)
    last_name = db.Column('surname', db.String(50), index=True, unique=True)
    stu_detail = db.relationship('Student_information', backref='student', lazy=True, uselist=False,cascade='all,delete')
    address=db.relationship('stu_address',backref='')

    def to_representation(self):
        if self.stu_detail:
            stu_detail = self.stu_detail.to.representation()
        else:
            stu_detail = {}
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'stu_detail': stu_detail
        }


class Student_information(db.Model):
    __tablename__ = 'student_details'
    id = db.Column('id', db.Integer, primary_key=True)
    age = db.Column('age', db.Integer, nullable=True)
    Class = db.Column('Class', db.String(50), unique=True)
    stu_id = db.Column('stu_id', db.Integer, db.ForeignKey('student.stuid'))


    def to_representation(self):
        return {
            'age': self.age,
            'Class': self.Class

        }
class Stu_address(db.Model):
    __tablename__ ='student_address'
    id=db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    city=db.Column('city',db.String(120))
    contact=db.Column('contact',db.Integer,unique=True)

    def to_representation(self):
        return {
            'city':self.city,
            'contact':self.contact
        }



