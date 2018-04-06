"""Convert json object to an object."""

import json
import names
import sys

from flask import Flask

from employee import Employee


app = Flask(__name__)


@app.route("/getEmployeeList")
def get_employee_list():
    """Initialise an employee list."""
    try:

        employee_list = []

        # Create instances for filling up employee list.
        for i in range(0, 5):
            employee = Employee(names.get_first_name(), names.get_last_name())
            employee_list.append(employee)

        # Convert to json
        json_str = json.dumps([e.to_json() for e in employee_list])

    except:
        print("Error ", sys.exe_info()[0])

    return json_str


# Conver db cursor result set to json
    # resultSet = cursor.fetchall()
    # empList = []
    # for emp in resultSet:
    #     empDict = {
    #         'Id': emp[0],
    #         'Name': emp[1],
    #         'Location': emp[2],
    #         'Address': emp[3]}
    #     empList.append(empDict)
    # return json.dumps(empList)


if __name__ == "__main__":
    app.run()
