---
data: >-
  curl
  'https://www.quora.com/webnode2/server_call_POST?_v=2rtUq6Z4HO9gWK&_m=edit' -H
  'Cookie: m-b="██████████████████"; m-sa=1; m-s="███████████████";
  m-screen_size=1920x1080; m-login=1; m-ju=███████████████████████████;
  m-early_v=4e4c117b82baf40e; m-tz=-120; m-css_v=69026465bc2615b6;
  m-wf-loaded=q-icons-q_serif; _ga=GA1.2.2058437224.1502195915;
  _gid=GA1.2.1848940326.1502195915' -H 'Origin: https://www.quora.com' -H
  'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language:
  it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4' -H 'User-Agent: Mozilla/5.0 (X11; Linux
  x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90
  Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded;
  charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H
  'Referer: https://www.quora.com/profile/Aleph-NaN' -H 'X-Requested-With:
  XMLHttpRequest' -H 'Connection: keep-alive' -H 'DNT: 1' --data
  'json={"args":[],"kwargs":{"id":███████████,"input":{"sections":[{"type":"plain","indent":0,"quoted":false,"spans":[{"modifiers":{},"text":"a"}]}],"caret":{"start":{"spanIdx":0,"sectionIdx":0,"offset":1},"end":{"spanIdx":0,"sectionIdx":0,"offset":1}}}}}&revision=904d048187b642341464067b64246119b8ce9489&formkey=6a34c75ed7fda8439ca2407b4520c974&postkey=736f2eea9e3826808823625bf4ede215&window_id=dep3204-1727465467565139446&referring_controller=user&referring_action=profile&_lm_transaction_id=0.7159021828610441&_lm_window_id=dep3204-1727465467565139446&__vcon_json=["2rtUq6Z4HO9gWK"]&__vcon_method=edit&__e2e_action_id=esl2xq4xyj&js_init={"id":████████████,"input":"user_description_text","typing_area":null,"draft_space":null,"unsaved_content_msg":"Your
  content has not been
  saved.","focus_onload":false,"is_qtext":true,"require_comment":false,"require_value":false,"content_type":null,"submit_text":"Update","show_editor":false}&__metadata={}'
  --compressed
tags:
  - xss
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:44.597Z'
id: 5d56d5e5-5ca1-4137-ba46-4921561fa2f3
verified: false
validated: true
submitted: true
---
# curl-quora-normal-edit

## Command

```bash
curl 'https://www.quora.com/webnode2/server_call_POST?_v=2rtUq6Z4HO9gWK&_m=edit' -H 'Cookie: m-b="██████████████████"; m-sa=1; m-s="███████████████"; m-screen_size=1920x1080; m-login=1; m-ju=███████████████████████████; m-early_v=4e4c117b82baf40e; m-tz=-120; m-css_v=69026465bc2615b6; m-wf-loaded=q-icons-q_serif; _ga=GA1.2.2058437224.1502195915; _gid=GA1.2.1848940326.1502195915' -H 'Origin: https://www.quora.com' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://www.quora.com/profile/Aleph-NaN' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'DNT: 1' --data 'json={"args":[],"kwargs":{"id":███████████,"input":{"sections":[{"type":"plain","indent":0,"quoted":false,"spans":[{"modifiers":{},"text":"a"}]}],"caret":{"start":{"spanIdx":0,"sectionIdx":0,"offset":1},"end":{"spanIdx":0,"sectionIdx":0,"offset":1}}}}}&revision=904d048187b642341464067b64246119b8ce9489&formkey=6a34c75ed7fda8439ca2407b4520c974&postkey=736f2eea9e3826808823625bf4ede215&window_id=dep3204-1727465467565139446&referring_controller=user&referring_action=profile&_lm_transaction_id=0.7159021828610441&_lm_window_id=dep3204-1727465467565139446&__vcon_json=["2rtUq6Z4HO9gWK"]&__vcon_method=edit&__e2e_action_id=esl2xq4xyj&js_init={"id":████████████,"input":"user_description_text","typing_area":null,"draft_space":null,"unsaved_content_msg":"Your content has not been saved.","focus_onload":false,"is_qtext":true,"require_comment":false,"require_value":false,"content_type":null,"submit_text":"Update","show_editor":false}&__metadata={}' --compressed
```

## Description

Sends a legitimate profile edit request to Quora's server_call_POST endpoint, capturing parameters for later modification in XSS/IDOR exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H 'Cookie: ...' | Session cookies for authentication | Yes |
| --data 'json=...' | Edit payload with sections and caret | Yes |
| window_id | Attacker's channel | Yes |
| __e2e_action_id | Normal action ID | Yes |
| --compressed | Enable gzip compression | No |

## Examples

### Basic Usage

```bash
curl 'https://www.quora.com/webnode2/server_call_POST?_v=2rtUq6Z4HO9gWK&_m=edit' ... --data '...' --compressed
```

### Advanced Usage

Copy from browser dev tools and adjust for replay.

## Expected Output

HTTP 200 OK with {"value": null, "pmsg": null}; edit applied and message queued to channel.

## Related

- [[commands/curl-quora-xss-exploit]]
- [[procedures/Login-and-Capture-Normal-Edit-Request]]
