# Configure Nginx to have a custom HTTP response header

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'Add X-Served-By header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => "add_header X-Served-By ${::hostname};",
  notify => Service['nginx'],
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  require    => Package['nginx'],
  subscribe  => File_line['Add X-Served-By header'],
}
