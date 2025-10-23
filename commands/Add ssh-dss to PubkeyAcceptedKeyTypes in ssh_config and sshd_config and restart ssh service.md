---
id: f53ece4a-de38-4ea1-9635-9c3d46d40b35
name: Add ssh-dss to PubkeyAcceptedKeyTypes in ssh_config and sshd_config and restart
  ssh service
type: command
executor: bash
data: 'echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/ssh_config

  echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/sshd_config

  /etc/init.d/ssh restart'
output: null
created_at: '2023-04-06T03:56:18.624933+00:00'
updated_at: '2023-04-10T20:34:29.313841+00:00'
---

# Add ssh-dss to PubkeyAcceptedKeyTypes in ssh_config and sshd_config and restart ssh service

```bash
echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/ssh_config
echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/sshd_config
/etc/init.d/ssh restart
```


