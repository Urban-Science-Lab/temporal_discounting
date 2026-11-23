# Why wait? Optimal rules for intertemporal decisions

Code to reproduce the figures in

> E. Tannira and L. M. A. Bettencourt, *Why wait? Optimal rules for intertemporal decisions across life history, economics and machine learning*.

| Script | Figure | Output |
|---|---|---|
| `Fig1.py` | Figure 1: (A) optimal waiting time for a linearly growing reward under exponential discounting; (B) discounted disutility of losses with dread (sign effect) | `waiting-time-and-losses.pdf` |
| `Fig2.py` | Figure 2: optimal retirement age from S-shaped (Gompertz) wage streams and Gompertz–Makeham mortality | `s-shaped-rewards-realistic.pdf` |

## Usage

```bash
pip install -r requirements.txt
python3 Fig1.py
python3 Fig2.py
```

Each script writes its PDF to the current directory. Parameter values are listed in each script's docstring and in the figure captions of the paper.

## License

MIT License; see [LICENSE](LICENSE).
