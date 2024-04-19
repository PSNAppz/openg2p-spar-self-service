# ruff: noqa: E402

import asyncio

from .config import Settings

_config = Settings.get_config()

from openg2p_fastapi_common.app import Initializer as BaseInitializer

from .controllers.dfsp_controller import DfspController
from .models import DfspLevel


class Initializer(BaseInitializer):
    def initialize(self, **kwargs):
        super().initialize(**kwargs)
        DfspController().post_init()

    def migrate_database(self, args):
        super().migrate_database(args)

        async def migrate():
            await DfspLevel.create_migrate()

        asyncio.run(migrate())
