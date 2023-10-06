# Define a class for configuring the web server
class web_server {
  package { 'nginx':
    ensure => 'installed',
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
  }
}

# Define a class for configuring the web_static directory and serving the HTML
class web_static {
  file { '/data/web_static/shared':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases/test':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases/test/index.html':
    content => "<html>
<head>
  </head>
  <body>
    <h1>welcome</h1>
    <h3>I'm ayoub el gharbi from ALX Africa</h3>
  </body>
</html>",
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file_line { 'nginx_config':
    path   => '/etc/nginx/sites-available/default',
    line   => 'location /hbnb_static/ {',
    match  => '^.*location /hbnb_static/ {',
    ensure => present,
  }

  exec { 'nginx_restart':
    command     => 'service nginx restart',
    refreshonly => true,
    subscribe   => [File_line['nginx_config'], Service['nginx']],
  }
}

# Include the classes in your node definition
node 'your_node_name' {
  include web_server
  include web_static
}
