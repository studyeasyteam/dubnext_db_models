from typing import Union
from pydantic import BaseModel


class WorkspaceSchema(BaseModel):
    name: str
    description: Union[str, None] = None


