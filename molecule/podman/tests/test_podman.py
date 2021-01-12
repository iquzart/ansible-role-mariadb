"""Role testing files using testinfra."""


def test_mariadb_is_installed(host):
    mariadb_package = host.package("MariaDB-server")
    assert mariadb_package.is_installed
