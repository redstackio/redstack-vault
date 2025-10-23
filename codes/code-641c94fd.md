---
id: 641c94fd-07a9-479a-ab9e-aa2c48b28c1b
type: code
language: Hashcat Rules
verified: false
created_at: '2019-10-18T00:15:53.228741+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 641c94fd

**Language**: Hashcat Rules

```hashcat rules
Nothing			:	        do nothing
Lowercase		l	Lowercase all letters
Uppercase		u	Uppercase all letters
Capitalize		c	Capitalize the first letter and lower the rest
Invert Capitalize	C	Lowercase first found character, uppercase the rest
Toggle Case		t	Toggle the case of all characters in word.
Toggle @		TN	Toggle the case of characters at position N
Reverse			r	Reverse the entire word
Duplicate		d	Duplicate entire word
Duplicate N		pN	Append duplicated word N times
Reflect			f	Duplicate word reversed
Rotate Left		{	Rotates the word left.
Rotate Right		}	Rotates the word right
Append Character	$X	Append character X to end
Prepend Character	^X	Prepend character X to front
Truncate left		[	Deletes first character
Trucate right		]	Deletes last character
Delete @ N		DN	Deletes character at position N
Extract range		xNM	Extracts M characters, starting at position N
Omit range		ONM	Deletes M characters, starting at position N
Insert @ N		iNX	Inserts character X at position N
Overwrite @ N		oNX	Overwrites character at position N with X
Truncate @ N		'N	Truncate word at position N
Replace			sXY	Replace all instances of X with Y
Purge			@X	Purge all instances of X
Duplicate first N	zN	Duplicates first character N times
Duplicate last N	ZN	Duplicates last character N times
Duplicate all		q	Duplicate every character
Extract memory		XNMI	Insert substring of length M starting from position N of word saved to memory at position I
Append memory		4	Append the word saved to memory to current word
Prepend memory		6	Prepend the word saved to memory to current word
Memorize		M	Memorize current word
```


