---
id: 18a1acf0-ef2c-41d3-8813-1767b1be428e
name: Get Access Token for Graph API
type: command
executor: bash
data: 'IDENTITY_ENDPOINT = os.environ[''IDENTITY_ENDPOINT'']

  IDENTITY_HEADER = os.environ[''IDENTITY_HEADER'']


  cmd = ''curl "%s?resource=https://graph.microsoft.com/&api-version=2017-09-01" -H
  secret:%s'' % (IDENTITY_ENDPOINT, IDENTITY_HEADER)

  val = os.popen(cmd).read()

  '
output: null
created_at: '2023-04-06T03:56:15.220657+00:00'
updated_at: '2023-05-24T16:02:35.207183+00:00'
---

# Get Access Token for Graph API

```bash
IDENTITY_ENDPOINT = os.environ['IDENTITY_ENDPOINT']
IDENTITY_HEADER = os.environ['IDENTITY_HEADER']

cmd = 'curl "%s?resource=https://graph.microsoft.com/&api-version=2017-09-01" -H secret:%s' % (IDENTITY_ENDPOINT, IDENTITY_HEADER)
val = os.popen(cmd).read()

```


