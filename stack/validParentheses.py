class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        det_list = []
        char_list = list(s)
        while char_list:
            ch = char_list[0]
            det_list.append(ch)
            if(len(det_list) > 1):
                if (ch == ')') and (det_list[-2]=='('):
                    a = det_list[-2]
                    del det_list[-1]
                    del det_list[-1]
                if (ch == ']') and (det_list[-2]=='['):
                    a = det_list[-2]
                    del det_list[-1]
                    del det_list[-1]
                if (ch == '}') and (det_list[-2]=='{'):
                    a = det_list[-2]
                    del det_list[-1]
                    del det_list[-1]
            del char_list[0]
        if not det_list:
            return True
        else:
            return False
