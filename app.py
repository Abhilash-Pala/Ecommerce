from flask import Flask, render_template, url_for, redirect, request, flash, session,Response
from flask_session import Session
import bcrypt
import mysql.connector
from otp import genotp
from cmail import sendmail
from tokens import token 
from keys import secret_key, salt1, salt2
from itsdangerous import URLSafeTimedSerializer
import os
import stripe
import pdfkit
stripe.api_key="sk_test_51MMsHhSGj898WTbYXSx509gD14lhhXs8Hx8ipwegdytPB1Bkw0lJykMB0yGpCux95bdw1Gk9Gb9nJIWzPEEDxSqf00GEtCqZ8Y"

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
app.secret_key = b'@\xdd/%ea'
config=pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
mydb = mysql.connector.connect(host='localhost', user="root", password="Admin", db="ecommy")
# user=os.environ.get('RDS_USERNAME')
# db=os.environ.get('RDS_DB_NAME')
# password=os.environ.get('RDS_PASSWORD')
# host=os.environ.get('RDS_HOSTNAME')
# port=os.environ.get('RDS_PORT')
# with mysql.connector.connect(host=host,port=port,user=user,password=password,db=db) as conn:
#     cursor=conn.cursor()
#     cursor.execute("CREATE TABLE if not exists vendor ( email varchar(50) NOT NULL, name varchar(150) NOT NULL,mobile_no bigint DEFAULT NULL,address text NOT NULL,password varbinary(255) DEFAULT NULL,PRIMARY KEY (email),UNIQUE KEY mobile_no (mobile_no),UNIQUE KEY mobile_no_2 (mobile_no) )")
#     cursor.execute("CREATE TABLE user ( username varchar(255) NOT NULL,mobile_no bigint NOT NULL,email varchar(255) NOT NULL,address text NOT NULL, password varbinary(255) DEFAULT NULL,PRIMARY KEY (email),UNIQUE KEY mobile_no (mobile_no))")
#     cursor.execute("CREATE TABLE additem (item_id binary(16) NOT NULL,item_name longtext NOT NULL,discription longtext,quantity int DEFAULT NULL,category enum('Electronics','Grocery','Fashion','Home') DEFAULT NULL,price int DEFAULT NULL,addedby varchar(100) DEFAULT NULL,imgid varchar(200) DEFAULT NULL,p_link text,PRIMARY KEY (item_id),KEY addedby (addedby), CONSTRAINT additem_ibfk_1 FOREIGN KEY (addedby) REFERENCES vendor (email) ON DELETE CASCADE ON UPDATE CASCADE)")
#     cursor.execute("CREATE TABLE orders ( ordid binary(16) NOT NULL,itemid binary(16) NOT NULL,item_name varchar(255) DEFAULT NULL,qty int DEFAULT NULL,total_price decimal(20,4) DEFAULT NULL,user varchar(255) DEFAULT NULL,category varchar(255) DEFAULT NULL,imgid binary(16) DEFAULT NULL,dis longtext,PRIMARY KEY (ordid),KEY itemid (itemid),KEY user (user),CONSTRAINT orders_ibfk_1 FOREIGN KEY (itemid) REFERENCES additem (item_id) ON DELETE CASCADE,CONSTRAINT orders_ibfk_2 FOREIGN KEY (user) REFERENCES user (email) ON DELETE SET NULL ON UPDATE CASCADE)")
#mydb=mysql.connector.connect(host=host,user=user,port=port,password=password,db=db)
@app.route('/')
def home():
    return render_template('welcome.html')


@app.route('/vendorsignup', methods=["GET", "POST"])
def vendorsignup():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        mobile_no = request.form['mobile_no']
        address = request.form['address']
        password = request.form['password']
        
        try:
            cursor = mydb.cursor(buffered=True)
            cursor.execute('select count(*) from vendor where email=%s', [email])
            count = cursor.fetchone()[0]
            if count == 1:
                raise Exception
        except Exception as e:        
            flash("Email already exists")
            return redirect(url_for('vendorsignup'))
        else:
            otp = genotp() 
            data = {'email': email, 'name': name, 'mobile_no': mobile_no, 'address': address, 'password': password, 'otp': otp}
            subject = 'OTP for Vendor Application' 
            body = f'This is the OTP for Ecom verification: {otp}' 
            sendmail(to=email, subject=subject, body=body)
            otp_token = token(data=data, salt=salt1)
            flash('OTP has been sent to the given Email, please check.')
            return redirect(url_for('otp', data=otp_token))
    return render_template('vendorsignup.html')        

@app.route('/otp/<data>', methods=['GET', 'POST']) 
def otp(data):
    try:
        serializer = URLSafeTimedSerializer(secret_key)
        data = serializer.loads(data, salt=salt1, max_age=360)
    except Exception as e:
        print(e)
        flash("OTP has expired")
        return render_template('otp.html')
    else:
        if request.method == 'POST':
            uotp = request.form['otp']
            if uotp == data['otp']:
                bytes=data['password'].encode('utf-8')
                salt=bcrypt.gensalt()
                hash=bcrypt.hashpw(bytes,salt)
                cursor = mydb.cursor(buffered=True)
                cursor.execute('INSERT INTO vendor (name, email, mobile_no, address, password) VALUES (%s, %s, %s, %s, %s)',
                               (data['name'], data['email'], data['mobile_no'], data['address'], hash))
                mydb.commit()
                cursor.close()
                flash('Registration has been successfully done')
               
                return redirect(url_for('vendorlogin'))
            else:
                flash('OTP was incorrect') 
                return redirect(url_for('otp', data=data))
    return render_template('otp.html')

@app.route('/vendorlogin', methods=["GET","POST"])
def vendorlogin():
    if session.get('vendor'): 
        return redirect(url_for('web'))            
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = mydb.cursor(buffered=True)
        cursor.execute('SELECT password FROM vendor WHERE email = %s', [email])
        hashed_password = cursor.fetchone()
        if hashed_password:
            hashed_password=hashed_password[0]
            if bcrypt.checkpw(password.encode('utf-8'),hashed_password):
                session['vendor']=email
                if not session['vendor']:
                    session[email]={}
                return redirect(url_for('web'))
            else:
                flash('password incorrect')
                return redirect(url_for('vendorlogin'))
        else:
            flash('email not registered') 
            return redirect(url_for('vendorsignup')) 
    return render_template('vendorlogin.html')      


                
               
    

@app.route('/web', methods=["GET", "POST"])
def web():
    if session.get('vendor'):
        return render_template('vendord.html')
    else:
        return redirect(url_for('vendorlogin'))    
    return render_template('web.html',user_email=user_email) 

@app.route('/v_logout',methods=["GET","POST"])
def v_logout():
    if session.get('vendor'):
        session.pop('vendor')
        return redirect(url_for('vendorlogin'))
    else:
        return redirect(url_for('vendorlogin'))    

@app.route('/additems',methods=["GET","POST"])
def additems():
    if session.get('vendor'):
        if request.method=='POST':
            name=request.form['name']
            dis=request.form['desc']
            qyt=request.form['qyt']
            category=request.form['category']
            price=request.form['price']
            
            img=request.files['image']
            
            imgextension=img.filename.split('.')[-1]
            imgname=genotp()
            
            filename=imgname+'.'+imgextension
            # imgname=product.filename
            # print(imgname)
            path=os.path.dirname(os.path.abspath(__file__))
            static_path=os.path.join(path,'static')
            img.save(os.path.join(static_path,filename))
            cursor=mydb.cursor(buffered=True)
            cursor.execute('insert into additem(item_id, item_name, discription, quantity, category, price, addedby, imgid) values(uuid_to_bin(uuid()), %s, %s, %s, %s, %s, %s, %s)', [name, dis, qyt, category, price, session.get('vendor'),filename])
            mydb.commit()
            cursor.close()
            flash(f'Item {name} successfully added')
            return redirect(url_for('web'))
    return render_template('additem.html')

@app.route('/viewitems')
def viewitems():
    if session.get('vendor'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('''select bin_to_uuid(item_id), item_name,discription, quantity, category, price,addedby, imgid,p_link from additem where addedby=%s''',[session.get('vendor')])
        count=cursor.fetchall()
        print(count)
        if count: 
            return render_template('vendord.html',count=count)
        else:
            return render_template('vendord.html')     
           
        
    else:
        return redirect(url_for('vendorlogin'))          
    
@app.route('/delete/<item_id>')
def delete(item_id):
    if session.get('vendor'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('''select imgid from additem where item_id=uuid_to_bin(%s) and addedby=%s''',[item_id,session.get('vendor')])
        count=cursor.fetchone()
        print(count)
        path=os.path.dirname(os.path.abspath(__file__))
        static_path=os.path.join(path,'static')
        file_path=os.path.join(static_path,count[0])
        
        # os.remove(file_path)
        cursor.execute('delete from additem where item_id=uuid_to_bin(%s) and addedby=%s',[item_id,session.get('vendor')])
        
        
        mydb.commit()
        cursor.close()  
        flash(f'Item {item_id} has deleted successfully')
        return redirect(url_for('viewitems'))
    
    return redirect(url_for('vendorlogin')) 

@app.route('/update/<item_id>',methods=["GET","POST"])
def update(item_id):
    if session.get('vendor'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('''select bin_to_uuid(item_id), item_name,discription, quantity, category, price,addedby, imgid from additem where item_id=uuid_to_bin(%s) and addedby=%s''',[item_id,session.get('vendor')])
        count=cursor.fetchall()
        if request.method=="POST":
            name=request.form['name']
            discription=request.form['desc']
            quantity=request.form['qyt']
            category=request.form['category']
            price=request.form['price']
           
            if request.files['image'].filename=='':
            
                filename=count[0][7]
            else:
                img=request.files['image']
                imgextension=img.filename.split('.')[-1]
                imgname=genotp()
                filename=imgname+'.'+imgextension
                
                
                path=os.path.dirname(os.path.abspath(__file__))
                static_path=os.path.join(path,'static')
                file_path=os.path.join(static_path,count[0][7])
                os.remove(file_path)
                
                img.save(os.path.join(static_path,filename)) 
            
                
                
            
                # img.save(os.path.join(static_path,imgname))
            cursor=mydb.cursor(buffered=True)
            cursor.execute('update additem set item_name=%s,discription=%s,quantity=%s,category=%s,price=%s,imgid=%s where item_id=uuid_to_bin(%s)',[name,discription,quantity,category,price,filename,item_id])
            mydb.commit()
            cursor.close()
                
            
            flash(f'item {name} updated successfully')
            return redirect(url_for('viewitems'))
    
           
        return render_template('updateitem.html',count=count)
    
    return redirect(url_for('vendorlogin')) 

             
     



@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
       
        email = request.form['email']
        subject = 'Reset link for vendor application'
        body = f"Reset link for forgot password of vendor: {url_for('fconfirm', token=token(data=email, salt=salt2), _external=True)}"
        sendmail(to=email, subject=subject, body=body)
        flash('Reset link has been sent to the given email, please check.')
        return redirect(url_for('forgot'))
    return render_template('forgot.html')

@app.route('/fconfirm/<token>' ,methods=["GET","POST"]) 
def fconfirm(token):
    try:
        serializer=URLSafeTimedSerializer(secret_key)
        email=serializer.loads(token,salt=salt2,max_age=180) 
    except Exception as e:
        return 'link expired'
    else:    
        if request.method=="POST":
            npassword=request.form['npassword']
            cpassword=request.form['cpassword']
            if npassword==cpassword:
                bytes=npassword.encode('utf-8')
                salt=bcrypt.gensalt()
                hash=bcrypt.hashpw(bytes,salt)
                cursor=mydb.cursor(buffered=True)
                cursor.execute('update vendor set password=%s  where email=%s',[hash,email])
                mydb.commit()
                cursor.close()
                return redirect(url_for('vendorlogin'))
                
            else:
                flash('password mismatch') 
                return render_template('updatepassword.html')   
        return render_template('updatepassword.html')

@app.route('/usersignup',methods=["GET","POST"])
def usersignup():
    if request.method == 'POST':
        
        name = request.form['name']
        
        mobile_no = request.form['mobile_no']
        email = request.form['email']
        address = request.form['address']
        password = request.form['password']
        
        try:
            cursor = mydb.cursor(buffered=True)
            cursor.execute('select count(*) from user where email=%s', [email])
            count = cursor.fetchone()[0]
            if count == 1:
                raise Exception
        except Exception as e:        
            flash("Email already exists")
            return redirect(url_for('usersignup'))
        else:
            otp = genotp() 
            data = { 'name': name, 'mobile_no': mobile_no, 'email': email,'address': address, 'password': password, 'otp': otp}
            subject = 'OTP for user Application' 
            body = f'This is the OTP for Ecom verification: {otp}' 
            sendmail(to=email, subject=subject, body=body)
            otp_token = token(data=data, salt=salt1)
            flash('OTP has been sent to the given Email, please check.')
            return redirect(url_for('otp1', data=otp_token))
    

    return render_template('usersignup.html')

@app.route('/otp1/<data>', methods=['GET','POST']) 
def otp1(data):
    try:
        serializer = URLSafeTimedSerializer(secret_key)
        data= serializer.loads(data, salt=salt1, max_age=360)
    except Exception as e:
        print(e)
        flash("OTP has expired")
        return render_template('otp.html')
    else:
        if request.method == 'POST':
            uotp = request.form['otp']
            if uotp == data['otp']:
                bytes=data['password'].encode('utf-8')
                salt=bcrypt.gensalt()
                hash=bcrypt.hashpw(bytes,salt)
                cursor = mydb.cursor(buffered=True)
                cursor.execute('insert into user (username,mobile_no,email, address, password) values (%s, %s, %s, %s, %s)',
                               (data['name'],  data['mobile_no'],data['email'], data['address'], hash))
                mydb.commit()
                cursor.close()
                flash('Registration has been successfully done')
                
                return redirect(url_for('userlogin'))
            else:
                flash('OTP was incorrect') 
                return redirect(url_for('otp1', data=data))
    return render_template('otp.html')    

@app.route('/userlogin',methods=["GET","POST"])
def userlogin():
    if session.get('user'): 
        return redirect(url_for('abhi'))            
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = mydb.cursor(buffered=True)
        cursor.execute('SELECT password FROM user WHERE email = %s', [email])
        hashed_password = cursor.fetchone()
        if hashed_password:
            hashed_password=hashed_password[0]
            if bcrypt.checkpw(password.encode('utf-8'),bytes(hashed_password)):
                session['user']=email
                if not session.get(email):
                    session[email]={}
                return redirect(url_for('abhi'))
            else:
                flash('password incorrect')
                return redirect(url_for('userlogin')) 
        else:
            flash('email not registered') 
            return redirect(url_for('usersignup')) 
    return render_template('userlogin.html') 

@app.route('/userlogout',methods=["GET","POST"])
def userlogout():
    if session.get('user'):
        session.pop('user')
        return redirect(url_for('abhi'))
    else:
        return redirect(url_for('userlogin'))        

@app.route('/abhi')
def abhi():
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select bin_to_uuid(item_id),item_name,discription,quantity,category,price,addedby,imgid from additem')
    count=cursor.fetchall()
    print(count)
   
    return render_template('web.html',count=count) 

@app.route('/category/<type>') 
def category(type):
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select bin_to_uuid(item_id),item_name,discription,quantity,category,price,addedby,imgid from additem where category=%s',[type])
    count=cursor.fetchall()
    print(count)
    return render_template('category.html',count=count)
    

@app.route('/discription/<item_id>')
def discription(item_id):
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select bin_to_uuid(item_id),(item_name),discription,quantity,category,price,addedby,imgid from additem where item_id=uuid_to_bin(%s)',[item_id])
    count=cursor.fetchone()
    print(count)
    return render_template('discription.html',count=count) 

@app.route('/cart/<item_id>/<item_name>/<discription>/<category>/<price>/<imgid>/<quantity>')
def cart(item_id,item_name,discription,category,price,imgid,quantity):
    if not session.get('user'):
        return redierct(url_for('userlogin')) 
    print(session[session.get('user')])
    if item_id not in session[session.get('user')]:
        session[session.get('user')][(item_id)]=[item_name,discription,category,price,imgid,int(quantity)]
        session.modified=True
        flash(f'{item_name} added to cart successfully')
        return redirect(url_for('abhi'))
    print(type(session[session.get('user')][item_id][5]))
    session[session.get('user')][item_id][5] += 1
    flash(f'{item_name} already added')               
    return redirect(url_for('viewcart'))
    
   

@app.route('/viewcart')
def viewcart():
    if not session.get('user'):
        return redirect(url_for('userlogin'))
    count=session.get(session.get('user')) if session.get(session.get('user')) else 'empty'
    if count=='empty':
        return 'No Products Added'
    print(count)        
   
    return render_template('cart.html',count=count)

@app.route('/removecart/<item_id>')
def removecart(item_id):
    print(item_id)
    if session.get('user'):
        print(session[session.get('user')])
        
        data1=session[session.get('user')].pop(item_id)
        flash(f'{data1[0]} has removed from cart')
        return redirect(url_for('viewcart'))
    return redirect(url_for('userlogin'))

@app.route('/review/<item_id>',methods=["GET","POST"])
def review(item_id):
    if session.get('user'):
        if request.method=='POST':
            content=request.form['content']
            title=request.form['title']
            rating=request.form['rating']
            cursor=mydb.cursor(buffered=True)
            cursor.execute('select username from user where email=%s',[session.get('user')])
            username=cursor.fetchone()[0]
            cursor=mydb.cursor(buffered=True)
            cursor.execute('insert into reviews(email,item_id,review,title,rating)values(%s,uuid_to_bin(%s),%s,%s,%s)',[session.get('user'),item_id,content,title,rating])
            mydb.commit()
            cursor.close()
            flash('review has added successfully')
            return redirect(url_for('discription',item_id=item_id))
        return render_template('review.html')
    else:
        return redirect(url_for('userlogin')) 

@app.route('/read/<item_id>')
def read(item_id):
    if session.get('user'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select * from reviews where item_id=uuid_to_bin(%s)',[item_id])
        allnotes=cursor.fetchall()
        print(allnotes)
        return render_template('table.html',data=allnotes)
    else:
        return redirect(url_for('login'))



@app.route('/view_notes/<nid>')
def view_notes(nid):
    if session.get('user'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select discription from reviews where nid=%s',[nid])
        allnotes=cursor.fetchone()
        print(allnotes)
        return render_template('readreview.html',data1=allnotes) 
    return redirect(url_for('login'))


        
@app.route('/payment/<itemid>/<item_name>/<int:price>/<category>/<imgid>/<dis>',methods=["GET","POST"])
def pay(itemid,item_name,price,category,imgid,dis):
    if session.get('user'):
        user=session.get('user')
        q=int(request.form['quantity']) if request.form['quantity'] else 1
        total=price*1
        checkout_session=stripe.checkout.Session.create(success_url=url_for('success',itemid=itemid,item_name=item_name,q=q,total=total,category=category,imgid=imgid,dis=dis,_external=True),
        line_items=[{
            'price_data':{
                'product_data':{
                    'name':item_name,
                },
                'unit_amount':price*100,
                'currency':'inr',
            },
            'quantity':q,
        }
        ],
        mode="payment",
        )
        return redirect(checkout_session.url)
    else:
        return redirect(url_for('userlogin')) 
@app.route('/success/<itemid>/<item_name>/<q>/<total>/<category>/<imgid>/<dis>') 
def success(itemid,item_name,q,total,category,imgid,dis):
    user=session.get('user') 
    cursor=mydb.cursor(buffered=True)
    cursor.execute(
    'insert into orders (ordid, itemid, item_name, qty, total_price, user, category,imgid, dis) '
    'values (uuid_to_bin(uuid()), uuid_to_bin(%s), %s, %s, %s, %s, %s,%s, %s)',
    [itemid, item_name, q, total, user, category, imgid, dis])

    mydb.commit()

    return redirect(url_for('abhi'))         

@app.route('/orders',methods=["GET","POST"])
def orders():
    if session.get('user'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute("select bin_to_uuid(ordid),bin_to_uuid(itemid),item_name,qty,total_price,user,category,imgid,dis from orders where user=%s",[session.get('user')])
        count=cursor.fetchall()
        return render_template('orders.html',count=count)
        print(count)
    return redirect(url_for('userlogin'))

# @app.route('/getinvoice/<ordid>.pdf') 
# def invoice(ordid):
#     cursor=mydb.cursor(buffered=True)
#     cursor.execute('select username,mobile_no,address, u.email,(ordid),uuid_to_bin(itemid),item_name,qty,total_price,category,bin_to_uuid(imgid),dis from user u join orders o on u.email=o.user where ordid=uuid_to_bin(%s)',[ordid])
#     count=cursor.fetchall()
#     if count:
#         html=render_template('bill.html',count=count)
#         pdf=pdfkit.from_string(html,False,configuration=config)
#         response=Response(pdf,content_type='application/pdf')
#         response.headers['Content-Discription']='inline; filename=output.pdf'
#         return response
#     else:
#         flash('something went wrong') 
#         return redirect(url_for('orders'))                  

@app.route('/getinvoice/<ordid>.pdf')
def invoice(ordid):
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select username,mobile_no,address,u.email,ordid,itemid,item_name,qty,total_price,category,imgid,dis from user u join orders o on u.email=o.user where ordid=uuid_to_bin(%s)',[ordid])
    count=cursor.fetchone()
    if count:
        html=render_template('bill.html',count=count)
        pdf=pdfkit.from_string(html,False,configuration=config)
        response=Response(pdf,content_type='application/pdf')
        response.headers['Content-disposition']='inline; filename=output.pdf'
        return response
    else:
        flash('something went wrong')
        return redirect(url_for('orders'))



app.run(debug=True, use_reloader=True)
