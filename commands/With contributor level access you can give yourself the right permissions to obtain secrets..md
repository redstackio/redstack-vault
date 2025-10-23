---
id: d8ee0d74-ecc3-4297-a5e8-5bbc0f2c3454
name: With contributor level access you can give yourself the right permissions to
  obtain secrets.
type: command
executor: bash
data: 'az keyvault set-policy --name <KeyVaultname> --upn <YourContributorUsername>
  --secret-permissions get list --key-permissions get list --storage-permissions get
  list --certificate-permissions get list

  '
output: null
created_at: '2020-07-14T19:07:50.926105+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# With contributor level access you can give yourself the right permissions to obtain secrets.

```bash
az keyvault set-policy --name <KeyVaultname> --upn <YourContributorUsername> --secret-permissions get list --key-permissions get list --storage-permissions get list --certificate-permissions get list

```


