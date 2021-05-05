MariaDB Server
=========

[![Ansible Galaxy](https://img.shields.io/badge/galaxy-iquzart.mariadb-blue)](https://galaxy.ansible.com/iquzart/mariadb)
![Molecule Test](https://github.com/iquzart/ansible-role-mariadb/workflows/Molecule%20Test/badge.svg?) 
[![License](https://img.shields.io/:license-mit-blue.svg)](https://badges.mit-license.org)


Ansible Role for MariaDB server

Features
---------
```
  1. Custom config with 
      - data directory
      - bind-address      
      - port
```

Support Matrix
---------------
| Destro | MariaDB 10.5 | 
| --- | --- |
| CentOS 8 | Supported (Tested) | 
| CentOS 7 | Supported (Tested) |
| Ubuntu 20.04 LTS | Supported (Tested) |
| Ubuntu 19.04 LTS | Supported (Tested) |
| Debian 10 | Supported (Tested) |
| Debian 9  | Supported (Tested) |


Role Variables
--------------

| Variable Name| Description | Default |
|---|---|---|
| mariadb_version  | MariaDB version | 10.5 |
| mariadb_port  | MariaDB PORT  | 3306  |
| mariadb_data_dir  | Database directory  | /var/lib/mysql |
| mariadb_bind_address  | MariaDB listen on  | 127.0.0.1  |

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: iquzart.mariadb }

License
-------

MIT

Author Information
------------------

Muhammed Iqbal <iquzart@hotmail.com>
