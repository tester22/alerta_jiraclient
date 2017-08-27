Jira Integration Plugin
=============

Send acknowledgmented alerts to an Jira Project.

For help, join [![Gitter chat](https://badges.gitter.im/alerta/chat.png)](https://gitter.im/alerta/chat)

Installation
------------

Clone the GitHub repo and run:

    $ python setup.py install

Or, to install remotely from GitHub run:

    $ pip install git+https://github.com/alerta/alerta-contrib.git#subdirectory=plugins/jiraclient

Note: If Alerta is installed in a python virtual environment then plugins
need to be installed into the same environment for Alerta to dynamically
discover them.

Configuration
-------------

Add `jiraclient` to the list of enabled `PLUGINS` in `alertad.conf` server
configuration file and set plugin-specific variables either in the
server configuration file or as environment variables.

```python
PLUGINS = ['jiraclient']
JIRA_API_URL = ''
JIRA_API_USERNAME = ''
JIRA_API_PASSWORD = ''
JIRA_PROJECT_KEY = ''
JIRA_ISSUE_TYPE = '' # Default 'Bug'
```

Troubleshooting
---------------

Restart Alerta API and confirm that the plugin has been loaded and enabled.

Set `DEBUG=True` in the `alertad.conf` configuration file and look for log
entries similar to below:

References
----------


License
-------

Copyright (c) 2017 Anton Delitsch. Available under the MIT License.