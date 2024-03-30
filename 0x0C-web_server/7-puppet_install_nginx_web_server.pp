# install nginx
package { 'nginx':
  ensure => installed,
}

# Custom index file
file { '/var/www/htm/index.html':
  ensure  => present,
  content => "Hello World!\n",
}

#configuring nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    listen 80;

    listen [::]:80;

    server_name _;

    root /var/www/html;

    location / {
	try_files $uri $uri/ =404;
    }

    location /redirect_me {
	return 301 'https://www.google.com';
    }
}
  ",
  require => Package['nginx'],
}

#remove default ngix webpage
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
}
