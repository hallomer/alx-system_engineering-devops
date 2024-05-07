# 7-puppet_install_nginx_web_server.pp
package { 'nginx':
  ensure => installed,
}

file { 'homepage':
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World!',
}

file_line { 'listen_on_port_80':
  path   => '/etc/nginx/sites-available/default',
  line   => 'listen 80;',
  match  => '^listen\s+80;',
  notify => Service['nginx'],
}

file_line { 'redirect_url':
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after  => 'server_name _;',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
