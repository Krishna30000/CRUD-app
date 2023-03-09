from fastapi import Depends, FastAPI
from Authentication.login import get_current_active_user, User
from server_app import app
from fastapi.security.api_key import APIKey

import pickle


balance = 500

@app.post("/spend/",status_code=202)
def spend(spent: float, current_user: User = Depends(get_current_active_user) ):
    global balance
    balance = balance-spent
    response_json={
        
        'balance':balance   }
    return response_json

@app.post("/add/",status_code=202)
def spend(add: float, current_user: User = Depends(get_current_active_user) ):
    global balance
    balance = balance+add
    response_json={
        'balance':balance   
        }
    return response_json

