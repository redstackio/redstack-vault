---
id: 2644a8c6-81b4-43d0-aa1f-f9974f326749
name: Retrieve IAM Security Credentials
type: command
executor: bash
data: curl http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_OF_PREVIOUS_COMMAND
output: null
created_at: '2023-04-06T03:56:13.577299+00:00'
updated_at: '2023-04-10T20:21:03.075046+00:00'
---

# Retrieve IAM Security Credentials

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_OF_PREVIOUS_COMMAND
```
