from pydantic import BaseModel
from pydantic import Field

class ColorShema(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str

class GeoShema(BaseModel):
    lat: str
    lng: str


class AddressShema(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: GeoShema


class CompanyShema(BaseModel):
    name: str
    catch_phrase: str = Field(alias="catchPhrase")
    bs: str


class UserSchema(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: AddressShema
    phone: str
    website: str
    company: CompanyShema
