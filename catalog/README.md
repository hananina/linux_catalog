
# Linux server

----
##


----
# The IP address and SSH port so your server can be accessed by the reviewer.
ssh -i ~/.ssh/udacity_key.rsa root@35.160.57.253



----
# The complete URL to your hosted web application.
http://ec2-35-160-57-253.us-west-2.compute.amazonaws.com/


----
# A summary of software you installed and configuration changes made.
Hint: refer to the .bash_history files on the server!


ssh -i ~/.ssh/udacity_key.rsa root@35.160.57.253

root で入る
35.160.57.253


##2. Follow the instructions provided to SSH into your server

su grader でgraderに変更、ここにパブリックキーを入れよう
mkdir .ssh

ssh -i ~/.ssh/udacity_key.rsa root@35.160.57.253

root から下記のコマンドを打って、

ssh -i ~/.ssh/grader grader@35.160.57.253 これでは入れた！！！！


##3. Create a new user named grader

    add user grader

##4.Give the grader the permission to sudo

    adduser grader sudo


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


## 7.Configure the Uncomplicated Firewall (UFW) to only allow incoming connections for SSH (port 2200), HTTP (port 80), and NTP (port 123)

check the status of Firewall.

    ufw status

and configure the details.

    ufw default deny incoming
    ufw default allow outgoing
    ufw allow ssh
    ufw allow www
    ufw allow http
    ufw allow 80
    ufw allow ntp
    ufw allow 2200/tcp
    ufw allow 80/tcp
    ufw allow 123/udp

This to enable Firewall.

    ufw enable




##8. Configure the local timezone to UTC

    dpkg-reconfigure tzdata

choose ```None of the above```from the list. then choose ```UTC```.




## 9.Install and configure Apache 
>to serve a Python mod_wsgi application

```a2ensite itemcatalog.conf```

https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
https://github.com/adilbekm/udacity_fsnd_project_5/blob/master/database_setup.py

"after run ```python __init__.py```
check url ```http://ec2-35-160-57-253.us-west-2.compute.amazonaws.com/```

## 10.Install and configure PostgreSQL

>Do not allow remote connections
Create a new user named catalog that has limited permissions to your catalog application database

1. Install PostgreSQL:
```apt-get install postgresql```

1. Check that no remote connections are allowed: ```nano /etc/postgresql/9.3/main/pg_hba.conf```

1. Create a new user for the database: ```adduser catalog```

1. Change to postgres user: ```su postgres```

1. Connect to postgreSQL: ```psql```

1. Create a new PostgreSQL user named catalog: ```CREATE USER catalog WITH PASSWORD <password>;```

1. Alter the permissions for the catalog user: ```ALTER USER catalog CREATEDB;```
1. Create the catalog database: ```CREATE DATABASE catalog WITH OWNER catalog;```

1. Connect to the catalog database: ```\c catalog```

1. Grant access to the catalog role only: ```REVOKE ALL ON SCHEMA public FROM public;```
```GRANT ALL ON SCHEMA public TO catalog;```



## 11.Install git, clone and setup your Catalog App project 
>(from your GitHub repository from earlier in the Nanodegree program) so that it functions correctly when visiting your server’s IP address in a browser. Remember to set this up appropriately so that your .git directory is not publicly accessible via a browser!






```a2ensite itemcatalog.conf```
https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
https://github.com/adilbekm/udacity_fsnd_project_5/blob/master/database_setup.py

"after run ```python __init__.py```
check url ```http://ec2-35-160-57-253.us-west-2.compute.amazonaws.com/```







----
# A list of any third-party resources you made use of to complete this project.



























##What's this project?

A project for [Udacity Full-Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004), I'm enrolled in Novenber 2015.

Item Catalog Web Application is to display cosmetic item's information for a use.
and you can also log in to the Web Application with SNS accounts to edit, delete, add an information.


## Operating Environment 
Python 2.7.10


## Files
* README.md
* database_setup.py
* lotsofmenus.py
* templates
* application.py
* database_setup.pyc
* prepros.cfg
* catalog.db
* dev
* static


## How to start


**1. Download these files withe the command below**

----
    code git clone https://github.com/hananina/catalog_udacity_pj3.git

----

**2. Get to the download folder directory and run the command to run vagrant. and go to vm local file directory**

    vagrant up
    vagrant ssh
    cd /vagrant
    cd /catalog



**3. Run the command to run the command to start the python programs**

    python application.py



## Author
[@hananina](https://twitter.com/hananina86)

######Thank you:)