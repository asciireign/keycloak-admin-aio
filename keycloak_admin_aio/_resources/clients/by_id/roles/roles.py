from keycloak_admin_aio.types import RoleRepresentation

from .... import (
    KeycloakResource,
)


class ClientsByIdRoles(KeycloakResource):
    """Roles for clients by UUID.

    .. code:: python

        from keycloak_admin_aio import KeycloakAdmin, RoleRepresentation

        kc: KeycloakAdmin  # must be instantiated
        client_uuid: str
    """

    def get_url(self) -> str:
        return f"{self._get_parent_url()}/roles"

    async def get(self) -> list[RoleRepresentation]:
        """Get roles for a client by UUID.

        .. code:: python

            roles_resource = kc.clients.by_id(client_uuid)
            roles_representations: list[
                ClientScopeRepresentation
            ] = await roles_resource.roles.get()
        """
        connection = await self._get_connection()
        response = await connection.get(self.get_url())
        return RoleRepresentation.from_list(response.json())
