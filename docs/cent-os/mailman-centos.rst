.. -*- coding: utf-8 -*-

.. highlight:: rest

.. _colab_software:

Mailman
=======

Install the fcgiwrap

.. code-block::

    sudo yum install fcgi-devel git -y
    cd /tmp
    sudo git clone https://github.com/gnosek/fcgiwrap.git
    cd fcgiwrap
    sudo yum groupinstall "Development tools" -y
    sudo autoreconf -i
    sudo ./configure
    sudo make
    sudo make install

Now you can install spawn fcgi

.. code-block::

    sudo yum install spawn-fcgi -y
    
And edit the spawn-fgci configuration file

.. code-block::

    sudo vim /etc/sysconfig/spawn-fcgi

.. code-block::

    FCGI_SOCKET=/var/run/fcgiwrap.socket
    FCGI_PROGRAM=/usr/local/sbin/fcgiwrap
    FCGI_USER=apache
    FCGI_GROUP=apache
    FCGI_EXTRA_OPTIONS="-M 0770"
    OPTIONS="-u $FCGI_USER -g $FCGI_GROUP -s $FCGI_SOCKET -S $FCGI_EXTRA_OPTIONS -F 1 -P /var/run/spawn-fcgi.pid -- $FCGI_PROGRAM"

Save and quit
    
.. code-block::

    [ESC]:wq!

Install mailman

.. code-block::

    sudo yum install mailman -y
    
Create a list, in this case we called it ``mailman``

.. code-block::

    sudo /usr/lib/mailman/bin/newlist mailman

Put a real email in ``Enter the email of the person running the list:``. And put a password in ``Initial mailman password:``, we used ``admin`` as password.
    
And add that list to the aliases file

.. code-block::

    sudo vim /etc/aliases
    
.. code-block::

    ## mailman mailing list
    mailman:              "|/usr/lib/mailman/mail/mailman post mailman"
    mailman-admin:        "|/usr/lib/mailman/mail/mailman admin mailman"
    mailman-bounces:      "|/usr/lib/mailman/mail/mailman bounces mailman"
    mailman-confirm:      "|/usr/lib/mailman/mail/mailman confirm mailman"
    mailman-join:         "|/usr/lib/mailman/mail/mailman join mailman"
    mailman-leave:        "|/usr/lib/mailman/mail/mailman leave mailman"
    mailman-owner:        "|/usr/lib/mailman/mail/mailman owner mailman"
    mailman-request:      "|/usr/lib/mailman/mail/mailman request mailman"
    mailman-subscribe:    "|/usr/lib/mailman/mail/mailman subscribe mailman"
    mailman-unsubscribe:  "|/usr/lib/mailman/mail/mailman unsubscribe mailman"

.. code-block::

    [ESC]:wq!

Now, reset the aliases

.. code-block::

    sudo newaliases
    
Restart postfix

.. code-block::

    sudo /etc/init.d/postfix restart
    
And add the mailman to start with the system

.. code-block::

    sudo chkconfig --levels 235 mailman on

Start mailman and create a symbolic link inside cgi-bin

.. code-block::

    sudo /etc/init.d/mailman start
    cd /usr/lib/mailman/cgi-bin/
    sudo ln -s ./ mailman

Create a config file to mailman inside nginx

.. code-block::

    sudo vim /etc/nginx/conf.d/list.conf
    
.. code-block::

    server {
            server_name localhost;
            listen 8025;
    
            location /mailman/cgi-bin {
                   root /usr/lib;
                   fastcgi_split_path_info (^/mailman/cgi-bin/[^/]*)(.*)$;
                   include /etc/nginx/fastcgi_params;
                   fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                   fastcgi_param PATH_INFO $fastcgi_path_info;
                   fastcgi_param PATH_TRANSLATED $document_root$fastcgi_path_info;
                   fastcgi_intercept_errors on;
                   fastcgi_pass unix:/var/run/fcgiwrap.socket;
            }
            location /images/mailman {
                   alias /usr/lib/mailman/icons;
            }
            location /pipermail {
                   alias /var/lib/mailman/archives/public;
                   autoindex on;
            }
    }

.. code-block::

    [ESC]:wq!

Restart nginx to update the new configuration

.. code-block::

    sudo service nginx restart

Edit the config script of mailman, to fix the url used by it.

.. code-block::

    sudo vim /etc/mailman/mm_cfg.py

Add this line in the end of file

.. code-block::

    DEFAULT_URL_PATTERN = 'https://%s/mailman/cgi-bin/'
    
.. code-block::

    [ESC]:wq!
    
Run the fix_url and restart mailman.
    
.. code-block::

    sudo /usr/lib/mailman/bin/withlist -l -a -r fix_url
    sudo service mailman restart

Giving the rights permissions to fcgi

Add nginx to the apache's user group (create by mailman), to grant all the right permissions to spawn-fcgi

.. code-block::

    sudo usermod -a -G apache nginx
    
Put spaw-fcgi to start with the system, and start it

.. code-block::

    sudo chkconfig --levels 235 spawn-fcgi on
    sudo /etc/init.d/spawn-fcgi start

Restart the services

.. code-block::

    sudo service mailman restart
    sudo service nginx restart

*NOTE:*

    You can access mailman in this url: `http://localhost:8025/mailman/cgi-bin/listinfo <http://localhost:8025/mailman/cgi-bin/listinfo>`_ 

