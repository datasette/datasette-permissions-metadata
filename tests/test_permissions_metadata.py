from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize("allowed", (False, True))
async def test_plugin(allowed):
    metadata = {}
    if allowed:
        metadata = {"permissions": {"permissions-debug": {"id": "user"}}}
    datasette = Datasette(metadata=metadata)
    cookies = {"ds_actor": datasette.sign({"a": {"id": "user"}}, "actor")}
    response = await datasette.client.get("/-/permissions", cookies=cookies)
    if allowed:
        assert response.status_code == 200
    else:
        assert response.status_code == 403
