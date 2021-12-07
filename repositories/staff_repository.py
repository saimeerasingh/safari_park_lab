from db.run_sql import run_sql

from models.staff import Staff

def save(staff):
    sql = "INSERT INTO staffs(name,start_date,department,performance_rating) VALUES(%s, %s, %s, %s)RETURNING *"
    values = [staff.name,staff.start_date,staff.department,staff.performance_rating]
    results = run_sql(sql,values)
    id = results[0]['id']
    staff.id = id
    return staff


def select_all():
    staffs = []

    sql = "SELECT * FROM staffs"
    results = run_sql(sql)

    for row in results:
        staff = Staff(row['name'],row['start_date'],row['department'],row['performance_rating'],row['id'])
        staffs.append(staff)
    return staffs

def select(id):
    staff = None
    sql = "SELECT * FROM staffs WHERE id = %s"
    values =[id]
    result = run_sql(sql,values)[0]

    if result is not None:
        staff = Staff(result['name'],result['start_date'],result['department'],result['performance_rating'],result['id'])
    return staff

def delete_all():
    sql = "DELETE FROM staffs WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(staff):
    sql = "UPDATE staffs SET (name,start_date,department,performance_rating)= (%s, %s, %s, %s)RETURNING *"
    values = [staff.name,staff.start_date,staff.department,staff.performance_rating,staff.id]
    run_sql(sql,values)

