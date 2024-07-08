package hot;

/**
 * https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
 */

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class ReverseNodesInKGroup {
    private ListNode reverse(ListNode head) {
        ListNode dummy = new ListNode(), p = head, pnext;
        while (p != null) {
            pnext = p.next;
            p.next = dummy.next;
            dummy.next = p;
            p = pnext;
        }

        return dummy.next;
    }

    public ListNode reverseKGroup(ListNode head, int k) {
        if (k < 2 || head == null) return head;
        ListNode p = head, pright;
        for (int i=0; i<k-1; ++i) {
            p = p.next;
            if (p == null) return head;
        }
        pright = p.next;
        p.next = null;
        head = reverse(head);
        for (int i=0, p=head; i<k-1; ++i) p = p.next;
        p.next = reverseKGroup(pright, k);

        return head;
    }
}
