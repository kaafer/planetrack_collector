from pydantic import BaseModel, Field, validator


class TrackValidator(BaseModel):
    ground_speed: int = Field(..., ge=0, lt=1000)

    @validator('ground_speed')
    def convert_from_knots(cls, v):
        return v * 1.852


class PlaneValidator(BaseModel):
    registration: str = Field(..., min_length=3, max_length=10)
    aircraft_code: str = Field(..., min_length=3, max_length=4)
    icao_24bit: str = Field(..., min_length=3, max_length=6)

    class Config:
        schema_extra = {
            'example': {
                'registration': 'RA-73828',
                'aircraft_code': 'A20N',
                'icao_24bit': '151EF1'
            }
        }
