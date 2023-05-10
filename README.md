# Event-Driven Architecture with RabbitMQ and Django and Flask
This repository provides a practical guide to building event-driven architectures using RabbitMQ and Python web frameworks like Django and Flask. The content is organized around the following topics:

- Event-Driven Patterns: A review of the main patterns in event-driven architecture, including event sourcing, event notification, and event-driven integration. We also discuss the benefits and challenges of each pattern, and provide examples of how they can be implemented using RabbitMQ and Python web frameworks

- RabbitMQ Configuration: A step-by-step guide to configuring RabbitMQ for event-driven architectures. We cover topics like creating exchanges, defining queues, and setting up bindings between exchanges and queues. We also provide some best practices for naming and organizing exchanges and queues.

- Shared Library of Models: A discussion of the importance of centralizing the models exchanged through the message broker to ensure data consistency. We provide an example of how to create a common-model package in Rabbit Service, which contains all the types exchanged between the producers and consumers of events. We also explain how to version and distribute the package on a central repo.

- Publishing and Consuming Events: A tutorial on how to publish and consume events using RabbitMQ and Python web frameworks. We provide examples of how to publish events from a Django or Flask controller class, and how to consume events using a listener class. We also discuss some best practices for error handling and retrying failed events.


# Requirements

To run the examples in this repository, you will need the following software:

    Python 3.6 or higher
    RabbitMQ 3.7 or higher
    Django 3.1
    Flask 1.1.2

# License

This repository is licensed under the MIT License. See the LICENSE file for details.
