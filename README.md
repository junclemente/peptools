# Peptide Tool

This is a simple web app written in Flask and Python.
Currently, its purpose is to take an amino acid chain written in 1-letter representation and
converts it to its 3-letter representation equivalent. Even though there are other apps that perform the same function, this app was written specifically for a company I was working for and developed with their specific requirements.

## How To Use
You need to download the zip or clone the repository to your computer. You will also need to have VirtualBox and Vagrant installed on your computer to run this app.

### Install following software if necessary
* Install [VirtualBox](https://www.virtualbox.org).
* Install [Vagrant](https://www.vagrantup.com).

### Clone the repository
* Open the terminal/command prompt.
* Clone the repository and enter the peptools directory:

```
$ git clone https://github.com/junclemente/peptools.git
$ cd peptools
```

### Start the Vagrant environment

* Initiate the Vagrant environment:

```
$ vagrant up
```

* Enter the vagrant environment

```
$ vagrant ssh
```

### Start the app
* Enter the app directory and start the app:

```
$ cd /vagrant
$ python run.py
```

### Access the web page
* Open up your favorite webrowser and open the following URL address:
[localhost:8080](http://localhost:8080)


