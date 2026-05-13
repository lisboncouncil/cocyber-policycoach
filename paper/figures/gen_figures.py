#!/usr/bin/env python3
"""Generate figures for the IWAPS 2026 paper.

Output: fig_scatter.pdf in the same directory as this script.
"""

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent

# ---------------------------------------------------------------------------
# Data from Table 2
# ---------------------------------------------------------------------------
configs = [
    {
        "label":   "gpt-4.1",
        "quality": 3.83,
        "privacy": 0,           # SEAL-0, no GDPR
        "cost":    0.02,
        "color":   "#d62728",   # red
        "marker":  "o",
    },
    {
        "label":   "gpt-4.1\n+ web",
        "quality": 3.90,
        "privacy": 0,
        "cost":    0.03,
        "color":   "#d62728",
        "marker":  "s",
    },
    {
        "label":   "gpt-5.5\n+ web",
        "quality": 4.60,
        "privacy": 0,
        "cost":    0.30,        # TBD — estimated
        "color":   "#d62728",
        "marker":  "^",
    },
    {
        "label":   "gpt-4.1\n(Assistants)",
        "quality": 3.70,
        "privacy": 1,           # SEAL-1, partial GDPR
        "cost":    0.07,
        "color":   "#ff7f0e",   # orange
        "marker":  "D",
    },
    {
        "label":   "Kimi K2.5\n(private RAG)",
        "quality": 4.15,
        "privacy": 2,           # SEAL-2, GDPR-compliant
        "cost":    0.05,
        "color":   "#2ca02c",   # green
        "marker":  "P",
    },
]

# Official SEAL level names (EC Cloud Sovereignty Framework, Apr 2026)
SEAL_LABELS = [
    "SEAL-0\nNo Sovereignty",
    "SEAL-1\nJurisdictional\nSovereignty",
    "SEAL-2\nData Sovereignty",
    "SEAL-3\nDigital Resilience",
    "SEAL-4\nFull Digital\nSovereignty",
]

# ---------------------------------------------------------------------------
# Figure: Quality vs Privacy posture (full SEAL-0 to SEAL-4 scale)
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 5.0))

for c in configs:
    ax.scatter(
        c["quality"], c["privacy"],
        s=130, color=c["color"], marker=c["marker"],
        zorder=5, edgecolors="white", linewidths=0.6,
    )
    offsets = {
        "gpt-4.1":                  (-0.01, -0.28),
        "gpt-4.1\n+ web":           (+0.06, +0.12),
        "gpt-5.5\n+ web":           (+0.02, +0.12),
        "gpt-4.1\n(Assistants)":    (-0.01, +0.12),
        "Kimi K2.5\n(private RAG)": (+0.02, +0.12),
    }
    dx, dy = offsets[c["label"]]
    ax.annotate(
        c["label"],
        xy=(c["quality"], c["privacy"]),
        xytext=(c["quality"] + dx, c["privacy"] + dy),
        fontsize=7.5,
        ha="center",
        va="bottom",
        color=c["color"],
    )

# 9% gap annotation
ax.annotate(
    "",
    xy=(4.15, 0.06), xytext=(4.60, 0.06),
    arrowprops=dict(arrowstyle="<->", color="#888888", lw=1.2),
)
ax.text(4.375, 0.14, "9% quality gap", ha="center", va="bottom",
        fontsize=7, color="#555555", style="italic")

# Shaded region: SEAL levels benchmarked in this study
ax.axhspan(-0.45, 2.45, alpha=0.04, color="#2ca02c", zorder=0)
ax.text(4.87, 1.0, "benchmarked\nrange", ha="right", va="center",
        fontsize=6.5, color="#2ca02c", alpha=0.7, style="italic")

# Axes — full SEAL scale
ax.set_xlabel("Average quality score (1–7 scale)", fontsize=9)
ax.set_ylabel("Cloud Sovereignty Level (EC SEAL framework)", fontsize=9)
ax.set_xlim(3.35, 4.95)
ax.set_ylim(-0.55, 4.55)
ax.set_yticks([0, 1, 2, 3, 4])
ax.set_yticklabels(SEAL_LABELS, fontsize=7.5)
ax.xaxis.set_tick_params(labelsize=8)

# Horizontal guide lines
for y in range(5):
    ax.axhline(y, color="#dddddd", lw=0.7, zorder=0)

# Legend
legend_items = [
    mpatches.Patch(color="#d62728", label="Frontier AI (SEAL-0)"),
    mpatches.Patch(color="#ff7f0e", label="Cloud RAG (SEAL-1, partial)"),
    mpatches.Patch(color="#2ca02c", label="Private RAG (SEAL-2)"),
]
ax.legend(handles=legend_items, fontsize=7.5, loc="upper left",
          framealpha=0.9, edgecolor="#cccccc")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig(OUT / "fig_scatter.pdf", bbox_inches="tight")
print("Saved fig_scatter.pdf")
