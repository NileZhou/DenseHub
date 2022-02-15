package hot;// Brute Force--Greedy
// 代码逻辑错误，未能正确表达自己想法
// https://codeforces.com/contest/1491/problem/B

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;


public class MinimalCost {
    static StreamTokenizer st=new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    public static void solveB() {
        int n = nextInt(), v = nextInt(), h = nextInt();
        int[] obstacles = new int[n];
        for (int i=0; i<n; ++i) obstacles[i] = nextInt();
        // 错误代码
        // 错因: for循环里前一个if是到最后才能下结论, 是第二个if的特解，所以第二个if不能马上return
        // 启示: for循环的if里包含判断周期更长的特解，if的判断周期也应该变长
        // 父分支的判断周期应该>=子分支的判断周期
//        for (int i=1; i<n; ++i) {
//            if (Math.abs(obstacles[i] - obstacles[i-1]) > 1) {
//                System.out.println(0);
//                return;
//            }
//            if (obstacles[i] != obstacles[i-1]) {
//                System.out.println(Math.min(h, v));
//                return;
//            }
//        }
//        System.out.println(h + Math.min(h, v));

        // 正确代码
        boolean existDiff = false;
        for (int i=1; i<n; ++i) {
            if (obstacles[i] != obstacles[i-1]) {
                if (Math.abs(obstacles[i] - obstacles[i-1]) > 1) {
                    System.out.println(0);
                    return;
                }
                existDiff = true;
            }
        }
        if (existDiff) System.out.println(Math.min(h, v));
        else System.out.println(h + Math.min(h, v));
    }

    public static void main(String[] args) {
        int t = nextInt();
        while (t-- > 0) {
            solveB();
        }
    }

    static int nextInt() {
        try{
            st.nextToken();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return (int) st.nval;
    }
}
