from dagster import Definitions, load_assets_from_modules, load_assets_from_package_module
from .iomanagers import PostgresIOManager
from .assets import extract_cards, extract_decks, extract_locations

defs = Definitions(
    assets=[extract_cards, extract_decks, extract_locations],
    resources={
        "postgres_io_manager_decks": PostgresIOManager(
            "postgresql://myuser:mypassword@localhost:5432/marvel_snap",
            table_name="decks"
            ),
        "postgres_io_manager_cards": PostgresIOManager(
            "postgresql://myuser:mypassword@localhost:5432/marvel_snap",
            table_name="cards"
            ),
        "postgres_io_manager_locations": PostgresIOManager(
            "postgresql://myuser:mypassword@localhost:5432/marvel_snap",
            table_name="locations"
            ),
    },
)