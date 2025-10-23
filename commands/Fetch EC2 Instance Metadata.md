---
id: 239bd5a7-e0d9-4978-a867-86a54c68bb94
name: Fetch EC2 Instance Metadata
type: command
executor: bash
data: 'http://169.254.169.254/latest/meta-data/

  http://169.254.169.254/latest/user-data/

  http://169.254.169.254/latest/meta-data/iam/security-credentials/IAM_USER_ROLE_HERE
  will return the AccessKeyID, SecretAccessKey, and Token

  http://169.254.169.254/latest/meta-data/iam/security-credentials/PhotonInstance'
output: null
created_at: '2023-04-06T03:55:53.744763+00:00'
updated_at: '2023-04-06T03:55:53.763748+00:00'
---

# Fetch EC2 Instance Metadata

```bash
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/user-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/IAM_USER_ROLE_HERE will return the AccessKeyID, SecretAccessKey, and Token
http://169.254.169.254/latest/meta-data/iam/security-credentials/PhotonInstance
```


