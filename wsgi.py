import os
from app import app

if __name__ == "__main__":
    os.system("pyclean .")
    app.run()
    os.system("pyclean .")