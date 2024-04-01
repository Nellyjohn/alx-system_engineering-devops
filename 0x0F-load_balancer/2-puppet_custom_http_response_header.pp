# automate the task of creating a custom HTTP header response, but with Puppet.

exec {'update_system':
  command => '/usr/bin/apt-get -y update',
}

package { 'nginx':
  ensure => 'installed',
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

file { '/var/www/html/index.html' :
  content => 'Hello World!',
}

file_line { 'Creating header':
  	ensure => present,
  	path   => '/etc/nginx/sites-available/default',
  	line   => "\tadd_header X-Served-By ${hostname};",
  	after  => 'server_name _;',
	require => Service['nginx'],
}
