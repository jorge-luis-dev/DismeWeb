# DismeWeb
Disme Web Site

## Create python virtual environment
```
virtualenv venv
```
or
```
virtualenv -p python3.12 venv
```
or
```
python3.12 -m venv venv
```
## Activate python virtual environment
```
source venv/bin/activate
```
## Update pip and tools
```
pip install -U pip
pip install --upgrade wheel
pip install --upgrade setuptools
```
## Install requirements
```
pip install -r requirements.txt
```
```
pip install -e ./
```
## Create database

Use this command only in first time for create the database, the parameters are:

    -d: database name
    -r: username
    -w: password
```
odoo -d odoo18 -r odoo18 -w o --stop-after-init
```
or without demonstration data
```
odoo -d odoo18 -r odoo18 -w o --without-demo=all --stop-after-init
```
## Configuring the Odoo server options
Creates a new **odoo.conf** configuration file
```
odoo -c odoo.conf --save --stop
```
### Edit **odoo.conf**
  * db_name = odoo18
  * db_password = o
  * db_user = odoo18

## Commands and Applications
### Create odoo module
```
odoo scaffold my_module ./custom_addons/name_module
```
## Install modules
```
odoo -c odoo.conf -i product_categ_image --stop-after-init
```
```
odoo -c odoo.conf -i product_category_custom --stop-after-init
```
```
odoo -c odoo.conf -i web_portal --stop-after-init
```
### Hot Reload
```
pip install watchdog
```
Run
```
odoo -c odoo.conf --dev=all -u my_module
```
or
```
odoo -c odoo.conf --dev=reload -u my_module 
```
### Pre-commit
Run in folder where contains module or modules
```
pip install pre-commit
```
Run
```
pre-commit run -a
```

