import os

def rename_(idx, name):
  new_idx = '{:02d}'.format(idx)
  os.rename(name, f"{new_idx}.jpg")

[rename_(i + 1, j) for (i, j) in enumerate(os.listdir()) if not j.endswith('.py')]
