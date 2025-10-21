import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="exampledb",
)

# 커서 생성 -> 명령어 작성 가능
cursor = conn.cursor()

# 명령어 실행
sql1 = """
INSERT INTO employees(ID,name,DeptID,ManagerID)
VALUES('8','KENNETH',8,'101');
"""
cursor.execute(sql1)
conn.commit()
print("데이터 삽입 완료")

# 연결 해제
conn.close()