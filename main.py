import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)


from fastapi import FastAPI
import uvicorn
import models
from database import engine
from routers import jean, user, authentication, preference, review, exception
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi import status, Request


app = FastAPI()

models.Base.metadata.create_all(engine)

app.mount("/static", StaticFiles(directory="app3/static"), name="static")


@app.exception_handler(exception.AuthException)
async def authentication_exception_handler(request: Request, exc: exception.AuthException):
    return RedirectResponse(
        '/auth',
        status_code=status.HTTP_303_SEE_OTHER
    )

app.include_router(authentication.router)
app.include_router(jean.router)
app.include_router(user.router)
app.include_router(preference.router)
app.include_router(review.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True, access_log=False)
