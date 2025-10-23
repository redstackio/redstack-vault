---
id: 0e9ac0e7-91e1-44dc-9530-3ca380d2aab3
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:17.031354+00:00'
updated_at: '2023-04-10T20:33:50.752012+00:00'
---

# Code Snippet 0e9ac0e7

**Language**: Powershell

```powershell
docker login -u admin -p admin docker.registry.local
docker pull docker.registry.local/wordpress-image
docker run -it docker.registry.local/wordpress-image /bin/bash
```


