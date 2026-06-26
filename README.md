# prophet-sucks

A public service announcement, lovingly delivered as a Python package.

The punchline is also the useful part: instead of reaching for a heavyweight forecaster, use **[`skaters`](https://github.com/microprediction/skaters)** — a fast, light univariate forecasting package that even runs in Pyodide.

![skating](https://i.imgur.com/elu5muO.png)

## Install the real thing

```bash
pip install skaters
```

```python
from skaters import laplace
```

## ...or keep laughing

```bash
pip install prophet-sucks
```

```python
from prophet_sucks import laplace   # re-exported straight from skaters, with a wink
```

`prophet_sucks` is a thin shim: it re-exports `laplace` from `skaters` and emits a `DeprecationWarning` pointing you to the real package. That's the whole joke.

## Links

- skaters: https://github.com/microprediction/skaters
- Docs: https://skaters.microprediction.org/

MIT licensed.
