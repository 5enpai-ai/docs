#!/usr/bin/env python3
"""Compute the Dante timing grammar from data/videos/*.json.

Only records with verification == "watched" are counted. Re-run whenever
records are added; the output is pasted into 03-grammar-and-recall.md.
Usage: python3 tools/timing_stats.py
"""
import glob
import json
import os
import statistics as st
from collections import Counter

ROOT = os.path.join(os.path.dirname(__file__), "..")
recs = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(ROOT, "data/videos/*.json")))]
recs = [r for r in recs if r["verification"] == "watched"]
n = len(recs)


def rng(xs, fmt="{:.1f}"):
    return f"{fmt.format(min(xs))} / {fmt.format(st.median(xs))} / {fmt.format(max(xs))}"


def beat(r, fn):
    return next((b["t_start"] for b in r["beats"] if b["function"] == fn), None)


print(f"Watched records: {n}\n")
print("| ID | Dur (s) | Shots | Avg shot (s) | Esc. | Pivot | Tag | CTA | Last cut | Tag % | Tag→end (s) |")
print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
rows = []
for r in recs:
    d = r["duration_s"]
    cuts = r["editing"]["cut_times_s"]
    esc, piv, tag, cta = (beat(r, f) for f in ("escalation", "pivot", "tag", "cta"))
    rows.append(dict(d=d, shots=len(cuts) + 1, avg=d / (len(cuts) + 1), esc=esc, piv=piv, tag=tag, cta=cta,
                     last=cuts[-1], tagp=tag / d * 100, tail=d - tag, ctap=cta / d * 100, pivp=piv / d * 100))
    print(f"| {r['id']} | {d:.2f} | {len(cuts)+1} | {d/(len(cuts)+1):.2f} | {'—' if esc is None else esc} | {piv} | {tag} "
          f"| {cta} | {cuts[-1]:.2f} | {tag/d*100:.0f} % | {d-tag:.1f} |")

col = lambda k: [x[k] for x in rows if x[k] is not None]
print("\nmin / median / max")
for label, k, fmt in [("Duration (s)", "d", "{:.1f}"), ("Shots", "shots", "{:.0f}"), ("Avg shot (s)", "avg", "{:.1f}"),
                      ("Escalation start (s)", "esc", "{:.0f}"), ("Pivot start (s)", "piv", "{:.0f}"),
                      ("Pivot start (% runtime)", "pivp", "{:.0f}"), ("Tag start (s)", "tag", "{:.0f}"),
                      ("Tag start (% runtime)", "tagp", "{:.0f}"), ("CTA start (s)", "cta", "{:.0f}"),
                      ("CTA start (% runtime)", "ctap", "{:.0f}"), ("Tag → end of video (s)", "tail", "{:.1f}")]:
    print(f"- {label}: {rng(col(k), fmt)}")
print(f"- Tag → CTA gap (s): {rng([x['cta'] - x['tag'] for x in rows], '{:.0f}')}")
print(f"- Last cut minus CTA start (s): {rng([x['last'] - x['cta'] for x in rows], '{:.1f}')}")
print("\nPivot types:", dict(Counter(r["pivot_type"] for r in recs)))
print("Topic groups:", dict(Counter(r["topic_group"] for r in recs)))
tags = Counter(p["text"] for r in recs for p in r["recurring_phrases"])
print("Tag variants:", dict(tags))
print("CTA variants:", dict(Counter(r["final_line"] for r in recs)))
