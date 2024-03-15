class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # greedy approach
        str_time = sorted([(trip[1], trip[0]) for trip in trips])

        end_time = sorted([(trip[2], trip[0]) for trip in trips])
        s=0
        e=0
        p=0
        while (s<len(trips) and e<len(trips)):

            if str_time[s][0]<end_time[e][0]:
                p+=str_time[s][1]
                if p>capacity:
                    return False
                s+=1
            else:
                p-=end_time[e][1]
                e+=1
        return True
        # or


        # trip = [0]*1001
        # for numpassengers,fromi,to in trips:
        #     for i in range(fromi, to):
        #         trip[i]+=numpassengers
        #         if trip[i]>capacity:
        #             return False
        # return True


        

        