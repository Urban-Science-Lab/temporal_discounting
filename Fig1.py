"""Figure 1 of "Why wait? Optimal rules for intertemporal decisions across life history,
economics and machine learning" (Tannira & Bettencourt).

(A) optimal waiting time for a linearly growing reward; (B) losses with dread.

(A) V(tau,t) = R0 tau exp[-gamma_G (tau - t)], R0 = 1, gamma_G = 0.05, t in {5,15,25};
    tau_* = 1/gamma_G = 20.
(B) Discounted disutility of a constant loss L due at tau, with dread kappa L per unit time:
    -V/L = G_eff(tau) = exp(-gamma_G tau) + (kappa/gamma_G)(1 - exp(-gamma_G tau)).
    kappa = 0 (same as a gain), 0 < kappa < gamma_G (sign effect: levels off at kappa/gamma_G),
    kappa > gamma_G (delay raises disutility: take the loss now).
Usage:  python3 Fig1.py   -> writes waiting-time-and-losses.pdf
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm",
                     "font.serif": ["CMU Serif", "Computer Modern Roman", "DejaVu Serif"],
                     "axes.unicode_minus": False})

gG = 0.05
colors = [plt.cm.viridis(x) for x in (0.2, 0.5, 0.8)]

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"wspace": 0.25})

# (A) linear reward, exponential discounting
for t0, c in zip((5, 15, 25), colors):
    tau = np.linspace(t0, 60, 400)
    a.plot(tau, tau * np.exp(-gG * (tau - t0)), color=c, lw=2, label=rf"$t={t0}$")
    a.plot(t0, t0, "o", color=c, mec="k", ms=7, zorder=3)
    a.annotate(rf"$t={t0}$", (t0, t0), textcoords="offset points", xytext=(-8, 6), ha="right", fontsize=12, color=c)
    if t0 < 1 / gG:
        ts = 1 / gG
        a.plot(ts, ts * np.exp(-gG * (ts - t0)), "s", color=c, mec="k", ms=6, zorder=3)
a.axvline(1 / gG, color="0.4", ls="--", lw=1)
a.text(1 / gG + 0.8, 1.2, r"$\tau_*=1/\gamma_G$", fontsize=12, color="0.3")
a.set_xlim(0, 60); a.set_ylim(0, 28)
a.set_xlabel(r"collection time $\tau$", fontsize=13)
a.set_ylabel(r"discounted value $V(\tau,t)$", fontsize=13)
a.text(0.97, 0.95, "gains", transform=a.transAxes, ha="right", fontsize=12)

# (B) losses with dread
tau = np.linspace(0, 60, 400)
for kappa, c in zip((0.0, 0.025, 0.075), colors):
    Geff = np.exp(-gG * tau) + (kappa / gG) * (1 - np.exp(-gG * tau))
    lab = {0.0: r"$\kappa=0$ (no dread)",
           0.025: r"$\kappa<\gamma_G$: sign effect",
           0.075: r"$\kappa>\gamma_G$: take loss now"}[kappa]
    b.plot(tau, Geff, color=c, lw=2, label=lab)
    if 0 < kappa < gG:
        b.axhline(kappa / gG, color=c, ls=":", lw=1)
b.set_xlim(0, 60); b.set_ylim(0, 2.3)
b.set_xlabel(r"delay of the loss $\tau$", fontsize=13)
b.set_ylabel(r"discounted disutility $-V(\tau)/L$", fontsize=13)
b.text(0.97, 0.95, "losses", transform=b.transAxes, ha="right", fontsize=12)
h, l = b.get_legend_handles_labels()  # reverse so legend order matches curve order (top to bottom)
b.legend(h[::-1], l[::-1], frameon=False, loc="upper right", bbox_to_anchor=(1, 0.91))

for ax, lab in ((a, "A"), (b, "B")):
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(-0.1, 1.04, lab, transform=ax.transAxes, fontsize=20, fontweight="bold")

fig.savefig("waiting-time-and-losses.pdf", bbox_inches="tight")
print("saved waiting-time-and-losses.pdf")
