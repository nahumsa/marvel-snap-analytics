from dagster import Definitions, load_assets_from_modules, load_assets_from_package_module
from .iomanagers import PostgresIOManager
from .assets import extract_cards, extract_decks

defs_cards = Definitions(
    assets=[extract_cards],
    resources={
        "postgres_io_manager": PostgresIOManager("postgresql://myuser:mypassword@localhost:5432/marvel_snap", "cards")
    },
)

defs = Definitions(
    assets=[extract_decks],
    resources={
        "postgres_io_manager": PostgresIOManager("postgresql://myuser:mypassword@localhost:5432/marvel_snap", "decks")
    },
)