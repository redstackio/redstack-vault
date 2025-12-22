---
id: e5f3c57e-34be-470f-8101-3eb13a524584
name: ssh2john-extract-hash-from-encrypted-ssh-key
type: command
executor: bash
data: python ssh2john.py $_PRIVATE_KEY > $_OUTPUT_FILE
output: '$sshng$1024$hash:plaintext$salt:iv'
created_at: '2019-10-25T19:09:24.118813+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - cryptography
  - credential-access
verified: true
validated: true
---

# ssh2john-extract-hash-from-encrypted-ssh-key

## Command

```bash
python ssh2john.py $_PRIVATE_KEY > $_OUTPUT_FILE
```

## Description

This command invokes the ssh2john.py script to parse an encrypted SSH private key file and extract its passphrase hash in a format suitable for cracking with John the Ripper. It is used in scenarios where an attacker has obtained an encrypted private key (e.g., from a compromised .ssh directory) and needs to recover the protecting passphrase through offline attacks. The command assumes ssh2john.py is in the PATH or a known location like /usr/share/john/.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PRIVATE_KEY | Path to the encrypted SSH private key file (e.g., id_rsa, id_dsa.enc; supports RSA/DSA/EC) | Yes |
| $_OUTPUT_FILE | File to redirect the extracted hash output to (e.g., ssh_hash.txt) | Yes |
| python | Python interpreter to run the script | Built-in |

## Examples

### Basic Usage

```bash
python /usr/share/john/ssh2john.py id_rsa.enc > ssh_hash.txt
```

### Advanced Usage

```bash
python ssh2john.py "/home/user/.ssh/id_rsa" > /tmp/extracted_ssh_hash.txt
```

## Expected Output

The command executes without verbose output to the console but generates a file containing the hash in John the Ripper format. Example content of $_OUTPUT_FILE:

```
$sshng$1024$hash:plaintext$salt:iv
```

Verify success by checking the file:
```bash
cat $_OUTPUT_FILE
```
No errors indicate a valid encrypted key was processed. If the key is unencrypted, no hash will be produced.

## Related

- [[tools/ssh2john]]
- [[commands/john-crack-sshng-hash]]
