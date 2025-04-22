from pydantic import BaseModel

class EmailStats(BaseModel):
    raw_emails: int
    acknowledged: int
    pending_human_review: int = 0