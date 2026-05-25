class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        output = []

        for i in strs:
            ana_dict={}
            for j in i:
                ana_dict[j]=ana_dict.get(j,0)+1
            anagrams.append(ana_dict)

        done_list=[]
        for i in range(0,len(anagrams)):
            lst = []
            if i not in done_list:
                lst.append(strs[i])
                for j in range(i+1,len(strs)):
                    if anagrams[i]==anagrams[j] and j not in done_list:
                        lst.append(strs[j])
                        done_list.append(j)
            if len(lst)>0:
                output.append(lst)

        return output