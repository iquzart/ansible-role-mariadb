"""Role testing files using testinfra."""


def test_mariadb_service_active(host):
    assert host.service('mariadb').is_running