#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SumoSurvey.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    # additional process for creation additional user, misc data, and anything
    for arg in sys.argv:
        # if syncdb occurs and users don't exist, create them
        if arg.lower() == 'syncdb':
            print 'syncdb post process...'
            from django.contrib.auth.models import User

            admin_id = 'root'
            admin_email = ''
            admin_password = 'root'

            # admin exists?
            user_list = User.objects.filter(username=admin_id)
            if len(user_list) == 0: 
                print 'create superuser: ' + admin_id
                new_admin = User.objects.create_superuser(admin_id, admin_email, admin_password)
