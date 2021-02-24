class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
   
    #TC - nlogn
    #Sc - O(1)
        
        intervals.sort(key=lambda x:x[0])
        for i in range(len(intervals)-1):
            if intervals[i+1][0] < intervals[i][1]:
                return False
            else:
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
        
        return True
        
#SOlution 2 - EASIERRR
        intervals.sort()
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
            
        return True
