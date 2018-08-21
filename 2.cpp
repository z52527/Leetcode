/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int tmp1 = 0, tmp2 = 0, x = 1;
        ListNode *l3 = NULL, *head = NULL;
/*        while(l1 != NULL){
            tmp1 += (l1->val) * x;
            x *= 10;
            l1 = l1 -> next;
        }
        x = 1;
        while(l2 != NULL){
            tmp2 += (l2->val) * x;
            x *= 10;
            l2 = l2 -> next;
        }
        int tmp = tmp1 + tmp2, flag = 1;
*/
        while(l1||l2||tmp){
            if(l1){
                tmp += l1 -> val;
                l1 = l1 -> next;
            }
            if(l2){
                tmp += l2 -> val;
                l2 = l2 -> next;
            }
            if(l3) {
                l3->next = new ListNode(tmp%10);
                l3 = l3->next;
            }
            else {
                l3 = head = new ListNode(tmp%10);
            }
            tmp /= 10;
        }
        //printf("%d %d", tmp1, tmp2);
        return head;
    }
};