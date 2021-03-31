import os
from app import app

if __name__ == "__main__":
    os.system("pyclean .")
    app.run(threaded=True, port=5000)
    os.system("pyclean .")