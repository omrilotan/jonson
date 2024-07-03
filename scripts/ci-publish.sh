#!/usr/bin/env bash

PACKAGE=$1

if [[ -z "$PACKAGE" ]]; then
  echo "Package name is required"
  exit 1
fi

echo "Get local and published versions"
INSTALLED=$(cat setup.py | grep version | awk -F '"' '{print $2}')
LATEST=$(curl -s "https://pypi.org/pypi/$PACKAGE/json" | jq -r '.info.version')

echo "Installed version is $INSTALLED. Latest version is $LATEST"
if [ "$INSTALLED" == "$LATEST" ]; then
  echo "No publishing needed. Version $INSTALLED is already the latest" >> $GITHUB_STEP_SUMMARY
  exit 0
fi

echo "Install publish dependencies"
python -m pip install --user -r publish/requirements.txt
if [ $? -ne 0 ]; then
  echo "Failed to install"
  exit 1
fi

echo "Publish new version ($INSTALLED)" >> $GITHUB_STEP_SUMMARY
python -m setup sdist bdist_wheel
if [ $? -ne 0 ]; then
  echo "Failed to build package"
  exit 1
fi
python -m twine upload --skip-existing dist/*
if [ $? -ne 0 ]; then
  echo "Failed to publish package"
  exit 1
fi
exit 0
