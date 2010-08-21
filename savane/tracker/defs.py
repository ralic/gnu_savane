# Trackers definition
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

from django.utils.translation import ugettext, ugettext_lazy as _

common = {
    'bug_id' : {
        'field_name': 'bug_id',
        'display_type': 'TF',
        'display_size': '6/10',
        'label': _("Item ID"),
        'description': _("Unique item identifier"),
        'scope': 'S',
        'required': 1,
        'empty_ok': 0,
        'keep_history': 0,
        'special': 1,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 10,
        'transition_default_auth': 'A',
    },
    'group_id' : {
        'field_name': 'group_id',
        'display_type': 'TF',
        'display_size': '',
        'label': _("Group ID"),
        'description': _("Unique project identifier"),
        'scope': 'S',
        'required': 1,
        'empty_ok': 0,
        'keep_history': 0,
        'special': 1,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 1,
        'show_on_add_members': 1,
        'place': 30,
        'transition_default_auth': 'A',
    },
    'submitted_by' : {
        'field_name': 'submitted_by',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Submitted by"),
        'description': _("User who originally submitted the item"),
        'scope': 'S',
        'required': 1,
        'empty_ok': 1,
        'keep_history': 0,
        'special': 1,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 20,
        'transition_default_auth': 'A',
    },
    'date' : {
        'field_name': 'date',
        'display_type': 'DF',
        'display_size': '10/15',
        'label': _("Submitted on"),
        'description': _("Date and time of the initial submission"),
        'scope': 'S',
        'required': 1,
        'empty_ok': 0,
        'keep_history': 0,
        'special': 1,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 40,
        'transition_default_auth': 'A',
    },
    'close_date' : {
        'field_name': 'close_date',
        'display_type': 'DF',
        'display_size': '10/15',
        'label': _("Closed on"),
        'description': _("Date and time when the item  status was changed to 'Closed'"),
        'scope': 'S',
        'required': 1,
        'empty_ok': 1,
        'keep_history': 0,
        'special': 1,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 50,
        'transition_default_auth': 'A',
    },
    'status_id' : {
        'field_name': 'status_id',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Open/Closed"),
        'description': _("Most basic status"),
        'scope': 'S',
        'required': 1,
        'empty_ok': 0,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 600,
        'transition_default_auth': 'A',
    },
    'severity' : {
        'field_name': 'severity',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Severity"),
        'description': _("Impact of the item on the system (Critical, Major,...)"),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 1,
        'show_on_add_members': 1,
        'place': 200,
        'transition_default_auth': 'A',
    },
    'category_id' : {
        'field_name': 'category_id',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Category"),
        'description': _("Generally high level modules or functionalities of the software (e.g. User interface, Configuration Manager, etc)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 1,
        'show_on_add_members': 1,
        'place': 100,
        'transition_default_auth': 'A',
    },
    'assigned_to' : {
        'field_name': 'assigned_to',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Assigned to"),
        'description': _("Who is in charge of handling this item"),
        'scope': 'S',
        'required': 1,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 0,
        'show_on_add_members': 1,
        'place': 500,
        'transition_default_auth': 'A',
    },
    'summary' : {
        'field_name': 'summary',
        'display_type': 'TF',
        'display_size': '65/120',
        'label': _("Summary"),
        'description': _("One line description of the item"),
        'scope': 'S',
        'required': 1,
        'empty_ok': 0,
        'keep_history': 1,
        'special': 1,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 1,
        'show_on_add_members': 1,
        'place': 700000,
        'transition_default_auth': 'A',
    },
    'details' : {
        'field_name': 'details',
        'display_type': 'TA',
        'display_size': '65/20',
        'label': _("Original Submission"),
        'description': _("Full description of the item"),
        'scope': 'S',
        'required': 1,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 1,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 1,
        'show_on_add_members': 1,
        'place': 700001,
        'transition_default_auth': 'A',
    },
    'bug_group_id' : {
        'field_name': 'bug_group_id',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Item Group"),
        'description': _("Characterizes the nature of the item (e.g. Crash Error, Documentation Typo, Installation Problem, etc"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 1,
        'show_on_add_members': 1,
        'place': 300,
        'transition_default_auth': 'A',
    },
    'resolution_id' : {
        'field_name': 'resolution_id',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Status"),
        'description': _("Current resolution of the item"),
        'scope': 'P',
        'required': 1,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 0,
        'show_on_add_members': 1,
        'place': 400,
        'transition_default_auth': 'A',
    },
    'privacy' : {
        'field_name': 'privacy',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Privacy"),
        'description': _("Determines whether the item can be seen by members of the project only or anybody."),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 1,
        'show_on_add_members': 1,
        'place': 402,
        'transition_default_auth': 'A',
    },
    'vote' : {
        'field_name': 'vote',
        'display_type': 'TF',
        'display_size': '6/10',
        'label': _("Votes"),
        'description': _("How many votes this item received."),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 0,
        'special': 1,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 405,
        'transition_default_auth': 'A',
    },
    'category_version_id' : {
        'field_name': 'category_version_id',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Component Version"),
        'description': _("Version of the System Component (aka Item Category) impacted by the item"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 1000,
        'transition_default_auth': 'A',
    },
    'platform_version_id' : {
        'field_name': 'platform_version_id',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Operating System"),
        'description': _("Operating System impacted by the issue"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 1100,
        'transition_default_auth': 'A',
    },
    'reproducibility_id' : {
        'field_name': 'reproducibility_id',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Reproducibility"),
        'description': _("How easy it is to reproduce the item"),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 1200,
        'transition_default_auth': 'A',
    },
    'size_id' : {
        'field_name': 'size_id',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Size (loc)"),
        'description': _("Estimated size of the code to be developed or reworked to fix the item"),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 1300,
        'transition_default_auth': 'A',
    },
    'fix_release_id' : {
        'field_name': 'fix_release_id',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Fixed Release"),
        'description': _("Release in which the item was actually fixed"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 1400,
        'transition_default_auth': 'A',
    },
    'comment_type_id' : {
        'field_name': 'comment_type_id',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Comment Type"),
        'description': _("Specify the nature of the follow up comment attached to this item"),
        'scope': 'P',
        'required': 1,
        'empty_ok': 1,
        'keep_history': 0,
        'special': 1,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 1500,
        'transition_default_auth': 'A',
    },
    'hours' : {
        'field_name': 'hours',
        'display_type': 'TF',
        'display_size': '5/5',
        'label': _("Effort"),
        'description': _("Number of hours of work needed to fix the item"),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 1700,
        'transition_default_auth': 'A',
    },
    'plan_release_id' : {
        'field_name': 'plan_release_id',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Planned Release"),
        'description': _("Release in which it is planned to have the item fixed"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 1600,
        'transition_default_auth': 'A',
    },
    'component_version' : {
        'field_name': 'component_version',
        'display_type': 'TF',
        'display_size': '10/40',
        'label': _("Component Version"),
        'description': _("Version of the system component (or work product) impacted by the item (<u>in free text</u>)"),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 1800,
        'transition_default_auth': 'A',
    },
    'fix_release' : {
        'field_name': 'fix_release',
        'display_type': 'TF',
        'display_size': '10/40',
        'label': _("Fixed Release"),
        'description': _("Release in which the bug was actually fixed (<u>in free text</u>)"),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 1900,
        'transition_default_auth': 'A',
    },
    'plan_release' : {
        'field_name': 'plan_release',
        'display_type': 'TF',
        'display_size': '10/40',
        'label': _("Planned Release"),
        'description': _("Release in which it is planned to have the item fixed (<u>in free text</u>)"),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 2000,
        'transition_default_auth': 'A',
    },
    'priority' : {
        'field_name': 'priority',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Priority"),
        'description': _("How quickly the item should be handled"),
        'scope': 'S',
        'required': 1,
        'empty_ok': 0,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 0,
        'show_on_add_members': 1,
        'place': 200,
        'transition_default_auth': 'A',
    },
    'keywords' : {
        'field_name': 'keywords',
        'display_type': 'TF',
        'display_size': '60/120',
        'label': _("Keywords"),
        'description': _("List of comma separated keywords associated with this item"),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 3000,
        'transition_default_auth': 'A',
    },
    'release_id' : {
        'field_name': 'release_id',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Release"),
        'description': _("Release (global version number) impacted by the item"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 800,
        'transition_default_auth': 'A',
    },
    'release' : {
        'field_name': 'release',
        'display_type': 'TF',
        'display_size': '10/40',
        'label': _("Release"),
        'description': _("Release (global version number) impacted by the item (<u>in free text</u>)"),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 800,
        'transition_default_auth': 'A',
    },
    'originator_name' : {
        'field_name': 'originator_name',
        'display_type': 'TF',
        'display_size': '20/40',
        'label': _("Originator Name"),
        'description': _("Name of the person who submitted the item (if different from the submitter field)"),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 550,
        'transition_default_auth': 'A',
    },
    'originator_email' : {
        'field_name': 'originator_email',
        'display_type': 'TF',
        'display_size': '20/40',
        'label': _("Originator Email"),
        'description': _("Email address of the person who submitted the item (if different from the submitter field, add address to CC list)"),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 2,
        'show_on_add_members': 0,
        'place': 560,
        'transition_default_auth': 'A',
    },
    'originator_phone' : {
        'field_name': 'originator_phone',
        'display_type': 'TF',
        'display_size': '10/40',
        'label': _("Originator Phone"),
        'description': _("Phone number of the person who submitted the item"),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 570,
        'transition_default_auth': 'A',
    },
    'percent_complete' : {
        'field_name': 'percent_complete',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Percent Complete"),
        'description': _(""),
        'scope': 'S',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 500,
        'transition_default_auth': 'A',
    },
    'custom_tf1' : {
        'field_name': 'custom_tf1',
        'display_type': 'TF',
        'display_size': '10/15',
        'label': _("Custom Text Field #1"),
        'description': _("Customizable Text Field (one line, up to 255 characters"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 30000,
        'transition_default_auth': 'A',
    },
    'custom_tf2' : {
        'field_name': 'custom_tf2',
        'display_type': 'TF',
        'display_size': '10/15',
        'label': _("Custom Text Field #2"),
        'description': _("Customizable Text Field (one line, up to 255 characters"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 30100,
        'transition_default_auth': 'A',
    },
    'custom_tf3' : {
        'field_name': 'custom_tf3',
        'display_type': 'TF',
        'display_size': '10/15',
        'label': _("Custom Text Field #3"),
        'description': _("Customizable Text Field (one line, up to 255 characters"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 30200,
        'transition_default_auth': 'A',
    },
    'custom_tf4' : {
        'field_name': 'custom_tf4',
        'display_type': 'TF',
        'display_size': '10/15',
        'label': _("Custom Text Field #4"),
        'description': _("Customizable Text Field (one line, up to 255 characters"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 30300,
        'transition_default_auth': 'A',
    },
    'custom_tf5' : {
        'field_name': 'custom_tf5',
        'display_type': 'TF',
        'display_size': '10/15',
        'label': _("Custom Text Field #5"),
        'description': _("Customizable Text Field (one line, up to 255 characters"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 30400,
        'transition_default_auth': 'A',
    },
    'custom_tf6' : {
        'field_name': 'custom_tf6',
        'display_type': 'TF',
        'display_size': '10/15',
        'label': _("Custom Text Field #6"),
        'description': _("Customizable Text Field (one line, up to 255 characters"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 30500,
        'transition_default_auth': 'A',
    },
    'custom_tf7' : {
        'field_name': 'custom_tf7',
        'display_type': 'TF',
        'display_size': '10/15',
        'label': _("Custom Text Field #7"),
        'description': _("Customizable Text Field (one line, up to 255 characters"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 30600,
        'transition_default_auth': 'A',
    },
    'custom_tf8' : {
        'field_name': 'custom_tf8',
        'display_type': 'TF',
        'display_size': '10/15',
        'label': _("Custom Text Field #8"),
        'description': _("Customizable Text Field (one line, up to 255 characters"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 30700,
        'transition_default_auth': 'A',
    },
    'custom_tf9' : {
        'field_name': 'custom_tf9',
        'display_type': 'TF',
        'display_size': '10/15',
        'label': _("Custom Text Field #9"),
        'description': _("Customizable Text Field (one line, up to 255 characters"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 30800,
        'transition_default_auth': 'A',
    },
    'custom_tf10' : {
        'field_name': 'custom_tf10',
        'display_type': 'TF',
        'display_size': '10/15',
        'label': _("Custom Text Field #10"),
        'description': _("Customizable Text Field (one line, up to 255 characters"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 30900,
        'transition_default_auth': 'A',
    },
    'custom_ta1' : {
        'field_name': 'custom_ta1',
        'display_type': 'TA',
        'display_size': '60/3',
        'label': _("Custom Text Area #1"),
        'description': _("Customizable Text Area (multi-line text)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 40000,
        'transition_default_auth': 'A',
    },
    'custom_ta2' : {
        'field_name': 'custom_ta2',
        'display_type': 'TA',
        'display_size': '60/3',
        'label': _("Custom Text Area #2"),
        'description': _("Customizable Text Area (multi-line text)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 40100,
        'transition_default_auth': 'A',
    },
    'custom_ta3' : {
        'field_name': 'custom_ta3',
        'display_type': 'TA',
        'display_size': '60/3',
        'label': _("Custom Text Area #3"),
        'description': _("Customizable Text Area (multi-line text)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 40200,
        'transition_default_auth': 'A',
    },
    'custom_ta4' : {
        'field_name': 'custom_ta4',
        'display_type': 'TA',
        'display_size': '60/3',
        'label': _("Custom Text Area #4"),
        'description': _("Customizable Text Area (multi-line text)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 40300,
        'transition_default_auth': 'A',
    },
    'custom_ta5' : {
        'field_name': 'custom_ta5',
        'display_type': 'TA',
        'display_size': '60/3',
        'label': _("Custom Text Area #5"),
        'description': _("Customizable Text Area (multi-line text)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 40400,
        'transition_default_auth': 'A',
    },
    'custom_ta6' : {
        'field_name': 'custom_ta6',
        'display_type': 'TA',
        'display_size': '60/3',
        'label': _("Custom Text Area #6"),
        'description': _("Customizable Text Area (multi-line text)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 40500,
        'transition_default_auth': 'A',
    },
    'custom_ta7' : {
        'field_name': 'custom_ta7',
        'display_type': 'TA',
        'display_size': '60/3',
        'label': _("Custom Text Area #7"),
        'description': _("Customizable Text Area (multi-line text)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 40600,
        'transition_default_auth': 'A',
    },
    'custom_ta8' : {
        'field_name': 'custom_ta8',
        'display_type': 'TA',
        'display_size': '60/3',
        'label': _("Custom Text Area #8"),
        'description': _("Customizable Text Area (multi-line text)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 40700,
        'transition_default_auth': 'A',
    },
    'custom_ta9' : {
        'field_name': 'custom_ta9',
        'display_type': 'TA',
        'display_size': '60/3',
        'label': _("Custom Text Area #9"),
        'description': _("Customizable Text Area (multi-line text)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 40800,
        'transition_default_auth': 'A',
    },
    'custom_ta10' : {
        'field_name': 'custom_ta10',
        'display_type': 'TA',
        'display_size': '60/3',
        'label': _("Custom Text Area #10"),
        'description': _("Customizable Text Area (multi-line text)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 40900,
        'transition_default_auth': 'A',
    },
    'custom_sb1' : {
        'field_name': 'custom_sb1',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Custom Select Box #1"),
        'description': _("Customizable Select Box (pull down menu with predefined values)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 50000,
        'transition_default_auth': 'A',
    },
    'custom_sb2' : {
        'field_name': 'custom_sb2',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Custom Select Box #2"),
        'description': _("Customizable Select Box (pull down menu with predefined values)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 50100,
        'transition_default_auth': 'A',
    },
    'custom_sb3' : {
        'field_name': 'custom_sb3',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Custom Select Box #3"),
        'description': _("Customizable Select Box (pull down menu with predefined values)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 50200,
        'transition_default_auth': 'A',
    },
    'custom_sb4' : {
        'field_name': 'custom_sb4',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Custom Select Box #4"),
        'description': _("Customizable Select Box (pull down menu with predefined values)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 50300,
        'transition_default_auth': 'A',
    },
    'custom_sb5' : {
        'field_name': 'custom_sb5',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Custom Select Box #5"),
        'description': _("Customizable Select Box (pull down menu with predefined values)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 50400,
        'transition_default_auth': 'A',
    },
    'custom_sb6' : {
        'field_name': 'custom_sb6',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Custom Select Box #6"),
        'description': _("Customizable Select Box (pull down menu with predefined values)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 50500,
        'transition_default_auth': 'A',
    },
    'custom_sb7' : {
        'field_name': 'custom_sb7',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Custom Select Box #7"),
        'description': _("Customizable Select Box (pull down menu with predefined values)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 50600,
        'transition_default_auth': 'A',
    },
    'custom_sb8' : {
        'field_name': 'custom_sb8',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Custom Select Box #8"),
        'description': _("Customizable Select Box (pull down menu with predefined values)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 50700,
        'transition_default_auth': 'A',
    },
    'custom_sb9' : {
        'field_name': 'custom_sb9',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Custom Select Box #9"),
        'description': _("Customizable Select Box (pull down menu with predefined values)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 50800,
        'transition_default_auth': 'A',
    },
    'custom_sb10' : {
        'field_name': 'custom_sb10',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Custom Select Box #10"),
        'description': _("Customizable Select Box (pull down menu with predefined values)"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 50900,
        'transition_default_auth': 'A',
    },
    'custom_df1' : {
        'field_name': 'custom_df1',
        'display_type': 'DF',
        'display_size': '10/10',
        'label': _("Custom Date Field #1"),
        'description': _("Customizable Date Field"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 60000,
        'transition_default_auth': 'A',
    },
    'custom_df2' : {
        'field_name': 'custom_df2',
        'display_type': 'DF',
        'display_size': '10/10',
        'label': _("Custom Date Field #2"),
        'description': _("Customizable Date Field"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 60100,
        'transition_default_auth': 'A',
    },
    'custom_df3' : {
        'field_name': 'custom_df3',
        'display_type': 'DF',
        'display_size': '10/10',
        'label': _("Custom Date Field #3"),
        'description': _("Customizable Date Field"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 60200,
        'transition_default_auth': 'A',
    },
    'custom_df4' : {
        'field_name': 'custom_df4',
        'display_type': 'DF',
        'display_size': '10/10',
        'label': _("Custom Date Field #4"),
        'description': _("Customizable Date Field"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 60300,
        'transition_default_auth': 'A',
    },
    'custom_df5' : {
        'field_name': 'custom_df5',
        'display_type': 'DF',
        'display_size': '10/10',
        'label': _("Custom Date Field #5"),
        'description': _("Customizable Date Field"),
        'scope': 'P',
        'required': 0,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 1,
        'use_it': 0,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 60400,
        'transition_default_auth': 'A',
    },
    'discussion_lock' : {
        'field_name': 'discussion_lock',
        'display_type': 'SB',
        'display_size': '',
        'label': _("Discussion Lock"),
        'description': _("Determines whether comments can still be added to the item"),
        'scope': 'S',
        'required': 1,
        'empty_ok': 1,
        'keep_history': 1,
        'special': 0,
        'custom': 0,
        'use_it': 1,
        'show_on_add': 0,
        'show_on_add_members': 0,
        'place': 800,
        'transition_default_auth': 'A',
    },
}
