from typing import Optional, List
from pydantic import BaseModel
import datetime

class Item(BaseModel):
    failure_id: str
    headline: str
    description: str
    system_id: int
    client_id: int
    computer_name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    tziah: Optional[str] = None
    molecule: Optional[str] = None
    department: Optional[str] = None
    voip: Optional[str] = None
    red_telephony: Optional[int] = None
    ids: Optional[List] = None
    queue_name: Optional[str] = None
    flow_url: Optional[str] = None
    attachment: Optional[List] = None
    symptom_id: int


class Takala:
    def __init__(self, failure_id, headline, description, system_id, client_id, computer_name, username, password,
                 tziah, molecule, department, voip, red_telephony, ids, queue_name, flow_url, attachment, symptom_id):
        self.failure_id = failure_id
        self.headline = headline
        self.description = description
        self.system_id = system_id
        self.date_created = datetime.datetime.strptime(str(datetime.datetime.now()), "%m/%d/%y  %H:%M:%S")
        self.date_updated = datetime.datetime.strptime(str(datetime.datetime.now()), "%m/%d/%y  %H:%M:%S")
        self.client_id = client_id
        self.computer_name = computer_name
        self.username = username
        self.password = password
        self.tziah = tziah
        self.molecule = molecule
        self.department = department
        self.voip = voip
        self.red_telephony = red_telephony
        self.ids = ids
        self.queue_name = queue_name
        self.flow_url = flow_url
        self.attachment = attachment
        self.symptom_id = symptom_id
        self.status_id = 1 # status_id : 1 = new failure