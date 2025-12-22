---
id: bf018377-733b-4d99-8648-d322227c5703
name: ssh-login-to-aws-instance
type: command
executor: bash
data: ssh -i $_EXISTING_PRIVATE_KEY $_USERNAME@$_INSTANCE_ADDRESS
output: null
created_at: '2023-04-06T03:56:13.676230+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ssh
  - access
verified: true
validated: true
---

# ssh-login-to-aws-instance

## Command

```bash
ssh -i $_EXISTING_PRIVATE_KEY $_USERNAME@$_INSTANCE_ADDRESS
```

## Description

This command establishes an SSH connection to an AWS EC2 instance using an existing private key for authentication, providing shell access to perform further actions like persistence setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_EXISTING_PRIVATE_KEY | Path to the private key file for initial access (e.g., ~/.ssh/id_rsa) | Yes |
| $_USERNAME | Target username on the instance (e.g., ec2-user, ubuntu) | Yes |
| $_INSTANCE_ADDRESS | Public DNS or IP of the EC2 instance (e.g., ec2-xxx-xxx-xxx-xxx.compute-1.amazonaws.com) | Yes |
| -i | Specifies the identity file (private key) | Built-in |

## Examples

### Basic Usage

```bash
ssh -i ~/.ssh/mykey.pem ec2-user@ec2-12-34-56-78.compute-1.amazonaws.com
```

### Advanced Usage

```bash
ssh -i ~/.ssh/mykey.pem -o StrictHostKeyChecking=no ec2-user@ec2-12-34-56-78.compute-1.amazonaws.com
```

## Expected Output

Successful connection shows a login banner and shell prompt:

```
The authenticity of host 'ec2-...' can't be established.
ECDSA key fingerprint is SHA256:...
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'ec2-...' to the list of known hosts.
               __|  __|_  )
               _|  (     /   Amazon Linux 2 AMI
          ___|\___|/  Amazon Linux release 2 (Karoo)

https://aws.amazon.com/amazon-linux-2/
[ec2-user@ip-xxx-xxx-xxx-xxx ~]$ 
```

## Related

- [[procedures/AWS-SSH-Persistence-using-Public-Key]]
