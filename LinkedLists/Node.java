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

    static Node deleteNode(Node head, int d){
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

    static void printLL(Node head){
        while(head != null){
            System.out.print(head.data + ", ");
            head = head.next;
        }
    }

    //2.1 page 94 Linked Lists question
    static Node remoteDuplicate(Node head){
        if(head == null) return null;
        Node currentFast = head;
        Node currentSlow = head;
        while(currentSlow.next != null){
            if(currentFast.next == null){
                currentSlow = currentSlow.next;
                currentFast = currentSlow.next;
            }
            else currentFast = currentFast.next;
            if(currentFast.data == currentSlow.data){ //if duplicate value
                //remote item
                deleteNode(head, currentFast.data);
            }
        }
        return head;
    }
        
    public static void main(String[] args){
        Node example = new Node(2);
        example.appendtoTail(1);
        example.appendtoTail(4);
        example.appendtoTail(1);
        printLL(example);

    }
}