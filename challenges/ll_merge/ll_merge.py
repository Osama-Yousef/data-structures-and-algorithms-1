def merge_lists(self, list1, list2): 
        list1_current = list1.head
        list2_current = list2.head
  
        while list1_current and list2_current: 
  
            # Save next pointers 
            list1_next_ref = list1_current.next
            list2_next_ref = list2_current.next
  
            # make list2_current as next of list1_current 
            list2_current.next = list1_next_ref # change next pointer of list2_current 
            list1_current.next = list2_current # change next pointer of list1_current 
  
            # update current pointers for next iteration 
            list1_current = list1_next_ref 
            list2_current = list2_next_ref 
        # self.head = list2_current 
