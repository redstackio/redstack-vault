---
id: d88b1934-7077-4e48-88fa-1d9f74d16be8
name: Add OpenSSL server address to hosts file
type: command
executor: bash
data: 'sudo echo "[OPENSSL SERVER ADDRESS] [domain.of.server.to.mitm]" >> /etc/hosts  #
  On client host'
output: null
created_at: '2023-04-06T03:56:22.335771+00:00'
updated_at: '2023-04-10T20:25:09.843906+00:00'
---

# Add OpenSSL server address to hosts file

```bash
sudo echo "[OPENSSL SERVER ADDRESS] [domain.of.server.to.mitm]" >> /etc/hosts  # On client host
```
