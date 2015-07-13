## Humboldt - A codebase to explore and analyze data from the BMV
Humboldt is a codebase that I have designed to provide exploratory features of the data of the Mexican Stock exchange
(BMV - Bolsa Mexicana de Valores).

* `DataManager.py` - The `DataManager` class is the main class for managing the BMV data. It has a basic workflow,
which is the following:
    * Create a `DataManager` instance - with configurations.
    * Call the `getData` method.
    * Call the `massageData` method to change the data form into a more useful one - (i.e. percentage changes).
* `run.py` - This script runs my (Pablo's) main workflow.
