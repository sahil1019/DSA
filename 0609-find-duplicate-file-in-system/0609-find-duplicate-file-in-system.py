class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = {}

        for path in paths:
            parts = path.split()
            root = parts[0]

            for file in parts[1:]:
                name, content = file.split('(')
                content = content[:-1]

                full_path = root + '/' + name
                files.setdefault(content, []).append(full_path)

        return [v for v in files.values() if len(v) > 1]