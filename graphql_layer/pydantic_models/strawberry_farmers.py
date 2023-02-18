from enum import Enum
from pydantic import BaseModel


class FarmerRole(str, Enum):
    quality_manager = "Quality Manager"
    data_analyst = "Data Analyst"
    pest_and_disease_control = "Pest and Disease Control"
    cultivation_expert = "Cultivation Expert"
    customer_support = "Customer Support"
    manpower_scheduler = "Manpower Scheduler"
    grower = "Grower"


class StrawberryFarmer(BaseModel):
    name: str
    age: int
    role: FarmerRole
