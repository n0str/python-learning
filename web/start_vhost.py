import sys
import os

if len(sys.argv) < 2:
    print "Usage error"
    exit()

template = []

path = sys.argv[1]

template.append("<VirtualHost *:80>\n")
template.append("   ServerName " + path + "\n")
template.append("   DocumentRoot /var/www/" + path + "/public\n")
template.append('''
    <Directory />
        Options FollowSymLinks
        AllowOverride None
    </Directory>\n
''')
template.append("   <Directory /var/www/" + path + ">\n")
template.append('''     Options Indexes FollowSymLinks MultiViews
        AllowOverride ALL
        Order allow,deny
        allow from all
    </Directory>
</VirtualHost>
''')

print "Created file /etc/apache2/sites-available/" + path + ".conf"

f = open("/etc/apache2/sites-available/" + path + ".conf", "w")
f.write(''.join(template))
f.close()

print "mkdir -p " + path + "/public"

os.system("mkdir -p " + path + "/public")

f = open(path + "/public/index.html","w")
f.write("Created")
f.close()

os.system("a2ensite "+path)
os.system("echo '\n127.0.0.1   " + path + "\n' >> /etc/hosts")
os.system("service apache2 reload")
os.system("chmod 777 "+path)
os.system("chown nostr:nostr "+path)