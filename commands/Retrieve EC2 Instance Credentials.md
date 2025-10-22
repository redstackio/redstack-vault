---
id: b6eafe27-01db-4578-afb4-bc4ecd3b8a09
name: Retrieve EC2 Instance Credentials
type: command
executor: bash
data: curl http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance
output: null
created_at: '2023-04-06T03:56:13.342352+00:00'
updated_at: '2023-04-10T20:20:07.343174+00:00'
---

# Retrieve EC2 Instance Credentials

```bash
curl http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance
```
