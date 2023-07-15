from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_success_request():
    response = client.get("/api/predictions/predict_value?x0=4.78547356727874&x1=-0.531572670933376&x2=-0.0563991808403612")
    assert response.status_code == 200

def test_bad_request_missing_input_x2():
    response = client.get("/api/predictions/predict_value?x0=4.78547356727874&x1=-0.531572670933376")
    assert response.status_code == 400
    assert response.json() == {"details": ["x2 Field required"], "message": "Input validation error"}

def test_bad_request_missing_input_x0():
    response = client.get("/api/predictions/predict_value?x2=4.78547356727874&x1=-0.531572670933376")
    assert response.status_code == 400
    assert response.json() == {"details": ["x0 Field required"], "message": "Input validation error"}

def test_bad_request_invalid_input():
    response = client.get("/api/predictions/predict_value?x0=4.78547356727874&x1=-0.531572670933376&x2=-0.0563991808403612*")
    assert response.status_code == 400
    assert response.json() == {"details": ["x2 Input should be a valid number, unable to parse string as a number"],
    "message": "Input validation error"}

def test_bad_request_invalid_input1():
    response = client.get("/api/predictions/predict_value?x0=4.78547356727874&x1=-0.531572670933376&x2=")
    assert response.status_code == 400
    assert response.json() == {"details": ["x2 Input should be a valid number, unable to parse string as a number"],
    "message": "Input validation error"}

def test_bad_request_invalid_input2():
    response = client.get("/api/predictions/predict_value?x0=4.78547356727874&x1=&x2=-0.0563991808403612")
    assert response.status_code == 400
    assert response.json() == {"details": ["x1 Input should be a valid number, unable to parse string as a number"],
    "message": "Input validation error"}

def test_bad_request_invalid_and_missing_input():
    response = client.get("/api/predictions/predict_value?x0=4.78547356727874&x1=-0.531572670933376*")
    assert response.status_code == 400
    assert response.json() == {"details": [
        "x1 Input should be a valid number, unable to parse string as a number",
        "x2 Field required"
    ],
    "message": "Input validation error"}

def test_bad_request_invalid_and_missing_input2():
    response = client.get("/api/predictions/predict_value?x1=-0.531572670933376*&x2=-0.0563991808403612")
    assert response.status_code == 400
    assert response.json() == {"details": [
        "x0 Field required",
        "x1 Input should be a valid number, unable to parse string as a number"
    ],
    "message": "Input validation error"}