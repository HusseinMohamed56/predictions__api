from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.routes.predictions_router import predictions_router

app = FastAPI(docs_url=None) 

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(
    predictions_router, 
    prefix='/api/predictions',
    tags=["predictions"],
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your specific needs
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Custom Exception Handling to send user friendly validation error messages
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    erros_details = []

    for error in errors:
        erros_details.append(error['loc'][1] + " " + error['msg'])

    return JSONResponse(
        status_code=400,
        content=jsonable_encoder({"details": erros_details, "message": "Input validation error"}),
    )

# Global exception handler to send user friendly error message for all other exceptions
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Something went wrong, please contact your system admin"},
    )

@app.get("/")
async def hello():
    return {"message": "Hello World"}

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="My API",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",  # Optional
        swagger_css_url="/static/swagger-ui.css",  # Optional
        # swagger_favicon_url="/static/favicon-32x32.png",  # Optional
    )