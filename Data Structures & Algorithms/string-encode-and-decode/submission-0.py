class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ''
        for i in range(len(strs)):
            for char in strs[i]:
                encode_str += str(ord(char)) + ' '
            encode_str += '- '
        # print(encode_str)
        return encode_str

    def decode(self, s: str) -> List[str]:
        decode_list = s.split()
        ret_list = []
        current_str = ''
        for item in decode_list:
            if item != '-':
                current_str += chr(int(item))
            else:
                # print(current_str)
                ret_list.append(current_str)
                current_str = ''
        # print(ret_list)
        return(ret_list)

