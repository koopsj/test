#command to flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from faker import Faker


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'ibm_db_sa://db2inst1:password@localhost:50000/testdb'

# for secure
# app.config['SQLALCHEMY_DATABASE_URI'] = 'ibm_db_sa://enter_user:enter_password@enter_host:50001/BLUDB;SECURITY=SSL;sslCertLocation=path/to/cer_file.cer;sslConnection=true;'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'TEST1'
    __table_args__ = {"schema":"DB2INST1"}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(256))
    email = db.Column(db.String(256))

with app.app_context():
   db.create_all()

@app.route('/')
def index():
    users = User.query
    return render_template('your_template.html', title='Fake Users',
                           users=users)

def create_fake_users(n):
    """Generate fake users."""
    faker = Faker()
    for i in range(n):
        user = User(name=faker.name(),
                    age=random.randint(20, 80),
                    address=faker.address().replace('\n', ', '),
                    phone=faker.phone_number(),
                    email=faker.email())
        db.session.add(user)
    db.session.commit()
    print(f'Added {n} fake users to the database.')
    create_fake_users(10)


{% block content %}
  <table id="data" class="table table-striped">
    <thead>
      <tr>
        <th>Name</th>
        <th>Age</th>
        <th>Address</th>
        <th>Phone Number</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      {% for user in users %}
        <tr>
          <td>{{ user.name }}</td>
          <td>{{ user.age }}</td>
          <td>{{ user.address }}</td>
          <td>{{ user.phone }}</td>
          <td>{{ user.email }}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}
