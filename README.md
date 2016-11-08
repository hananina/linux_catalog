# Linux server
=================================

- The IP address and SSH port so your server can be accessed by the reviewer.
  ```ssh -i ~/.ssh/udacity_key.rsa root@35.160.57.253```


- The complete URL to your hosted web application.

  [http://ec2-35-160-57-253.us-west-2.compute.amazonaws.com/](http://ec2-35-160-57-253.us-west-2.compute.amazonaws.com/)



## 1. Launch your Virtual Machine with your Udacity account. 

Done!


##2. Follow the instructions provided to SSH into your server

- Download ```udacity_key.rsa```(Private Key)
- Move the private key file into the folder ~/.ssh
- Change the permission of the file
```chmod 600 ~/.ssh/udacity_key.rsa```

- Connect the server
```ssh -i ~/.ssh/udacity_key.rsa root@35.160.57.253```


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

Configure according to the Tips: [How to deploy a flask app on an ubuntu vps]
(https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)


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

- Check this url to see the application deployed ```http://ec2-35-160-57-253.us-west-2.compute.amazonaws.com/```

 
**Problems with configuring and how I solved it : 
[Udacity Forum](https://discussions.udacity.com/t/wsgi-app-config/195286/5)


## 10.Install and configure PostgreSQL

>Do not allow remote connections
Create a new user named catalog that has limited permissions to your catalog application database

- Install PostgreSQL
```apt-get install postgresql```

- Change to postgres user by ```su postgres```

-  Connect to postgreSQL by  ```psql```

- Create a user named catalog```CREATE USER catalog WITH PASSWORD <password>;```

- Update users permission ```ALTER USER catalog CREATEDB;```

- Create database called  catalog
```CREATE DATABASE catalog WITH OWNER catalog;```

- limit access to user called catalog only 
```REVOKE ALL ON SCHEMA public FROM public;```
```GRANT ALL ON SCHEMA public TO catalog;```


## 11.Install git, clone and setup your Catalog App project 
>(from your GitHub repository from earlier in the Nanodegree program) so that it functions correctly when visiting your server’s IP address in a browser. Remember to set this up appropriately so that your .git directory is not publicly accessible via a browser!

- Install git
```sudo apt-get install git```

- Add the project directory
```git clone https://github.com/hananina/linux_catalog.git```


## Author
[@hananina](https://twitter.com/hananina86)

######Thank you:)