from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

COSMOS_URL = os.getenv("COSMOS_URL")
COSMOS_KEY = os.getenv("COSMOS_KEY")

FILMS_PATH = Path(__file__).parent / "films.json"
DB_ID = "FilmReviewDB"
CONTAINER_ID = "Films"
# partition documents on year e.g. 2020, 2021
PARTITION_KEY = "/year"