import mysql.connector
def dbconn():
    with mysql.connector.connect(host='spm.ctbgpu7gycn4.ap-northeast-1.rds.amazonaws.com',user='admin',password='Datta2521',db='spm') as conn:
        cursor=conn.cursor()
        cursor.execute('create table if not exists students(rollno varchar(6) primary key,name varchar(30),std_group varchar(10),password varchar(15),email varchar(70))')
        cursor.execute('create table if not exists notes(nid int primary key auto_increment,rollno varchar(6),title varchar(30),content text,date datetime default now(),foreign key(rollno) references students(rollno))')
        cursor.execute('create table if not exists files(fid int primary key auto_increment,rollno varchar(6),filename varchar(30),filedata longblob,date datetime default now(),foreign key(rollno) references students(rollno))')

