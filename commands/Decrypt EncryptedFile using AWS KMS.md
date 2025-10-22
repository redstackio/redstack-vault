---
id: 96cbe21e-6bc2-4a23-bf2a-76c5ff3bbbb2
name: Decrypt EncryptedFile using AWS KMS
type: command
executor: bash
data: aws kms decrypt --ciphertext-blob fileb://EncryptedFile --output text --query
  plaintext
output: null
created_at: '2023-04-06T03:56:12.454343+00:00'
updated_at: '2023-04-10T20:20:34.546447+00:00'
---

# Decrypt EncryptedFile using AWS KMS

```bash
aws kms decrypt --ciphertext-blob fileb://EncryptedFile --output text --query plaintext
```
