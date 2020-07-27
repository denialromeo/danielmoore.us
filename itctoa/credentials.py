import keyring

MAGIC_USERNAME_KEY = 'im_the_magic_username_key'

# the service is just a namespace for your app

service_id =’iTOA’

username = 'toa_user'  # replace with username we hard coded in conftest

# save password

keyring.set_password(service_id, username, "WelcomeITC@2019") # replae with password from conftest

# save password

keyring.set_password(service_id, MAGIC_USERNAME_KEY, username )# replae with username  from conftest
