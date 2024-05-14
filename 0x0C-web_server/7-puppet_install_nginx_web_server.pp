# Configures an Nginx server using Puppet
package { 'nginx':
  ensure => installed,
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https:\/\/www.youtube.com\/watch?v=Htqn7tGvQsc permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'Add X-Served-By header':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  line   => 'add_header X-Served-By $HOSTNAME;',
  after  => 'server_name _',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
