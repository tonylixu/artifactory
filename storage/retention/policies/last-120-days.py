"""
Usage:
    $ lavatory purge --policies-path=./last-120-days.py --repo repo-name
"""

def purgelist(artifactory):
    """Policy to purge all artifacts older than 120 days"""
    purgable = artifactory.time_based_retention(keep_days=120)
    return purgable
