import jenkins

server = jenkins.Jenkins('http://192.168.4.208:8080/', username="abrusco", password="8A6b7eV2")
server.build_job('test')
