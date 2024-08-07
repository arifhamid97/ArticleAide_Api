from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.models import Query
from src.core import Model

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    error_messages = " | ".join(error.get("msg") for error in exc.errors())
    return JSONResponse(
        status_code=422,
        content={"detail": error_messages},
    )


@app.post("/generate/")
async def generate_text(query: Query):

    try:
        context = query.context
        model = Model()
        result = model.invoke_chain(context=context, flavour=query.prompt_flavour)
        return {"generated_text": result["explaination"]}
    except Exception as e:
        raise HTTPException(status_code=500, details=str(e))


# A simple root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the OpenAI text generation API"}
