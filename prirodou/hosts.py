from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'home.urls', name='www'),
    host(r'admin', 'admin.urls', name='admin'),
    host(r'system', 'system.urls', name='system'),
    host(r'data', 'data.urls', name='data'),
    host(r'rostliny', 'plants.urls', name='plants'),
)
