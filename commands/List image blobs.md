---
id: 9cdcfb1d-34b8-4a92-9f0f-c3db10db6793
name: List image blobs
type: command
executor: bash
data: 'curl -s -k --user "admin:admin" https://docker.registry.local/v2/_catalog

  curl -s -k --user "admin:admin" https://docker.registry.local/v2/wordpress-image/tags/list

  curl -s -k --user "admin:admin" https://docker.registry.local/v2/wordpress-image/manifests/latest'
output: null
created_at: '2023-04-06T03:56:17.031155+00:00'
updated_at: '2023-04-10T20:33:50.751327+00:00'
---

# List image blobs

```bash
curl -s -k --user "admin:admin" https://docker.registry.local/v2/_catalog
curl -s -k --user "admin:admin" https://docker.registry.local/v2/wordpress-image/tags/list
curl -s -k --user "admin:admin" https://docker.registry.local/v2/wordpress-image/manifests/latest
```


