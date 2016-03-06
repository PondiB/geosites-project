
# Settings to apply to all GeoSites

import os
from geonode.contrib import geosites

# Start with GeoSites pre_settings
GEOSITES_ROOT = os.path.dirname(geosites.__file__)
execfile(os.path.join(GEOSITES_ROOT, 'pre_settings.py'))

# global settings

# base urls for all sites
ROOT_URLCONF = '{{ project_name }}.urls'

# Zinnia blog app
INSTALLED_APPS = INSTALLED_APPS + (
    'zinnia',
    'django_comments',
    'tagging'
)

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'zinnia.context_processors.version',
)

THEME_ACCOUNT_CONTACT_EMAIL = ''
