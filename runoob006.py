import paramiko

private_key_path = '/home/ejianlv/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(private_key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
ssh.connect('147.128.77.150', 22, 'ejianlv', "xxxxx")
stdin, stdout, stderr = ssh.exec_command('hostname')
stdin, stdout, stderr = ssh.exec_command('pwd')
print(stdout.read())