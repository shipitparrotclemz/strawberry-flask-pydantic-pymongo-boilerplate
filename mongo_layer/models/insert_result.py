from typing import Optional

from pydantic import BaseModel


class InsertResult(BaseModel):
    id: Optional[str]
    success: bool