from agents.category_agent import CategoryAgent
from agents.routing_agent import RoutingAgent
from data.test_cases import test_cases

def main():
    category_agent = CategoryAgent()
    routing_agent = RoutingAgent()

    results = []

    for ticket in test_cases:
        category = category_agent.process(ticket)
        route = routing_agent.process(ticket, category)
        results.append((ticket["ticket_id"], category, route))

    # Print results
    print("Ticket ID | Predicted Category | Predicted Route")
    for ticket_id, category, route in results:
        print(f"{ticket_id} | {category} | {route}")

    # Append results to ai_chat_history.txt
    with open("ai_chat_history.txt", "a", encoding="utf-8") as f:
        f.write("Ticket ID | Predicted Category | Predicted Route\n")
        for ticket_id, category, route in results:
            f.write(f"{ticket_id} | {category} | {route}\n")
        f.write("\n")

if __name__ == "__main__":
    main()
