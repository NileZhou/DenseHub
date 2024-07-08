package hot;// Monotone Stack--Dynamic Programming--Math
// 代码力不够强，未快速实现单调栈

// 题目
// https://leetcode-cn.com/problems/trapping-rain-water/


// 最先想到的是单调栈解法
// 关键之处是想出单调栈的逻辑: 从左到右存的是在height[]里的下标值，高度由大到小, 下标值也由小到大
// 这是计算行的雨水
// 时间复杂度O(n), 空间复杂度O(k) k可能为n
public class TrappingRainWater {
    public int trap(int[] height) {
        int n = height.length;
        if (n < 3) return 0;
        int[] st = new int[1000];
        int right = -1, mid, ans = 0;
        st[++right] = 0;
        for (int i=1; i<n; ++i) {
            while (right > -1 && height[i] > height[st[right]]) {
                // 对凹槽的处理
                mid = height[st[right--]];
                if (right > -1) ans += (Math.min(height[i], height[st[right]]) - mid) * (i - st[right] - 1);
            }
            if (right == -1 || height[st[right]] > height[i]) st[++right] = i;
            if (height[st[right]] == height[i]) st[right] = i;
        }

        return ans;
    }
}


// 计算列的雨水
// 对于每一列存的雨水，是{左边最大值，右边最大值}的最小值减去当前高度
// 所以可以用动态规划
// 时间复杂度O(n), 空间复杂度O(n)
class Solution2 {
    public int trap(int[] height) {
        int n = height.length;
        if (n < 3) return 0;
        int[] leftMax = new int[n], rightMax = new int[n];
        leftMax[0] = height[0];
        rightMax[n-1] = height[n-1];
        for (int i=1; i<n; ++i) {
            leftMax[i] = Math.max(leftMax[i-1], height[i]);
        }
        for (int i=n-2; i>=0; --i) {
            rightMax[i] = Math.max(rightMax[i+1], height[i]);
        }
        int ans = 0, h;
        for (int i=1; i<n-1; ++i) {
            h = Math.min(leftMax[i-1], rightMax[i+1]);
            if (h > height[i]) ans += h - height[i];
        }

        return ans;
    }
}

// 数学角度思考什么是积雨水: 


