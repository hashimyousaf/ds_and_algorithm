
class Solution(object):
   def minMeetingRooms(self, intervals):
       """
       :type intervals: List[List[int]]
       :rtype: int
       """
       # first sort meeting by their stating time.
       # then loop through number of meetings you are going to deal with
       #  Again loop thorugh the number of meetings if there is any already used meeting room which we got free or you gonna assign new room.
       # Check if current meeting start time >= to any previous ongoing meeting no need to increase counter Just override meeting room value
       # Increase counter and assign a new room

       start_time = 0
       end_time = 1
       intervals.sort()
       counter = 0
       meeting_room_dict = {}
       for meeting in intervals:
           if not meeting_room_dict:
               # This is the case to execute only for the first iteration. It will never execute again.
               counter += 1
               meeting_room_dict[counter] = meeting

           else:
               assign_new_room = False
               dict_to_iterate = meeting_room_dict.copy()
               for meeting_room_number, meeting_room_val in dict_to_iterate.items():
                   if meeting[start_time] >= meeting_room_val[end_time]:
                       meeting_room_dict[meeting_room_number] = meeting
                       assign_new_room = False
                       break
                   else:
                       assign_new_room = True
               if assign_new_room:
                   counter += 1
                   meeting_room_dict[counter] = meeting
       return counter

print(Solution().minMeetingRooms([[1,10],[2,7],[3,19],[8,12], [10,20], [11,30]]))