from typing import Union
from pydantic import BaseModel

class FolderSchema(BaseModel):
    name: str
    description: Union[str, None] = None