---
id: 2e6bceee-c674-4631-be58-fd6dfe4d7de2
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:17.189385+00:00'
updated_at: '2023-04-10T20:33:49.010512+00:00'
---

# Code Snippet 2e6bceee

**Language**: Powershell

```powershell
$ docker build -t cve-2019-5736:malicious_image_POC ./RunC-CVE-2019-5736/malicious_image_POC
$ docker run --rm cve-2019-5736:malicious_image_POC
```
