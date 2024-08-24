from typing import Any, List, Optional
import datetime

from pydantic import BaseModel
from houseprice_model.processing.validation import DataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    #predictions: Optional[List[int]]
    predictions: Optional[int]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {'CRIM':[0.023], 
                     'ZN': [7.0],
                     'INDUS':[6.23],
                     'CHAS':[0.0],
                     'NOX':[0.467],
                     'RM':[5.781],
                     'AGE':[45.1],
                     'DIS':[5.69],
                     'RAD':[3],
                     'TAX':[234],
                     'PTRATIO':[12.3],
                     'B':[345.8], 
                     'LSTAT':[3.48]
                    }
                ]
            }
        }
