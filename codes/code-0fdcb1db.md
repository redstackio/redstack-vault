---
id: 0fdcb1db-01df-49c9-9550-7fdd53990c21
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:14.584641+00:00'
updated_at: '2023-04-10T20:19:39.811529+00:00'
---

# Code Snippet 0fdcb1db

**Language**: Powershell

```powershell
pipenv shell
roadrecon auth [-h] [-u USERNAME] [-p PASSWORD] [-t TENANT] [-c CLIENT] [--as-app] [--device-code] [--access-token ACCESS_TOKEN] [--refresh-token REFRESH_TOKEN] [-f TOKENFILE] [--tokens-stdout]
roadrecon gather [-h] [-d DATABASE] [-f TOKENFILE] [--tokens-stdin] [--mfa]
roadrecon auth -u test@<TENANT NAME>.onmicrosoft.com -p <PASSWORD>
roadrecon gather
roadrecon gui
```
