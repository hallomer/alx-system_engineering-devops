# Creating a custom HTTP header response, but with Puppet.

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
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => "        add_header X-Served-By ${::hostname};",
  notify => Service['nginx']
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
