from app import create_app
from flask_script import Manager #la clase Manager permite levantar el servidor a partir de una instancia

app = create_app()

if __name__ == '__main__':
    manager = Manager(app)
    manager.run()
