from datasette import hookimpl
from datasette.utils import actor_matches_allow


@hookimpl
def permission_allowed(datasette, actor, action, resource):
    permissions = datasette.metadata("permissions")
    if not permissions or not actor:
        return None
    if action in permissions:
        # Use that allow block
        return actor_matches_allow(actor, permissions[action])
    return None
