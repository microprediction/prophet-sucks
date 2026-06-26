"""
prophet-sucks is a public service announcement, lovingly delivered as a Python package.

The punchline is also the useful part: stop reaching for heavyweight forecasters and
use `skaters` (https://github.com/microprediction/skaters) instead — a fast, light
univariate forecasting package that even runs in Pyodide.

This package is a thin shim. It re-exports `laplace` from `skaters` so that
`from prophet_sucks import laplace` works, and emits a DeprecationWarning nudging
you toward the real thing:

    pip install skaters
    from skaters import laplace
"""
import warnings

warnings.warn(
    "prophet-sucks is a joke package. The serious recommendation is `skaters` "
    "(pip install skaters; https://github.com/microprediction/skaters). "
    "prophet_sucks only re-exports `laplace` from skaters. "
    "Please import `from skaters import laplace` instead.",
    DeprecationWarning,
    stacklevel=2,
)

from skaters import laplace

__all__ = ["laplace"]
