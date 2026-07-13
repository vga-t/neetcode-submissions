class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        else:
            s_dict, t_dict = dict(), dict()
            for s_value, t_value in zip(s,t):
                if s_value in s_dict:
                    s_dict[s_value]+=1 
                else:
                    s_dict[s_value] = 1 
                if t_value in t_dict:
                    t_dict[t_value]+=1 
                else:
                    t_dict[t_value] = 1  
        return s_dict == t_dict
                 

        
