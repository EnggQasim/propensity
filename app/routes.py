from app import app

from flask import jsonify, redirect ,url_for, session
from app.exchange import exchange
from app.page import  pagination
import pymysql
from flask import render_template
from flask import request
from flask import Response

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'ubl'
}

def dbs():
    return pymysql.connect("localhost", "root", "", "ubl")
#db = pymysql.connect(**config)


@app.route('/',methods=['GET','POST'])
def index():
    db = dbs()
    results=""
    if 'username' in session:
                return render_template("profile.html", results=results)
    if request.method == "POST":
        user = request.form['Username']
        password = request.form['Password']

        cursor = db.cursor()
        sql = "SELECT * FROM users where user='"+str(user)+"' and pass='"+str(password)+"'"
    
        row_count = cursor.execute(sql)
        # if Data found in database
        if row_count > 0:
            results = cursor.fetchall()
            # if Valid user then go to profile page
            for row in results:
                session['user_id'] = row[0]
                session['username'] = row[1]
                session['type']= row[3]
            if 'username' in session:
                if session['type']=="admin":
                    return redirect(url_for('dashboard'))
                    #dashboard()
                    
                return render_template("profile.html", results=results)
        else:
            log_error = "Not Valid User Name or Password"
        return render_template("index.html", log_error=log_error)        
    else:
        return render_template("index.html", results=results)
    db.close()


@app.route('/logot',methods=['GET','POST'])
def logout():
    db = dbs()
    if 'callers_ids' in session:
        cursor = db.cursor()
        cursor.execute("Select * from calls")
        data1 = cursor.fetchall()
        for row in data1:        
            db_callers_list=row[1].split(",")
        operator_list = session['callers_ids']
        update_list = list(set(map(int,db_callers_list)) - set(map(int,operator_list)))
        cursor.execute('update calls set Customers_lists="%s"'%(str(list(map(int,update_list)))[1:-1]))
        db.commit()
        print('update calls set Customers_lists="%s"'%(str(list(map(int,update_list)))[1:-1]))
        print(update_list)
        print(session['callers_ids'])
    session.pop('callers_ids', None)

    session.pop('username', None)
    session.pop('ids', None)
    session.pop('data', None)
    db.close()
    return redirect(url_for('index'))
    

@app.route('/search',methods=['GET','POST'])
def search():
    db = dbs()
    if request.method=="POST":
        if request.form['search']:
            s=request.form['search']
            cursor = db.cursor()
            sql = "SELECT * FROM customers where cnic='"+str(s)+"' or acc_no='"+str(s)+"'"
            print(sql)
            row_count = cursor.execute(sql)
            # if Data found in database
            if row_count > 0:
                results = cursor.fetchall()
                return render_template("profile.html", s=results)            
    db.close()
    return render_template("profile.html", results="")
    

@app.route("/calls",methods=["POST","GET"])
def calls():
    db = dbs()
    if session.get('callers_ids'):
        ids=session['ids']
        cursor = db.cursor()
        updata = str(list(map(int, session['callers_ids'])))[1:-1]
        cursor.execute("Select * from customers where id in("+updata+")")        
        data = cursor.fetchall()
        return render_template('users.html', resutls=data, callers=ids)
    else:
        data = []
        ids = "Sorry!"
        error = "Sorry!"
        return render_template('users.html', resutls=data, callers=ids, error=error)
    db.close()


@app.route('/customers', methods=['POST','GET'])
def customers_show():
    db = dbs()
    check=1

    cursor = db.cursor()   
    cids = ""
  
    #get All customers list those our All call operatos are calling
    if session.get('ids') ==None:
        cursor.execute("Select * from calls")
        data1 = cursor.fetchall()
        for row in data1:        
            session['ids']=row[1].split(",")
       
    #set values for query
    for i in session['ids']:
        cids += "'"+str(i).strip()+"',"

    cursor.execute('SELECT * FROM customers where (call_status="" or call_status="0" or call_status="cl" or intrest_level="cl") and(id not in('+cids[:-1]+')) order by score desc limit 2')
    print('SELECT * FROM customers where (call_status="" or call_status="0" or call_status="cl" or intrest_level="cl") and(id not in('+cids[:-1]+')) order by score desc limit 2')

    data = cursor.fetchall() 
    session['callers_ids']=[]
    if data:
        for row in data:
            session['ids'].append(str(row[0]))
            session['callers_ids'].append(str(row[0]))
    #set update value base on database column data type 
    if check==1:           
        updata = str(list(map(int, session['ids'])))[1:-1]
        cursor.execute("update calls set Customers_lists='%s'"%(updata))
        db.commit()
        check+=1
    
    print("update calls set Customers_lists='"+updata+"'")
    
    cursor.close()
    db.close()
    return redirect(url_for('calls'),code=307)
    #return render_template('users.html', resutls=data, callers=ids)

@app.route("/call_status_update", methods=['POST','GET'])
def call_status_update():
    db = dbs()
    ## For Timestamp
    import time
    ts = time.time()
    import datetime
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    page=request.form["page"]   
    if page=='home':
        status=request.form["status"]
        call=request.form['call']
        comment=request.form['c']
        pid=request.form['id'] 
        opid=session["user_id"] #Operator Id
        cursor = db.cursor()
        cursor.execute("update customers set call_status=%s, intrest_level='%s', comments='%s', caller_id=%s , time='%s' where id=%s"%(call,status,comment,opid,st,pid))
        db.commit()
        return render_template('profile.html',home_data_update="success")
        
   
    status=request.form["status"]
    call=request.form['call']
    comment=request.form['c']
    pid=request.form['id'] #Customer id
    opid=session["user_id"] #Operator Id
    
    print(len(session['callers_ids']))
    
    if page=='calls': 
        if len(session['callers_ids']) >0:       
            cursor = db.cursor()
            cursor.execute("update customers set call_status=%s, intrest_level='%s', comments='%s', caller_id=%s , time='%s' where id=%s"%(call,status,comment,opid,st,pid))
            db.commit()
            print(session['ids'])
            print(session['callers_ids'])
            if int(pid) in list(map(int,session['callers_ids'])):
                session['callers_ids'].remove(pid)        
                session['ids'].remove(pid)
                #updata calls id in All calls id columns that currently in process
                cursor.execute("Select * from calls")
                data1 = cursor.fetchall()
                for row in data1:           
                    newList=row[1].split(",")
                print(list(map(str.strip, newList)))
                NewList = list(map(int,newList))
                NewList.remove(int(pid))
                cursor.execute('update calls set Customers_lists="%s"'%(str(NewList)[1:-1]))
                db.commit()
                print("Update====================",newList)
                print("pid===",pid)
            else:
                session['callers_ids']=[]
                session['ids']=[0]
            
            
            session.modified = True
            print(session['ids'])
            print(session['callers_ids'])
            updata = str(list(map(int, session['callers_ids'])))[1:-1]
            if not len(session['callers_ids'])==0:
                cursor.execute("Select * from customers where id in("+updata+")")     
                data = cursor.fetchall()
            else:
                error="Sorry!"
                return render_template('users.html', error=error, callers=session['ids'])
            return render_template('users.html', resutls=data, callers=session['ids'])
        
        else:
            error = "Sorry"
            return render_template('users.html', error=error, callers=session['ids'])
    db.close()
        
#=================Dashboard====================
# confusion matrix
@app.route("/confusion_matrix", methods=['POST','GET'])
def confusion_matrix():
    db = dbs()
    cursor = db.cursor()
    #True Positive
    rows = cursor.execute('select count(*) from customers where intrest_level=1 and predict_intrest_level=1')
    data = cursor.fetchall()
    if rows > 0:
        for row in data:
            tp=row[0]
    # False Positive
    rows = cursor.execute('select count(*) from customers where intrest_level=0 and predict_intrest_level=1')
    data = cursor.fetchall()
    if rows > 0:
        for row in data:
            fp=row[0]
    #True Negative
    rows = cursor.execute('select count(*) from customers where intrest_level=1 and predict_intrest_level=0')
    data = cursor.fetchall()
    if rows > 0:
        for row in data:
            tn=row[0]
    #False Negative
    rows = cursor.execute('select count(*) from customers where intrest_level=0 and predict_intrest_level=0')
    data = cursor.fetchall()
    if rows > 0:
        for row in data:
            fn=row[0]    
    return render_template("profile.html", tp=tp, fp=fp, tn=tn, fn=fn)

# confusion matrix
@app.route("/dashboard", methods=['POST','GET'])
def dashboard():
    db = dbs()
#SELECT date(time) as date,count(case when intrest_level=1 then 1 end) as success ,count(case when intrest_level=0 then 1 end) as failer from customers group by date(time)
    cursor = db.cursor()
    cursor.execute('SELECT date(time) as date,count(case when intrest_level=1 then 1 end) as success ,count(case when intrest_level=0 then 1 end) as failer from customers  group by date(time) ORDER BY date(time) LIMIT 30')
    data = cursor.fetchall()    

    cursor.execute('SELECT count(case when intrest_level=1 and predict_intrest_level=1 then 1 end) as tp, count(case when intrest_level=0 and predict_intrest_level=1 then 1 end) as fp, count(case when intrest_level=1 and predict_intrest_level=0 then 1 end) as tn, count(case when intrest_level=0 and predict_intrest_level=0 then 1 end) as tp from customers order by date(time) desc LIMIT 30')
    matrix = cursor.fetchall()
    
    cursor.close()
    db.close()

    
    return render_template("profile.html", success=data, matrix=matrix)