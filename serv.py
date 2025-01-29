from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Настройка базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель для хранения заявок
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(100), nullable=False)

# Инициализация базы данных
@app.before_first_request
def initialize_database():
    with app.app_context():  # Создание контекста приложения
        db.create_all()

# Эндпоинт для создания заявок
@app.route('/api/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    new_appointment = Appointment(
        name=data['name'],
        phone=data['phone'],
        branch=data['branch'],
        service=data['service']
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment created successfully!'}), 201

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)