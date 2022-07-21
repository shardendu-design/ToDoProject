# from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# import psycopg2


# app = Flask(__name__)


# app.config.update(
    
#     SECRET_KEY = 'Computer1234',
#     SQLALCHEMY_DATABASE_URI= 'postgresql://postgres:Computer1234@localhost/company_details',
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     )

# db = SQLAlchemy(app)


# class Company_Info(db.Model):

#     __tablename__ = 'company_info'

#     id = db.Column(db.Integer, primary_key = True)
#     Company_Name = db.Column(db.String(50), unique=True, nullable=False)
#     Start_Date = db.Column(db.DateTime, default= datetime.utcnow)
#     End_Date = db.Column(db.DateTime, default= datetime.utcnow)
#     Company_Type = db.Column(db.String(50), nullable=False)
#     Company_Address = db.Column(db.String(50), nullable=False)
#     Company_Phone = db.Column(db.String(50), nullable=False)
#     Company_Email_Address = db.Column(db.String(50), nullable=False)
#     Company_Url = db.Column(db.String(50), nullable=False)

#     def __init__(self,Company_Name,Company_Type,Company_Address,Company_Phone,Company_Email_Address,Company_Url):
       
#         self.Company_Name = Company_Name
#         self.Company_Type = Company_Type
#         self.Company_Address =  Company_Address
#         self.Company_Phone = Company_Phone
#         self.Company_Email_Address = Company_Email_Address
#         self.Company_Url = Company_Url



#     def __reper__(self):
#         return f"Company_Info('{self.Company_Name}', '{self.Company_Type}', '{self.Company_Phone}')"




# @app.route('/')

# def home():
#     return render_template('index.html')




# if __name__ == "__main__" :

#     db.create_all()
#     app.run(debug=True)



# <h4>dddddddd</h4>

#         {% for name in company_names %}
#             <h4>Comapny Name: {{ name.Company_Name }}</h4>
#             <p>Start date: {{ name.Start_Date }}</p>
#             <p>End Date: {{ name.End_Date }}</p>
#             <p>Company Type: {{ name.Company_Type }}</p>
#             <p>Company Address: {{ name.Company_Address }}</p>
#             <p>Company_Phone: {{ name.Company_Phone }}</p>
#             <p>Company Email: {{ name.Company_Email_Address }}</p>
#             <p>Company Url: {{ name.Company_Url }}</p>

#         {% endfor %}




{% extends 'layout.html' %}

{% block content %}
<h1 class="company_header">EDIT COMPANY</h1>
<hr>

<div id="company_container" class="container">

    <form method="POST" action="">
        {{ form.hidden_tag() }}
        <!-- {{ form.csrf_token }} -->
        <fieldset class="hm-fieldset" id="hmfieldset">

            <legend class="hm-legend" id="hmlegend">EDIT COMPANY</legend>

            <div class="form-group">
                <label for="company_name">Company Name</label>
                <input type="text" class="form-control" id="company_name"  name="company_name" placeholder="Company Name" required='required'>

                {% for error in form.company_name.errors %}

                <span style="color:red;">
                    {{error}}

                </span>
                {% endfor %}
                
            </div> 
            <div class="form-group">
                <label for="comapny_type">Company Type</label>
                
                <select class="custom-select" name="comapny_type" id="comapny_type"  style="width: 100%" required='required'>
                    <option Open this select menu value=""></option>
                    <option value="Trading">Trading</option>
                    <option value="Retailers">Retailers</option>
                    <option value="Manufacturing">Manufacturing</option>
                </select>

            </div>  
            
            <div class="form-group">
                <label for="company_address">Company Address</label>
                <input type="text" class="form-control" id="company_address" name="company_address" placeholder="Address" required='required'>
                
            </div>
            <div class_for="company_phone">Company Phone</label>
                <input type="tel" class="form-control" id="company_phone" name="company_phone" placeholder="Phone" required='required'>
            </div>
            <div class="form-group">
                <label for="company_email">Company Email</label>
                <input type="email" class="form-control" id="company_email" name="company_email" placeholder="Email" required='required'>
            
            </div>
            <div class="form-group">
                <label for="company_url">Company Url:</label>
                <input type="url" class="form-control" id="company_url" name="company_url" placeholder="Url" required='required'>
                </div>
            <div class="btnoutline" id="btnoutline">
                <button type="submit" class="btn btn-success">Edit</button>
                <!-- <button type="submit" class="btn btn-primary">Edit</button>
                <button type="submit" class="btn btn-danger">Delete</button> -->
                <hr>
    
            </div>


        </fieldset>
        <hr>
                
    </form>   
</div>
<hr>
{% endblock %}







{% extends 'layout.html' %}


{% block content %}
  


<h1 class="company_header">CREATE COMPANY</h1>
<hr>

<div id="company_container" class="container">

    <form method="POST" action="">
    
        <fieldset class="hm-fieldset" id="hmfieldset">

            <legend class="hm-legend" id="hmlegend">COMPANY</legend>

            <div class="form-group">
                <label for="company_name">Company Name</label>
                <input type="text" class="form-control" id="company_name"  name="company_name" placeholder="Company Name" required='required'>

                {% for error in form.company_name.errors %}

                <span style="color:red;">
                    {{error}}

                </span>
                {% endfor %}
                
            </div>
            <div class="form-group">
                <label for="comapny_type">Company Type</label>
                <!-- <input type="text" class="form-control" id="comapny_type" name="comapny_type" placeholder="Company Type" required='required'> -->
                <select class="custom-select" name="comapny_type" id="comapny_type"  style="width: 100%" required='required'>
                    <option Open this select menu value=""></option>
                    <option value="Trading">Trading</option>
                    <option value="Retailers">Retailers</option>
                    <option value="Manufacturing">Manufacturing</option>
                </select>

            </div>  
            
            <div class="form-group">
                <label for="company_address">Company Address</label>
                <input type="text" class="form-control" id="company_address" name="company_address" placeholder="Address" required='required'>
                
            </div>
            <div class="form-group">
                <label for="company_phone">Company Phone</label>
                <input type="tel" class="form-control" id="company_phone" name="company_phone" placeholder="Phone" required='required'>
            </div>
            <div class="form-group">
                <label for="company_email">Company Email</label>
                <input type="email" class="form-control" id="company_email" name="company_email" placeholder="Email" required='required'>
            
            </div>
            <div class="form-group">
                <label for="company_urll">Company Url:</label>
                <input type="url" class="form-control" id="company_url" name="company_url" placeholder="Url" required='required'>
                </div>
            <div class="btnoutline" id="btnoutline">
                <button type="submit" class="btn btn-success">Save</button>
                <!-- <button type="submit" class="btn btn-primary">Edit</button>
                <button type="submit" class="btn btn-danger">Delete</button> -->
                <hr>
    
            </div>


        </fieldset>
        <hr>
                
    </form>   
</div>
<hr>

{% endblock %}


Company.query.order_by('id')


