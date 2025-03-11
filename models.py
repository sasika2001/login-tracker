from pydantic import BaseModel
from datetime import datetime

class LoginData(BaseModel):
    user_id: str
    timestamp: datetime
    ip_address: str
