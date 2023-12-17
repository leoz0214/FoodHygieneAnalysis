"""
Investigating the 3 sub-metrics in detail:
Hygiene, Cleanliness and Management.
The lowest scoring metric is determined and any links
between the scores for each metric are also searched for.

Important Information:
Hygiene: 0 - 25
Cleanliness: 0 - 25
Management: 0 - 30
The lower the score, the better.
"""
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent.parent))
