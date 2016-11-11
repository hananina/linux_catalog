# Linux server
=================================

- The IP address and SSH port so your server can be accessed by the reviewer.
  ```ssh -i ~/.ssh/udacity_key.rsa root@35.161.68.50```


- The complete URL to your hosted web application.

  [http://ec2-35-161-68-50.us-west-2.compute.amazonaws.com/](http://ec2-35-161-68-50.us-west-2.compute.amazonaws.com/)



## 1. Launch your Virtual Machine with your Udacity account. 

Done!


##2. Follow the instructions provided to SSH into your server

- Download ```udacity_key.rsa```(Private Key)
- Move the private key file into the folder ~/.ssh
- Change the permission of the file
```chmod 600 ~/.ssh/udacity_key.rsa```

- Connect the server
```ssh -i ~/.ssh/udacity_key.rsa root@35.161.68.50```


##3. Create a new user named grader

    adduser grader


move to home directory of user "grader"
```cd ~```

create new directory called ".ssh" 
```mkdir .ssh```

create new file to store public key for later use 
```touch authorized_keys```


login as grader genarate pair of files. (grader.rsa, grader.rsa.pub)
*run without sudo command, otherwise you will ganarate keys under root/.ssh/
```ssh-keygen```

copy the content of "grader.rsa" to you local machine ~/.ssh/grader.rsa,
and "grader.rsa.pub" to the "authorized_keys" file in ~/.ssh/


change the permissions
```chmod 700 .ssh```
```chmod 600 authorized_keys```


```ssh -i ~/.ssh/grader.rsa grader@35.161.68.50```



##4.Give the grader the permission to sudo

    adduser grader sudo

Update configure file.

```cd /etc/sudoers.d```
create a new configuretion file.
```nano /etc/sudoers.d/grader```

and write the line below to allow sudo permission to user ```grader```

    grader ALL=(ALL) PASSWD:ALL

reload SSH
```service ssh restart```


##5.Update all currently installed packages

check the latest updates with this comand.

    sudo apt-get update

and implement actual update.

    
    sudo apt-get upgrade


##6.Change the SSH port from 22 to 2200

Open the ssh config file

    $ sudo nano /etc/ssh/sshd_config

Change the ssh port from 22 to 2200

    Port 2200


disable remote login of root user:

change ```PermitRootLogin``` from ```without-password``` to ```no```

reload SSH
```service ssh restart```

you can login with ```grader``` and ```port 2200```
```ssh grader@35.161.68.50 -p 2200```


## 7.Configure the Uncomplicated Firewall (UFW) to only allow incoming connections for SSH (port 2200), HTTP (port 80), and NTP (port 123)

check the status of Firewall.

    ufw status

and configure the details.

    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    sudo ufw allow ssh
    sudo ufw allow www
    sudo ufw allow http
    sudo ufw allow ntp
    sudo ufw allow 2200/tcp
    sudo ufw allow 80/tcp
    sudo ufw allow 123/udp

This to enable Firewall.

    sudo ufw enable


##8. Configure the local timezone to UTC

    dpkg-reconfigure tzdata

choose ```None of the above```from the list. then choose ```UTC```.



## 9.Install and configure Apache 
>to serve a Python mod_wsgi application

Install apache
```sudo apt-get install apache2```

```sudo nano /etc/apache2/sites-enabled/000-default.conf```

add the line below, before th closing tag</VirtualHost>
```WSGIScriptAlias / /var/www/html/catalog/catalog.wsgi```


    <VirtualHost *:80>
            # The ServerName directive sets the request scheme, hostname and port that
            # the server uses to identify itself. This is used when creating
            # redirection URLs. In the context of virtual hosts, the ServerName
            # specifies what hostname must appear in the request's Host: header to
            # match this virtual host. For the default virtual host (this file) this
            # value is not decisive as it is used as a last resort host regardless.
            # However, you must set it for any further virtual host explicitly.
            #ServerName www.example.com

            ServerAdmin webmaster@localhost
            DocumentRoot /var/www/html

            # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
            # error, crit, alert, emerg.
            # It is also possible to configure the loglevel for particular
            # modules, e.g.
            #LogLevel info ssl:warn

            ErrorLog ${APACHE_LOG_DIR}/error.log
            CustomLog ${APACHE_LOG_DIR}/access.log combined

            # For most configuration files from conf-available/, which are
            # enabled or disabled at a global level, it is possible to
            # include a line for only one particular virtual host. For example the
            # following line enables the CGI configuration for this host only
            # after it has been globally disabled with "a2disconf".
            #Include conf-available/serve-cgi-bin.conf
            WSGIScriptAlias / /var/www/html/catalog/catalog.wsgi
    </VirtualHost>

    # vim: syntax=apache ts=4 sw=4 sts=4 sr noet


!!I wasted a few hours since I didn't restert the apache after changed the configuration file.
Restart apache
```sudo service apache2 restart```


```catalog.wsgi``` file content below,

    <VirtualHost *:80>
            ServerName 35.161.68.50
            ServerAdmin admin@35.161.68.50
            WSGIScriptAlias / /var/www/catalog/catalog.wsgi
            <Directory /var/www/catalog/catalog/>
                Order allow,deny
                Allow from all
            </Directory>
            Alias /static /var/www/catalog/catalog/static
            <Directory /var/www/catalog/catalog/static/>
                Order allow,deny
                Allow from all
            </Directory>
            ErrorLog ${APACHE_LOG_DIR}/error.log
            LogLevel warn
            CustomLog ${APACHE_LOG_DIR}/access.log combinedsudo service apache2 restart
    </VirtualHost>


Configure according to the Tips: 
[How to deploy a flask app on an ubuntu vps](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)

[How To Set Up Apache Virtual Hosts on Ubuntu 14.04 LTS](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-14-04-lts)


【My directory structure】

    |--------catalog
    |----------------catalog
    |-----------------------static
    |-----------------------templates
    |-----------------------__init__.py
    |----------------catalog.wsgi


- Enable the application ```a2ensite itemcatalog.conf```

- Run the application
```python __init__.py```

- Check this url to see the application deployed ```http://ec2-35-161-68-50.us-west-2.compute.amazonaws.com/```

 
**Problems with configuring and how I solved it : 
[Udacity Forum](https://discussions.udacity.com/t/wsgi-app-config/195286/5)


## 10.Install and configure PostgreSQL

>Do not allow remote connections
Create a new user named catalog that has limited permissions to your catalog application database

- Install PostgreSQL
```apt-get install postgresql```

- Change to postgres user by ```su postgres```

-  Connect to postgreSQL by  ```psql```

- Create a user named catalog```CREATE USER catalog WITH PASSWORD 'password';```

- Update users permission ```ALTER USER catalog CREATEDB;```

- Create database called  catalog
```CREATE DATABASE catalog WITH OWNER catalog;```

- limit access to user called catalog only 
```REVOKE ALL ON SCHEMA public FROM public;```
```GRANT ALL ON SCHEMA public TO catalog;```


- *error*

when I run "python __initial__.py"

I got error that "can't connect the catalog user"


have to add a line to the file below, to allow this user's connection.
make sure that youu are login as "postgres"
the file in /etc/postgresql/9.3/main/pg_hba.conf

```Connect pg_hba.conf```

    local all postgres peer
    local all all peer
    host all all 127.0.0.1/32 md5
    host all all ::1/128 md5
    host catalog all 127.0.0.1/32 md5


restart postgres
```sudo /etc/init.d/postgresql restart```

and don't forget to set the password in "database_setup.py" in catalog(app directry)

```engine = create_engine( 'postgresql://catalog:PASSWORD FOR THE USER CATALOG@localhost/catalog')```


also the line in "__init__.py" 
```engine = create_engine( 'postgresql://catalog:PASSWORD FOR THE USER CATALOG@localhost/catalog')```




## 11.Install git, clone and setup your Catalog App project 
>(from your GitHub repository from earlier in the Nanodegree program) so that it functions correctly when visiting your server’s IP address in a browser. Remember to set this up appropriately so that your .git directory is not publicly accessible via a browser!

- Install git
```sudo apt-get install git```

- Add the project directory
```git clone https://github.com/hananina/linux_catalog.git```



## How to debug
apache error:
```sudo cat /var/log/apache2/error.log```

## Issues I used to have


- !!I wasted a few hours since I didn't restert the apache after changed the configuration file.
Restart apache
```sudo service apache2 restart```


- Adress already in use error

to see what is already using that port. 

```lsof -i :8889```

That will show the pid, then to stop that process
    grader@ip-10-20-16-86:/var/www/catalog/catalog$ lsof -i :8889
    COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
    python  25257 grader    3u  IPv4  88432      0t0  TCP *:8889 (LISTEN)
    python  25261 grader    3u  IPv4  88432      0t0  TCP *:8889 (LISTEN)
    python  25261 grader    6u  IPv4  88432      0t0  TCP *:8889 (LISTEN)

then, kill the connection

```kill 25257``` ```kill 25261```

https://discussions.udacity.com/t/address-already-in-use-error/185435
http://linux-topics.com/02linux/12_1.html

- Google login not working!
You have to update your ```cliant_secres.json```, get it from [app console](https://console.cloud.google.com/apis/credentials/oauthclient/).


## Author
[@hananina](https://twitter.com/hananina86)

######Thank you:)