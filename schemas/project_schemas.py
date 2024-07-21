from typing import Union
from pydantic import BaseModel

class ProjectSchema(BaseModel):
    name: str
    description: Union[str, None] = None