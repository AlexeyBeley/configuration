from enum import Enum
from loggin import get_logger
from grade_configuration import GradeConfiguration

logger = get_logger()


class InfrastructureConfiguration(GradeConfiguration):
    def __init__(self):
        self._jenkins_host_name = None

    @property
    def corporate_dns_extension(self):
        return "fun-horey"

    @corporate_dns_extension.setter
    def corporate_dns_extension(self, _):
        raise ValueError("Static value")

    @property
    def dns_grade_extension(self):
        if self.grade == self.Grade.GradeValue.PROD:
            raise RuntimeError("No grade extension for prod")
        return self.grade.lower()

    @dns_grade_extension.setter
    def dns_grade_extension(self, _):
        raise ValueError("Static value")

    @property
    def jenkins_host_name(self):
        if self.grade != self.Grade.GradeValue.PROD:
            return f"jenkins.{self.dns_grade_extension}.{self.corporate_dns_extension}.com"

        return f"jenkins.{self.corporate_dns_extension}.com"

    @jenkins_host_name.setter
    def jenkins_host_name(self, value):
        if self.grade > self.GradeValue.QA:
            raise ValueError(value)

        logger.info(f"Setting jenkins_host_name value: '{value}' ")
        self._jenkins_host_name = value
