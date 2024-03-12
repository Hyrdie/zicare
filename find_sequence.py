class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    
    return dummy.next

def find_sequence(data, seq):
    data_head = create_linked_list(data)
    seq_head = create_linked_list(seq)

    main_ptr = data_head
    while main_ptr:
        if main_ptr.val == seq_head.val:
            main_temp = main_ptr.next
            seq_temp = seq_head.next
            while seq_temp:
                if not main_temp or main_temp.val != seq_temp.val:
                    break
                main_temp = main_temp.next
                seq_temp = seq_temp.next
            if not seq_temp:
                return True
        main_ptr = main_ptr.next
    return False

data = [20, 7, 8, 10, 2, 5, 6]
seq1 = [7, 8]
seq2 = [8, 7]
seq3 = [7, 10]

print(find_sequence(data, seq1))  # true
print(find_sequence(data, seq2))  # false
print(find_sequence(data, seq3))  # false