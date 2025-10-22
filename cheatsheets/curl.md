---
id: e380b72f-251b-4369-8105-ac73de03e548
name: curl
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:56.398685+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# curl

**Command** ([[download emails via curl]]):

```bash
curl --insecure --url "imaps://target-domain/Drafts;UID=4" --user "username:password"

```

**Command** ([[bypass useragent blacklisting]]):

```bash
curl -A "Googlebot" http://target-ip/robots.txt

```
