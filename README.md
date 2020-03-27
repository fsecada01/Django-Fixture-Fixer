# MongoFixtureFixer

This is a non-functioning prototype of a fixture application for Django. This was created as a step nest specific payloads from MongoDB into fixture-compliant payloads. While ultimately not successful, it may provide a stepping stone for a different developer.  

## Program Design
* The Core file is comprised of a singular class object that generates the JSON payload from the string-representation of a JSON backup file. 
    - The defined functions converts the name of the models to be Django-compliant, dumps the assigned JSON payload to a sanitized file, and converts the JSON to csv-compliant data (and saves the file).
*  Data-Transforming functions changes the assigned JSON to be compliant with Django Fixtures. 

## Considerations
* Code should be rebased to move data-transforming functions to the core programming file and to assign them within the class object via assigned functions.
* Evaluate how Django utilizes ORM to process fixtures
* Evaluate Djongo and psycopg2 integrations with Django's backend, and evaluate how mongo is converted to compliant SQL.
