from flask import Blueprint,request,jsonify

from first_flask import db
from first_flask.student_info_relation.stu_model import Studentinfo,Student_information

mod=Blueprint('first_flask_relation',__name__,url_prefix='/stu_info')

@mod.route('/create_user',methods=['POST'])
def Cretae_user():
    stu_data=request.get_json()
    stu=Studentinfo(
        first_name=stu_data['first_name'],
        last_name=stu_data['last_name']
    )
    db.session.add(stu)
    db.session.commit()
    return "User add successfully!!"

@mod.route('/add_data',methods=['POST'])
def add_data():
    stu_data=request.get_json()
    stu=Student_information(
        age=stu_data['age'],
        Class=stu_data['Class'],
        stu_id=stu_data['stu_id']
    )
    db.session.add(stu)
    db.session.commit()
    return "user add age and class successfully!!"


@mod.route('/delete/<user_id>/',methods=['DELETE'])
def delete_user(user_id):
    user = Studentinfo.query.get(int(user_id))
    db.session.delete(user)
    db.session.commit()
    return "user deleted "

@mod.route('/get_data',methods=['GET'])
def fetch_stu():
    stu=Studentinfo.query.all()
    response=[x.to_representation() for x in stu]
    return jsonify(response)