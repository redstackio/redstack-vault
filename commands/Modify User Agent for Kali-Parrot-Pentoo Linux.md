---
id: a6b91027-dfa9-48c3-8e2b-f7914e65e1bd
name: Modify User Agent for Kali/Parrot/Pentoo Linux
type: command
executor: bash
data: "boto3_session = boto3.session.Session()\nua = boto3_session._session.user_agent()\n\
  if 'kali' in ua.lower() or 'parrot' in ua.lower() or 'pentoo' in ua.lower():  #\
  \ If the local OS is Kali/Parrot/Pentoo Linux\n    # GuardDuty triggers a finding\
  \ around API calls made from Kali Linux, so let's avoid that...\n    self.print('Detected\
  \ environment as one of Kali/Parrot/Pentoo Linux. Modifying user agent to hide that\
  \ from GuardDuty...')"
output: null
created_at: '2023-04-06T03:56:09.785937+00:00'
updated_at: '2023-04-10T20:19:56.179198+00:00'
---

# Modify User Agent for Kali/Parrot/Pentoo Linux

```bash
boto3_session = boto3.session.Session()
ua = boto3_session._session.user_agent()
if 'kali' in ua.lower() or 'parrot' in ua.lower() or 'pentoo' in ua.lower():  # If the local OS is Kali/Parrot/Pentoo Linux
    # GuardDuty triggers a finding around API calls made from Kali Linux, so let's avoid that...
    self.print('Detected environment as one of Kali/Parrot/Pentoo Linux. Modifying user agent to hide that from GuardDuty...')
```


