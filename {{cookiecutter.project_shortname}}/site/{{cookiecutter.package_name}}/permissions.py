"""Permission policy."""
from invenio_communities.permissions import CommunityPermissionPolicy
from invenio_communities.generators import (
    AllowedMemberTypes, 
    CommunityManagersForRole, 
    GroupsEnabled,
)
from invenio_records_permissions.generators import SystemProcess

class DatasafeCommunitiesPermissionPolicy(CommunityPermissionPolicy):
    """Communities permission policy of Datasafe."""

    # we want to allow adding members directly
    can_members_add = [
        CommunityManagersForRole(),
        AllowedMemberTypes("user", "group"),
        GroupsEnabled("group"),
        SystemProcess(),
    ]