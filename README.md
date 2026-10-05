# Week 3 Assignment: Grade Reporter & Bug Hunt

- `grade_reporter.py` - loops through a list of scores, prints each grade (A/B/C/F), and calculates the pass count, fail count, and average.
- `bug_hunt.py` - a fixed while-loop program that correctly sums 1 to 5, with a `# BUG:` comment for each of the three bugs.

The hardest bug to find was the `count < 5` condition, because the program ran without any error and printed 10 instead of 15. I knew something was wrong because I added the numbers up myself and got 15, so the output didn't match the expected answer. Changing the condition to `count <= 5` fixed it.