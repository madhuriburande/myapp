from flask import Blueprint,request,jsonify

from first_flask import db
from first_flask.employee_info_relation.model_emp import Employeeinfo,EmpDetails,Address,emp_addresses

import json

mod = Blueprint('employee_info_relation', __name__, url_prefix='/emp_info')

@mod.route('/create_user',methods=['POST'])
def Create_user():
    emp_data=request.get_json()
    emp=Employeeinfo(
        username=emp_data['username'],
        email=emp_data['email'],
        password=emp_data['password']

    )
    db.session.add(emp)
    db.session.commit()
    return "User add sucessfully."

@mod.route('/add_age',methods=['POST'])
def Add_age():
    emp_data=request.get_json()
    emp=EmpDetails(
        age=emp_data['age'],         # here we add multiple time age on postman like 1st we add 27 then send again add 25 then it will not change becouse we get primary key or duplicate not allow
        emp_id=emp_data['emp_id']      ## here use foreign key so empandemp_details id are avilable both side.
    )
    db.session.add(emp)
    db.session.commit()
    return "User age add successfully."



@mod.route('/add_address',methods=['POST'])
def Add_adr():
    emp_data=request.get_json()
    emp_id=emp_data['empid']
    address=Address(
        city=emp_data['city']
    )
    emp=Employeeinfo.query.get(emp_id)
    emp.addresses.append(address)
    db.session.commit()
    return "User address added successfully."




@mod.route('/get_data',methods=['GET'])
def fetch_user():
    emp=Employeeinfo.query.all()
    response=[x.to_representation() for x in emp]     ## fetch the data both
    return jsonify(response)






