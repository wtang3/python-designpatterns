# Design Patterns in Python

This repo was designed for learning purposes, feedback welcomed.

### Strategy Pattern ###

One major problem in OOD is the Open-Closed Principle (OCP) in SOLID, this pattern allows
you to add additional implementation without breaking existing logic.

### Observer Pattern ###

Also known as pub-sub pattern or dependents pattern. When the state of one changes its dependents are notified.
A one to many relationship.

                |------ Observer
    Subject --- |------ Observer
                |------ Observer

### Facade Pattern ###

Also known as the structural pattern, used to provide a simplified interface or a class library. It defines
a higher-level interface that allows a subsystem easier to use.

Example SOA a webservice calling a number of smaller services.


### Resources ###
- https://en.wikipedia.org/wiki/Strategy_pattern
- https://en.wikipedia.org/wiki/Observer_pattern
- https://en.wikipedia.org/wiki/Facade_pattern
