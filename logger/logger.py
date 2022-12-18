class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log_info_port(port,message):
	print(bcolors.OKGREEN + "%s | %s" % (port, message))

def log_warning_port(port,message):
	print(bcolors.WARNING + "%s | %s" % (port, message))

def log_fail_port(port,message):
	print(bcolors.FAIL + "%s | %s" % (port, message))

def log_info(message):
    print(bcolors.OKGREEN + "Info: %s" % message)

def log_warning(message):
    print(bcolors.WARNING + "Warning: %s" % message)

def log_fail(message):
    print(bcolors.FAIL + "Fail: %s" % message)