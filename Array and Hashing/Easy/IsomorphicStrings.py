class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for i, j in zip(s, t):
            d[j] = i
        unique_values_dict = {}

        updated_dict = {}
        
        # Removing Keys with the same values as other keys
        # Ex - {'b': 'f', 'a': 'o', 'r':'o'}
        for key, value in d.items():
            if value not in unique_values_dict:
                unique_values_dict[value] = key
                updated_dict[key] = value
            else:
                updated_dict[unique_values_dict[value]] = value
                
        Str = ""
        # Rebuilding the String with the mapping and checking if it matches
        for ch in t:
            if ch in updated_dict:
                Str += updated_dict[ch]
        if Str == s:
            return True
        else:
            return False