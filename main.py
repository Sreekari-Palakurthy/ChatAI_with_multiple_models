from fastapi import FastAPI
from app.database import engine
from common import Base as CommonBase
from user import models as user_models
from keys import models as key_models
from thread import models as thread_models
from message import models as message_models
from user.views import router as user_router
from keys.views import router as key_router
from thread.views import router as thread_router
from message.views import router as message_router

user_models.Base.metadata.create_all(bind=engine)
key_models.Base.metadata.create_all(bind=engine)
thread_models.Base.metadata.create_all(bind=engine)
message_models.Base.metadata.create_all(bind=engine)
CommonBase.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(key_router, prefix="/keys", tags=["keys"])
app.include_router(thread_router, prefix="/threads", tags=["threads"])
app.include_router(message_router, prefix="/messages", tags=["messages"])
