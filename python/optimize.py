import cProfile
import re
from pympler import tracker
tr = tracker.SummaryTracker()
cProfile.run('re.compile("foo|bar")', 'restats')

tr.print_diff()