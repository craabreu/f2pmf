"""
Forces to PMF
RBF Regression from Gradient Samples
"""

# Add imports here
from .f2pmf import Variable  # noqa: F401, F403

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
