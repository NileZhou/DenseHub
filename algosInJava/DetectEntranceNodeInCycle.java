package hot;

/**
 * https://leetcode-cn.com/problems/linked-list-cycle-ii/
 * Definition for singly-linked list.
 * class hot.ListNode {
 *     int val;
 *     hot.ListNode next;
 *     hot.ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class DetectEntranceNodeInCycle {
    public ListNode detectCycle(ListNode head) {
        if (head == null) return null;
        ListNode fast = head.next, slow = head;
        while (fast != null) {
            if (slow == fast) break;
            slow = slow.next;
            if (fast.next == null) return null;
            fast = fast.next.next;
        }
        if (fast == null) return null; // 必须要这一行
        fast = head; slow = slow.next;
        while (fast != slow) {
            fast = fast.next;
            slow = slow.next;
        }
        return slow;
    }
}
