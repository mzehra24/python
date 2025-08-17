temp=None
head=None
data=None
def insertNodeAtTail(head, data):
    new_node=SinglyLinkedListNode(data)
    if head is None:
        return new_node

    # Store the head reference in a temporary variable
    last = head

    # Traverse till the last node
    while last.next:
        last = last.next

    # Change the next pointer of the last 
    # node to point to the new node
    last.next = new_node

    # Return the head of the list
    return head

    
    
    return new_node
