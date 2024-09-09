# Geoquery
Python script to read a list of ips and query against geolite db to display hits by country name  

### Pre-Requisites  
* Python  

### Dependencies  
```
python -m pip install geoip2  
```

### Executing  
1. Clone this repository (with git or downloading it as zip then extract it).  
2. Export the list of extracted IP's into a file named ips.txt.  
For example, to extract the ips that connected to your Linux server ( /var/log/auth.log ) use the command bellow:  
```
sudo egrep -h -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' /var/log/auth.log > /tmp/ips.txt
```
3. Put the file ips.txt in the same folder as the geoquery.py file (inside src folder of this project).
4. Install geoip2 python dependency.  
```
python -m pip install geoip2  
```
5. Run it.  
```
python geoquery.py
```


![image](https://user-images.githubusercontent.com/91758384/202926057-eb0ac0a0-e905-46e3-b9db-ace84b9129fe.png)
