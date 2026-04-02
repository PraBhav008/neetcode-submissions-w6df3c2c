import json
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoder = json.dumps(strs)

        return encoder


    def decode(self, s: str) -> List[str]:
        decoder = json.loads(s)

        return decoder