---
id: b45bab75-dc38-4313-b2b1-e04b7f9dd1e6
name: aws-iam-list-ssh-public-keys-for-user
type: command
executor: bash
data: |
  aws iam list-ssh-public-keys --user-name $AWS_IAM_USER
output: null
created_at: '2020-07-31T04:25:28.973336+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - aws
  - iam
  - discovery
  - ssh
verified: true
validated: true
---

# aws-iam-list-ssh-public-keys-for-user

## Command

```bash
aws iam list-ssh-public-keys --user-name $_AWS_IAM_USER
```

## Description

This command lists SSH public keys associated with an IAM user, which can be used for EC2 access. It aids in discovering alternative authentication methods.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --user-name $_AWS_IAM_USER | The IAM username (e.g., 'dev-user') | Yes |

## Examples

### Basic Usage

```bash
aws iam list-ssh-public-keys --user-name dev-user
```

### With Table Output

```bash
aws iam list-ssh-public-keys --user-name dev-user --output table
```

## Expected Output

```
{
    "SSHPublicKeys": [
        {
            "UserName": "dev-user",
            "SSHPublicKeyId": "APKA1234EXAMPLE",
            "Fingerprint": "01:23:45:67:89:ab:cd:ef:01:23:45:67:89:ab:cd:ef",
            "Status": "Active",
            "UploadDate": "2015-03-09T18:39:23.411Z"
        }
    ]
}
```

Returns a list of SSH keys with fingerprints and status.

## Related

- [[procedures/List-AWS-IAM-Access-Keys]]
- [[commands/aws-iam-list-access-keys-for-user]]
