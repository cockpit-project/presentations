#!/usr/bin/python3
import os
import subprocess

my_dir = os.path.dirname(os.path.realpath(__file__))

fedsrv = subprocess.Popen(['bots/machine/testvm.py', 'fedora-38'],
                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
fedsrv_ssh = fedsrv.stdout.readline().strip().split()
_cockpit_url = fedsrv.stdout.readline().strip()
assert fedsrv.stdout.readline().strip() == 'RUNNING'
print(fedsrv_ssh)
subprocess.run(fedsrv_ssh + ['hostnamectl', 'set-hostname', 'fedsrv'])

c9s = subprocess.Popen(['bots/machine/testvm.py', 'centos-9-stream'],
                       stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
c9s_ssh = c9s.stdout.readline().strip().split()
_cockpit_url = c9s.stdout.readline().strip()
assert c9s.stdout.readline().strip() == 'RUNNING'
print(c9s_ssh)
subprocess.run(c9s_ssh + ['hostnamectl', 'set-hostname', 'c9s'])
subprocess.run(c9s_ssh + ['rpm', '-v', '-e', 'cockpit-bridge', 'cockpit-ws', 'cockpit-system', 'cockpit'])

# ssh config: fedsrv with user/pass, c9s cloud instance with key
with open('/tmp/testvms.config', 'w') as f:
    f.write(f'''Host fedsrv
        HostName 127.0.0.2
        User admin
        Port {fedsrv_ssh[4]}
        StrictHostKeyChecking no
        UserKnownHostsFile /dev/null
        IdentitiesOnly yes\n\n''')

    f.write(f'''Host c9s
        HostName 127.0.0.2
        User admin
        Port {c9s_ssh[4]}
        StrictHostKeyChecking no
        UserKnownHostsFile /dev/null
        IdentityFile {my_dir}/bots/machine/identity
        IdentitiesOnly yes
''')

# this must appear at the top to be effective
subprocess.run(['sed', '-i', '1 aInclude /tmp/testvms.config', os.path.expanduser('~/.ssh/config')])

input('Press Enter to stop VMs...')

subprocess.run(['sed', '-i', r'/Include .*\/testvms.config/d', os.path.expanduser('~/.ssh/config')])

fedsrv.stdin.close()
fedsrv.terminate()
c9s.stdin.close()
c9s.terminate()
fedsrv.wait()
c9s.wait()
