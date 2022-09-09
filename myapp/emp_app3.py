from first_flask import create_app,db
import os

config_name = os.getenv('FLASK_CONFIG', 'development')
app = create_app(config_name)

if __name__ == "__main__":
    with app.app_context():   ## what is backrount is nothing but context.
        db.create_all()  ## automatically create table or any data.
    app.run(debug=True, port=7000)