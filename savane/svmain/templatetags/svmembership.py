# Request membership properties
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
import savane.svmain.models as svmain_models

register = template.Library()

@register.filter
def is_nonsuper_admin_of(user, group):
    """
    Return if the user is admin of this group (do not take superuser
    privs in account)

    Example:
    {% if request.user|is_nonsuper_admin_of:group %}
    """
    return svmain_models.Membership.is_nonsuper_admin(user, group)

@register.filter
def is_admin_of(user, group):
    """
    Return if the user is admin of this group

    Example:
    {% if request.user|is_admin_of:group %}
    """
    return svmain_models.Membership.is_admin(user, group)
