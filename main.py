#This file(when run) makes flask create a local-server after importing the package '_app_' and 
#getting its app instance. #
from _app_ import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)