import jenkins

server = jenkins.Jenkins('http://192.168.4.208:8080/', username="dna_nni_user", password="7YxBfy3TSh4rqxrD5Im4")
server.build_job('test')

# import os
# import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), "TwoNotesEcosystemPyTools", "src", "modules", ""))

# from tools.email import Mailer

# with Mailer() as mailer:
#     mailer.send('developper@orosys.fr', ['antoine.brusco@orosys.fr'], 'test', 'test')
