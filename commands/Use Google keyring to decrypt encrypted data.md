---
id: e725d35c-3d09-4f7f-981c-11088af95e17
name: Use Google keyring to decrypt encrypted data
type: command
executor: bash
data: 'gcloud kms decrypt --ciphertext-file=encrypted-file.enc --plaintext-file=out.txt
  --key <crypto-key> --keyring <crypto-keyring> --location global

  '
output: null
created_at: '2020-07-14T19:08:34.230784+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Use Google keyring to decrypt encrypted data

```bash
gcloud kms decrypt --ciphertext-file=encrypted-file.enc --plaintext-file=out.txt --key <crypto-key> --keyring <crypto-keyring> --location global

```
