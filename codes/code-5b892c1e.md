---
id: 5b892c1e-4b17-4cb3-ab95-b331d64016e0
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:00.200176+00:00'
updated_at: '2023-04-10T20:33:56.272193+00:00'
---

# Code Snippet 5b892c1e

**Language**: Powershell

```powershell
# Run gitleaks against a local repository already cloned into /tmp/
docker run --rm --name=gitleaks -v /tmp/:/code/  zricethezav/gitleaks -v --repo-path=/code/gitleaks

```
