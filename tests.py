import os
import pathlib

import pytest

os.chdir(pathlib.Path.cwd() / 'challenges')

pytest.main()
