import json
from typing import List
from PyPDF2 import PdfReader


class File:
    id: int | None
    path: str
    title: str
    page: int

    def __init__(self, data: dict):
        self.id = data["id"]
        self.path = data["path"]
        self.title = data["title"]
        self.page = data["page"]


class Config:
    destination: str
    language: str
    total: int
    files: List[File]

    def __init__(self, filepath: str):
        file = open(filepath, "r", encoding='utf-8')
        data_dict = json.load(file)
        file.close()
        self.destination = data_dict["destination"]
        self.total = data_dict["total"]
        self.language = data_dict["language"]
        self.files = []
        for file in data_dict["files"]:
            self.files.append(File(file))
