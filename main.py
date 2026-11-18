#!/usr/bin/env python3
"""Deterministic news summary image writer for make.fun news-image-20261117.
Copies the pre-built summary image of 17 Nov 2026 world news to /output/entry.png.
No network. Same bytes every run.
"""
import os, shutil, sys
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out_dir = "/output"
os.makedirs(out_dir, exist_ok=True)
dst = os.path.join(out_dir, "entry.png")
shutil.copy2(src, dst)
print(f"Wrote {dst}", file=sys.stderr)
