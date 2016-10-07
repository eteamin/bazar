# -*- coding: utf-8 -*-
"""The application's Globals object"""
import tg
import os
__all__ = ['Globals']


class Globals(object):
    """Container for objects available throughout the life of the application.

    One instance of Globals is created during application initialization and
    is available during requests via the 'app_globals' variable.

    """

    def __init__(self):
        """Do nothing, by default."""
        self.root_dir = os.path.abspath(os.path.join(tg.config['paths']['root'], '..'))
        self._setup_maryjane()

    def _setup_maryjane(self):
        enabled = tg.config.get('maryjane.enabled', 'false')
        if enabled.upper() == 'TRUE':
            from maryjane import main
            manifest_file = os.path.join(self.root_dir, tg.config.get('maryjane.manifest', 'maryjane.yaml'))
            main(manifest_file, enable_watcher=True, bootstrap=False)
