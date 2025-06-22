from pydantic import BaseModel

class CategoryAgent(BaseModel):
    """Agent that categorizes tickets based on their subject and message."""

    def process(self, ticket: dict) -> str:
        subject = ticket["subject"].lower()
        message = ticket["message"].lower()

        if "error" in subject or "fail" in subject or "broken" in subject:
            return "bug"
        if "feature" in subject:
            return "feature_request"
        if "ui" in subject or "dashboard" in subject:
            return "ui_issue"
        if "security" in subject or "vulnerability" in subject:
            return "security"
        if "rate limit" in subject or "api" in subject:
            return "integration"
        return "other"
