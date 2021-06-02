#!/bin/bash
#chmod +x pact_runner.py

PYON_ENVIRONMENT='staging'
PYON_EXCLUDED_TAG='wip'

PYON_TARGET='local'
PYON_MODE='api'

PYON_OS='MacOS Catalina'
PYON_OS_VERSION=

PYON_TAGS='swapi_planets_suite'

# echo 'COPYING PROPERTIES'
# cp env_settings.properties.local env_settings.properties
# echo 'UPDATING PACKAGES...'
# python update.py
python pact_runner.py --target $PYON_TARGET \
                      --environment "$PYON_ENVIRONMENT" \
                      --mode $PYON_MODE \
                      --os "$PYON_OS" \
                      --os_version "$PYON_OS_VERSION" \
                      --tags "$PYON_TAGS"
