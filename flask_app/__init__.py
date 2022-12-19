from flask import Flask
import logging

app=Flask(__name__)
logging.basicConfig(filename='error.log',level=logging.ERROR)