# data: URLs

Data URLs, URLs prefixed with the data: scheme, allow content creators to embed small files inline in documents.

## `data:[<media-type>][;base64],<data>`


### `data:`

The scheme of the URL

### `<media-type>`

The MIME type indicating the type of data, such as image/jpeg for a JPEG image file. If omitted, defaults to text/plain;charset=US-ASCII.
 
### `;base64`

Indicates that the data should be base64-decoded

### `<data>`

The data itself. If the data contains characters defined in RFC 3986 as reserved characters, or contains space characters, newline characters, or other non-printing characters, those characters must be percent-encoded. If the data is textual, you can embed the text (using the appropriate entities or escapes based on the enclosing document's type). Otherwise, you can specify base64 to embed base64-encoded binary data.