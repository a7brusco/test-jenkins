import os
import sys

import jenkins

sys.path.append(os.path.join(os.path.dirname(__file__), "common", ""))

from credentials import get_jenkins_credentials

if __name__ == "__main__":
    login, password = get_jenkins_credentials()
    server = jenkins.Jenkins(
        os.environ['JENKINS_URL'], username=login, password=password
    )
    server.build_job("test")
