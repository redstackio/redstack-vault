---
id: 2837268e-f498-47e8-96db-b093e5066ad3
name: Accessing EC2 instance metadata
type: command
executor: bash
data: 'http://169.254.169.254/latest/user-data

  http://169.254.169.254/latest/user-data/iam/security-credentials/[ROLE NAME]

  http://169.254.169.254/latest/meta-data/

  http://169.254.169.254/latest/meta-data/iam/security-credentials/[ROLE NAME]

  http://169.254.169.254/latest/meta-data/iam/security-credentials/PhotonInstance

  http://169.254.169.254/latest/meta-data/ami-id

  http://169.254.169.254/latest/meta-data/reservation-id

  http://169.254.169.254/latest/meta-data/hostname

  http://169.254.169.254/latest/meta-data/public-keys/

  http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key

  http://169.254.169.254/latest/meta-data/public-keys/[ID]/openssh-key

  http://169.254.169.254/latest/meta-data/iam/security-credentials/dummy

  http://169.254.169.254/latest/meta-data/iam/security-credentials/s3access

  http://169.254.169.254/latest/dynamic/instance-identity/document'
output: null
created_at: '2023-04-06T03:56:38.154291+00:00'
updated_at: '2023-04-10T20:23:59.980820+00:00'
---

# Accessing EC2 instance metadata

```bash
http://169.254.169.254/latest/user-data
http://169.254.169.254/latest/user-data/iam/security-credentials/[ROLE NAME]
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/[ROLE NAME]
http://169.254.169.254/latest/meta-data/iam/security-credentials/PhotonInstance
http://169.254.169.254/latest/meta-data/ami-id
http://169.254.169.254/latest/meta-data/reservation-id
http://169.254.169.254/latest/meta-data/hostname
http://169.254.169.254/latest/meta-data/public-keys/
http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key
http://169.254.169.254/latest/meta-data/public-keys/[ID]/openssh-key
http://169.254.169.254/latest/meta-data/iam/security-credentials/dummy
http://169.254.169.254/latest/meta-data/iam/security-credentials/s3access
http://169.254.169.254/latest/dynamic/instance-identity/document
```


