# kills a process named killmenow
exec { 'kill':
  command  => 'pkill -9 -f killmenow',
  path	=> ['/usr/bin', '/usr/sbin', '/bin']
}
