<div align="center">

![sqlalchemylab](./assets/logo.png)

_A scientist in his laboratory is not a mere technician: he is also a child confronting natural phenomena that impress him as though they were fairy tales. - Marie Curie_

</div>

This repo works as a lab for those that want to try queries using SQLAlchemy.

### Built With

- Python 🐍
- SQLAlchemy
- Alembic
- Docker

## Getting Started

To get a local copy up and running follow the **Prerequisites** and **Setup** sections.

### Prerequisites

Make sure you have a properly Python & Poetry environment with version ~3.10.

### Setup

1. Clone the repo

   ```sh
   git clone git@github.com:victormartinez/sqlalchemylab.git
   ```

2. Install the dependencies

   ```sh
   cd sqlalchemylab/
   poetry install
   ```

3. Activate virtual environment

   ```sh
   poetry shell
   ```

4. Run database container
   ```sh
   make db_up
   ```

## Lifecycle

```
1. Update the model at sqlalchemylab/entities/models.py
2. Update the command at sqlalchemylab/command.py
3. Update the query at sqlalchemylab/query.py
4. Create and apply migration

    $ make db_generate_revision
    $ make db_upgrade

5. Execute your command

    $ make command

6. Execute your query

    $ make query

7. Repeat
```

### Help

```sh
make help
```
