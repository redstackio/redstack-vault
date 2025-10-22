---
id: 290beea6-31ac-4fd4-a188-6ecc6ff1f5ab
name: Get Access Token for Management API
type: command
executor: bash
data: 'IDENTITY_ENDPOINT = os.environ[''IDENTITY_ENDPOINT'']

  IDENTITY_HEADER = os.environ[''IDENTITY_HEADER'']

  cmd = ''curl "%s?resource=https://management.azure.com/&api-version=2017-09-01"
  -H secret:%s'' % (IDENTITY_ENDPOINT, IDENTITY_HEADER)

  val = os.popen(cmd).read()

  '
output: null
created_at: '2023-04-06T03:56:15.220597+00:00'
updated_at: '2023-05-24T16:02:35.210655+00:00'
---

# Get Access Token for Management API

```bash
IDENTITY_ENDPOINT = os.environ['IDENTITY_ENDPOINT']
IDENTITY_HEADER = os.environ['IDENTITY_HEADER']

cmd = 'curl "%s?resource=https://management.azure.com/&api-version=2017-09-01" -H secret:%s' % (IDENTITY_ENDPOINT, IDENTITY_HEADER)
val = os.popen(cmd).read()

```
