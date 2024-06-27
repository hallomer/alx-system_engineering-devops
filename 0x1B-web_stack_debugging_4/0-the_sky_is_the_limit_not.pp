# This Puppet manifest adjusts the ulimit for Nginx workers to handle more open files.

$file_line { 'set-nginx-ulimit':
  path  => '/etc/default/nginx',
  line  => 'ULIMIT="-n 4096"',
  match => '^ULIMIT=',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure     => 'running',
  enable     => true,
  hasrestart => true,
  restart    => 'service nginx reload',
}
