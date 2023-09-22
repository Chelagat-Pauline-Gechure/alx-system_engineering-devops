#How to create a manifest that kills a process named killmenow

exec { 'kill_process':
  path    => '/usr/bin/',
  command => 'pkill killmenow',
  returns => [0, 1]
}
