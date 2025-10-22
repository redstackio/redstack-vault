---
id: 420b7d4e-4bfa-41c9-a308-60442b268901
name: Query System Information
type: command
executor: bash
data: select os_name,os_version,os_release,host_name from sysibmadm.env_sys_info --
  requires priv
output: null
created_at: '2023-04-06T03:56:33.151418+00:00'
updated_at: '2023-04-10T20:22:02.290872+00:00'
---

# Query System Information

```bash
select os_name,os_version,os_release,host_name from sysibmadm.env_sys_info -- requires priv
```
