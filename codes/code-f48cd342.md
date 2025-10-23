---
id: f48cd342-82df-4edd-b441-315af87d2af5
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:24.983449+00:00'
updated_at: '2023-04-10T20:25:31.246275+00:00'
---

# Code Snippet f48cd342

**Language**: Powershell

```powershell
ctrl+z
echo $TERM && tput lines && tput cols

# for bash
stty raw -echo
fg

# for zsh
stty raw -echo; fg

reset
export SHELL=bash
export TERM=xterm-256color
stty rows <num> columns <cols>
```


