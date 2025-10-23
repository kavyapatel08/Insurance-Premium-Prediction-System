from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120)]
    sex: Annotated[Literal['male', 'female'], Field(...)]
    height: Annotated[float, Field(..., gt=0)]
    weight: Annotated[float, Field(..., gt=0)]
    children: Annotated[int, Field(..., ge=0, le=10)]
    smoker: Annotated[Literal['yes', 'no'], Field(...)]
    region: Annotated[
        Literal['southwest', 'southeast', 'northwest', 'northeast'],
        Field(...)
    ]

    @computed_field(return_type=float)
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
