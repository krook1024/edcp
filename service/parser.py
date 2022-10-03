from model.file import File


class Parser:
    def should_parse(self, file: File) -> bool:
        pass

    def parse_maps(self, file: File) -> File:
        pass
