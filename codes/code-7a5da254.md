---
id: 7a5da254-4b91-4fa9-be63-28232e2dea72
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:37.657088+00:00'
updated_at: '2023-04-10T20:24:12.491158+00:00'
---

# Code Snippet 7a5da254

**Language**: Powershell

```powershell
1. Create a page on a whitelisted host that redirects requests to the SSRF the target URL (e.g. 192.168.0.1)
2. Launch the SSRF pointing to vulnerable.com/index.php?url=http://YOUR_SERVER_IP
vulnerable.com will fetch YOUR_SERVER_IP which will redirect to 192.168.0.1
3. You can use response codes 307 and 308 in order to retain HTTP method and body after the redirection.
```


