def evaluate(results, expected=None):
    """Evaluate results. Will compare against `expected` if available."""
    for ticket_id, category, route in results:
        print(f"Ticket: {ticket_id} -> Category: {category}, Route: {route}")

    # Placeholder for future metrics like accuracy, agreement, etc.
    # Currently just prints results
    print("\nEvaluation Complete.")
