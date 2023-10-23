#! /usr/bin/python3

# This is based on the PR at
# https://salsa.debian.org/cpython-team/python3-defaults/-/merge_requests/11

import sys
sys.path.insert(0, "/usr/share/python3")
from py3versions import supported_versions, version_to_tuple


def minmax_supported_version(minmax, version_only=False):
    supported_versions_list = supported_versions(True)
    version = minmax(version_to_tuple(ver) for ver in supported_versions_list)
    version_str = '%d.%d' % version
    if version_only:
        return version_str
    else:
        return 'python' + version_str


if __name__ == "__main__":
    print(minmax_supported_version(min))

