// https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] arr = s.toCharArray();
        int n = arr.length, ans = 0;
        if (n < 2) return n;
        Map<Character, Integer> map = new HashMap<>();
        for (int i=0, j=0; i<n; ++i) {
            if (map.containsKey(arr[i])) {
                j = Math.max(j, map.get(arr[i]) + 1); // 注意: 这里必须保证j的单调性
            }
            map.put(arr[i], i);
            ans = Math.max(i - j + 1, ans);
        }

        return ans;
    }
}
