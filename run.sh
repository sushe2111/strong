docker run -p 3306:3306 -v $PWD/logs:/logs -v $PWD/datae:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysqlx 
docker run  -v $PWD/tornado_strong:/usr/src/myapp  -w /usr/src/myapp -p 8001:8001 -d pythonx python main.py
