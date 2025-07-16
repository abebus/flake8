"""Module allowing for ``python -m flake8 ...``."""
from __future__ import annotations

from flake8.main.cli import main

if __name__ == "__main__":
    from flake8.plugins.pycodestyle import execution_times
    code = main()
    import statistics
    stats = {k: statistics.mean(v) for k, v in execution_times.items()}
    from pprint import pprint
    pprint(stats)
    raise SystemExit(code)
