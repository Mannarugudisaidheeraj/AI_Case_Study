from pydantic import BaseModel

class RoutingAgent(BaseModel):
    """Agent that routes tickets to the right team based on category and customer tier."""

    def process(self, ticket: dict, category: str) -> str:
        tier = ticket["customer_tier"]

        if category == "security":
            return "security_team"

        if category == "bug":
            return "backend_team"

        if category in ["feature_request", "integration"]:
            return "product_management"

        if category == "ui_issue":
            return "frontend_team"

        # Premium and enterprise tickets go to dedicated team
        if tier in ["premium", "enterprise"]:
            return "priority_support"

        return "general_support"
