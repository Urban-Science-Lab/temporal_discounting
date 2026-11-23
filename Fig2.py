"""Figure 2 of "Why wait? Optimal rules for intertemporal decisions across life history,
economics and machine learning" (Tannira & Bettencourt): optimal retirement age.

Usage:  python3 Fig2.py   -> writes s-shaped-rewards-realistic.pdf

Wages: R(tau) = R_max * exp(-exp(-omega (tau - tau_w)))  -> gamma_R = omega exp(-omega (tau - tau_w))
Discount rate: Gompertz--Makeham mortality, mu(tau) = mu0 + alpha exp(beta tau)
Optimal retirement age tau_*: gamma_R(tau_*) = mu(tau_*).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import brentq

plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm",
                     "font.serif": ["CMU Serif", "Computer Modern Roman", "DejaVu Serif"]})

omega = 0.08
mu0, alpha, beta = 5e-4, 2e-5, 0.09
groups = [("No diploma", 29.73, 1.00), ("High school", 30.73, 1.26),
          ("Bachelor\u2019s", 34.73, 2.09), ("Advanced degree", 38.73, 2.57)]
colors = [plt.cm.viridis(x) for x in (0.2, 0.4, 0.6, 0.85)]

R = lambda t, tw, Rm: Rm * np.exp(-np.exp(-omega * (t - tw)))
gR = lambda t, tw: omega * np.exp(-omega * (t - tw))
mu = lambda t: mu0 + alpha * np.exp(beta * t)
tstar = [brentq(lambda t: gR(t, tw) - mu(t), tw, 120) for _, tw, _ in groups]

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"wspace": 0.25})
t = np.linspace(0, 80, 800)
for (name, tw, Rm), c, ts in zip(groups, colors, tstar):
    a.plot(t, R(t, tw, Rm), color=c, lw=2, label=name)
    a.plot(ts, R(ts, tw, Rm), "o", color=c, mec="k", ms=7, zorder=3)
a.set_xlim(0, 80); a.set_xlabel(r"age $\tau$", fontsize=13); a.set_ylabel(r"reward $R(\tau)$", fontsize=13)
a.legend(frameon=False, loc="upper left")

x = np.arange(len(groups))
for xi, c, ts in zip(x, colors, tstar):
    b.plot(xi, ts, "o", color=c, mec="k", ms=11)
    b.annotate(f"{ts:.1f}", (xi, ts), textcoords="offset points", xytext=(0, 12), ha="center")
b.set_xticks(x); b.set_xticklabels([g[0].replace(" ", "\n") for g in groups], fontsize=11)
b.set_xlim(-0.5, len(groups) - 0.5); b.set_ylim(60, 69)
b.set_ylabel(r"optimal retirement age $\tau_*$", fontsize=13)

for ax, lab in ((a, "A"), (b, "B")):
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(-0.1, 1.04, lab, transform=ax.transAxes, fontsize=20, fontweight="bold")

fig.savefig("s-shaped-rewards-realistic.pdf", bbox_inches="tight")
print("tau_* =", [round(x, 1) for x in tstar])
