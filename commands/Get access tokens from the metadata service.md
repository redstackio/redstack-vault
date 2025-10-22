---
id: ff6f8e67-5a57-4e70-9bd9-20a04748a43d
name: Get access tokens from the metadata service
type: command
executor: bash
data: 'GET ''http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/''
  HTTP/1.1 Metadata: true

  '
output: null
created_at: '2020-07-14T19:07:50.928987+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get access tokens from the metadata service

```bash
GET 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/' HTTP/1.1 Metadata: true

```
