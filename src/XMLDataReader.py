# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from Types import DataType
from DataReader import DataReader


class XMLDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()

        for student in root:
            studentName = student.tag.strip()
            self.students[studentName] = []

            for subject in student:
                subjectName = subject.tag.strip()
                subjectScore = int(subject.text.strip())
                self.students[studentName].append((
                    subjectName,
                    subjectScore)
                )

        return self.students