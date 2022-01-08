from more_itertools import ichunked
import logging
from utils import ManagementLogging

ml = ManagementLogging()

from search_app.models import RedditAdvert
from django.core.management.base import BaseCommand
from ...meilisearch_utils import clear_meilisearch, initialise_meilisearch, meili_client

logger = ml.getLogger()

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--clear-meili', action="store_true")
        parser.add_argument('--populate-from-db', action="store_true")
        parser.add_argument('--update-indices', action="store_true")

    def handle(
            self,
            clear_meili,
            populate_from_db,
            update_indices,
            verbosity,
            *args, **kwargs
    ):
        batch_size = 10000
        ml.set_level_from_verbosity(verbosity)
        if clear_meili:
            clear_meilisearch()

        if update_indices:
            initialise_meilisearch()

        if populate_from_db:
            initialise_meilisearch()
            adverts = RedditAdvert.objects.all()
            logger.info("Found %s adverts in db", len(adverts))
            ichunks = ichunked(adverts, batch_size)
            for i, ichunk in enumerate(ichunks):
                logger.info(f"Fetching {batch_size} ads from db...")
                to_update = [
                    add_meili for add_meili in
                    (ad.serialize_meilisearch() for ad in ichunk)
                    if add_meili is not None
                ]
                logger.info(f"Inserting {len(to_update)} ads in meilisearch.")
                if len(to_update) > 0:
                    meili_client.index("Adverts").add_documents(to_update)
            logger.info("Adverts fed to meilisearch")
