# Shorten range for pagination
# Copyright (C) 2010  Sylvain Beucler
#
# This file is part of Savane.
# 
# Savane is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# Savane is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django import template

register = template.Library()

@register.filter
def short_range(page_range, cur_page):
    """
    Shorten a pagination range:
    1 2 3 4 5 [6] 7 8 9 10 11
    -> 1 2 '...' 5 [6] 7 '...' 10 11
    """

    ADJACENT = 4
    FAR = 2

    short_page_range = []
    orig_last = page_range[-1]

    middle = cur_page
    if middle - ADJACENT < 1:
        middle = 1 + ADJACENT
    if middle + ADJACENT > orig_last:
        middle = orig_last - ADJACENT

    middle_start = max(middle - ADJACENT, 1)
    middle_end = min(middle + ADJACENT, orig_last)

    short_page_range = range(middle_start, middle_end+1)

    if middle_start > 1:
        if middle_start <= 1+FAR:
            short_page_range = range(1, middle_start) + short_page_range
        elif middle_start <= 1+FAR+(2*ADJACENT+1):
            short_page_range = range(1, FAR+1) + ['...'] + short_page_range
        else:
            # dichotomy if you can fit more than the display range in the '...'
            short_page_range = range(1, FAR+1) + ['...'] \
                + [1+FAR + ((middle_start-1) - FAR) / 2] + ['...'] + short_page_range

    if middle_end < orig_last:
        if middle_end >= orig_last-FAR:
            short_page_range = short_page_range + range(middle_end+1, orig_last+1)
        elif middle_end >= orig_last-FAR-(2*ADJACENT+1):
            short_page_range = short_page_range + ['...'] + range(orig_last-FAR+1, orig_last+1)
        else:
            # dichotomy if you can fit more than the display range in the '...'
            short_page_range = short_page_range + ['...'] \
                + [orig_last-FAR - ((orig_last-FAR) - middle_end) / 2] + ['...'] + range(orig_last-FAR+1, orig_last+1)

    return short_page_range
