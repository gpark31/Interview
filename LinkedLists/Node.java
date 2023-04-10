package LinkedLists;

class Node{
    Node next = null;
    int data;

    public Node(int d){
        data = d;
    }

    void appendtoTail(int d){
        Node end = new Node(d);
        Node n = this;
        while (n.next != null){
            n = n.next;
        }
        n.next = end;
    }

    Node deleteNode(Node head, int d){
        if (head == null) return null;
        Node n = head;
        if (n.data == d){
            return head.next;
        }
        while (n.next != null){
            if (n.next.data == d){
                n.next = n.next.next;
                return head;
            }
            n.next = n.next.next;
        }
        return head;
    }
        

}