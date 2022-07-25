class RemoteCrashFetcher(Process):
    def __init__(self):
        super(RemoteCrashFetcher, self).__init__()

    def fetch_remote_crashes(self):
        try:
            client = SSHClient()
            #LOAD HOST KEYS
            #client.lo_host_keys('~/.ssh/known_hosts') 
            client.load_host_keys()
            client.load_system_host_keys()D
        except SSHException as sshException:
            print("Unable to establish SSH connection: %s" % sshException)
        except BadHostKeyException as badHostKeyException:
            print("Unable to verify server's host key: %s" % badHostKeyException)
        except AuthenticationException:
            print("Authentication failed, please verify your credentials: %s")
        finally:
            client.close()