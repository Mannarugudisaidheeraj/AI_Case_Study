# Architecture
Two-agent architecture:
- CategoryAgent: Determines category based on subject/message.
- RoutingAgent: Determines routing based on category and customer tier.

# Why Multiple Agents
Separates concerns, making it extensible and maintainable.

# Challenges
- Ambiguity between category and route.
- Handling undefined subjects.

# Improvements
Future iterations could use embeddings or classification.
