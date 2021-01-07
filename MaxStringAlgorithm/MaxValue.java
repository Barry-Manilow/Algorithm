/**
 * @author lianying
 * @create 2021-01-04 9:27 下午
 **/


/**
 * 一、算法优化说明：
 *     主要优化了原先算法中先根据字符串长度排序，长度相等时根据拼接值大小进行排序的逻辑。取出n个字符串后仍采用按拼接值排序的方式。
 *
 * 二、具体实现逻辑：
 *    1、当数组为空或取出字符串数量n<=0时返回空
 *    2、当数组数量为1时返回仅有的一个元素
 *    3、当取出字符串数量n >= 数组大小nums_size 时，直接对数组中所有字符串按拼接值大小进行排序
 *    4、当取出字符串数量 0 < n < 数组大小nums_size 时,根据木桶原理将数组中字符串按长度进行分类
 *       4.1  n <= nums_size/2 时，将木桶按高度降序排序，从最高的桶开始取字符串，一直取到字符串数量满足n为止，将取出的字符串按拼接值排序
 *       4.2  n > nums_size/2 时，将木桶按高度升序排序，从最矮的桶开始剔除符串，一直剔除到剩余字符串数量满足n为止，将剩余的字符串按拼接值排序
 *    e.g：nums=["53213","68","49","9","10","33","3","30","333"]，按长度分类后的结果如下：
 *         长度为 1 的数字字符串列表：[9, 3]
 *         长度为 2 的数字字符串列表：[68, 49, 10, 33, 30]
 *         长度为 3 的数字字符串列表：[333]
 *         长度为 5 的数字字符串列表：[53213]
 *        当 n=3时，小于数组长度的一半（9/2=4），因此从长度为5的字符串桶开始取，长度为5、3的字符串桶全部取出，长度为2的字符串桶取出值最大，取出的字符串为[53213, 333, 68]
 *        当 n=6时，大于数组长度的一半（9/2=4），因此从长度为1的字符串桶开始剔除，长度为1的字符串桶全部剔除，长度为2的桶剔除1个元素，剔除后剩余字符串为[68, 49, 33, 30, 333, 53213]
 *
 * 二、算法复杂度分析：
 *    1、时间复杂度
 *       原算法使用按长度排序长度相等按拼接值排序的算法逻辑，时间复杂度大于O(nlogn)（程序语言内置的TimSort算法的复杂度）
 *       优化后的算法先按长度分类，并将分类结果排序。由于循环一遍数组的复杂度为O(n)，对长度分类进行排序时，长度分类的种类数远小于数组的长度，
 *       且只需要对需要拆分的桶进行拼接值排序，因此优化效果较为明显。
 *       几种特殊情况分析：
 *       e.g.1：每种长度的字符串只有一个时，时间复杂度较高，但nums_size很大时实际不会出现这种情况
 *       e.g.2：当大部分字符串集中分布于待拆分的桶中时，比如上述例子中，长度为2的桶就是待拆分的桶（部分删除，部分取出），此时仍然需要将桶内的字符串进行排序，
 *              但由于TimSort排序算法中会先扫描一遍数组取出严格单调下降和严格单调上升的片段后再进行排序，所以如果在这个步骤中对桶中的字符串进行排序，后面再
 *              根据拼接值进行排序时不会重复对已经排过序的片段进行排序，所以即使这块排了一次序也不会导致时间复杂度上升
 *    2、空间复杂度
 *       使用HashMap结构存储按长度分类后的字符串，增加了内存开销
 **/



import java.util.*;


public class MaxValue {
    public static void main(String[] args) {
        
        // 初始输入数组
        ArrayList<String> nums = new ArrayList<>();
        nums.add("53213");
        nums.add("49");
        nums.add("9");
        nums.add("10");
        nums.add("33");
        nums.add("68");
        nums.add("3");
        nums.add("30");
        nums.add("330");
        nums.add("890");
        nums.add("333");
        // 取几个进行拼接
        Integer n = 5;

        String maxStr = getMaxStr(nums, n);
        System.out.format("%d个字符串拼接的最大值是：%s",n,maxStr);
    }

    private static String getMaxStr(ArrayList<String> nums, Integer n){
        Integer nums_size = nums.size();

        //1.如果为空返回""
        if(nums.isEmpty() || n <= 0){
            return "";
        }

        //2.如果只有1个元素也直接返回
        if(nums_size == 1){
            return nums.get(0);
        }

        //3.如果需要取出来的字符串数量n大于等于数组长度相同，直接按拼接值进行排序
        if(nums_size <= n){
            Collections.sort(nums, new LargerNumberComparator());
            String MaxStr = String.join("", nums);

            return MaxStr;
        }
        //4.如果n小于数组大小，根据木桶原理将字符串按长度存储在不同的桶中，然后分成两种情况
        //1）n <= nums_size/2:从较高的桶开始取字符串，一直取到字符串数量为n
        //2）n > nums_size/2:从较矮的桶开始剔除符串，一直剔除到剩余字符串数量为n

        //首先将不同长度的字符串按长度分类，以hashmap结构存储，key为当前桶的字符串长度，value为当前桶中的字符串
        HashMap<Integer, ArrayList<String>> hm = new HashMap<>();
        int cur_num_length = 0;
        for (String num: nums){
            cur_num_length = Integer.valueOf(num.length()).intValue();
            Set<Integer> set = hm.keySet();
            ArrayList<String> al;
            //如果已包含该长度的字符串则把原来的ArrayList取出来
            if(set.contains(cur_num_length)){
                al = hm.get(cur_num_length);
            }
            //如果还未包含当前长度的字符串，则新建ArrayList
            else{
                al = new ArrayList();
            }
            al.add(num);
            hm.put(cur_num_length, al);
        }
        //打印查看按长度分类是否正确
        Set<Integer> set = hm.keySet();
        System.out.printf("将原数组按字符串长度分类：\n");
        for(Integer i:set){
            System.out.printf("长度为 %d 的数字字符串列表：%s\n",i,hm.get(i));
        }
        ArrayList<String> res = new ArrayList<>();

        //4.如果需要取出来的字符串数量n小于数组长度的一半，，循环取出最长的n个字符串后按拼接值进行排序
        if(n <= nums_size/2){
            //从字符串长度最大的那个ArrayList开始提取，一直提取到字符串数量为n时为止
            Set<Integer> sortSet = new TreeSet<>((o1, o2) -> o2.compareTo(o1));
            sortSet.addAll(set);
            while(true){
                if(res.size() >= n){
                    break;
                }
                Integer max = sortSet.iterator().next();
                ArrayList cur_list = hm.get(max);
                //如果当前桶的字符串数量 <= 还需要的字符串数量，则全部提取
                if(cur_list.size() <= n-res.size()){
                    res.addAll(cur_list);
                }
                //如果当前桶的字符串数量 > 还需要的字符串数量，则先按拼接值大小进行排序后，取出所需要的数量
                else{
                    Collections.sort(cur_list, new LargerNumberComparator());
                    List sub_list = cur_list.subList(0, n-res.size());
                    res.addAll(sub_list);
                }
                sortSet.remove(max);
            }
        }
        //5.如果需要取出来的字符串数量n大于数组长度的一半，剔除最短的nums_size-n的几个字符串后，按拼接值进行排序
        else{
            Integer need_del_total = nums_size - n;//需要剔除的字符串总数量
            Integer already_del_num = 0;//已经剔除的字符串数量
            Integer remainder_del_num = 0;//还需要剔除的字符串数量

            //将桶按高度正序排序
            Set<Integer> sortSet = new TreeSet<>((o1, o2) -> o1.compareTo(o2));
            sortSet.addAll(set);

            //从最矮的桶开始剔除字符串，一直剔除到剩余字符串数量为n时为止
            while(true){
                remainder_del_num = need_del_total - already_del_num;
                if(remainder_del_num == 0){
                    break;
                }
                Integer min = sortSet.iterator().next();
                ArrayList cur_list = hm.get(min);
                //如果当前桶的字符串数量小于等于剩余未删除数量则全部删除
                if(cur_list.size() <= remainder_del_num){
                    already_del_num += cur_list.size();
                    hm.remove(min);
                    sortSet.remove(min);
                }
                //如果当前桶的字符串数量大于剩余未删除数量，则将该桶内的字符串按拼接值排序后删除较小的
                else{
                    Collections.sort(cur_list, new LargerNumberComparator());
                    List sub_list = cur_list.subList(cur_list.size()-remainder_del_num, cur_list.size());
                    already_del_num += remainder_del_num;
                    cur_list.removeAll(sub_list);
                    hm.replace(min, cur_list);
                }
            }
            for(Integer key:hm.keySet()){
                res.addAll(hm.get(key));
            }
        }

        //将最后取出的n个字符串按照拼接值大小进行排序
        System.out.format("最后取出的%d个字符串为：",n);
        System.out.println(res);
        Collections.sort(res, new LargerNumberComparator());
        String MaxStr = String.join("", res);
        return MaxStr;
    }

    private static class LargerNumberComparator implements Comparator<String> {
        @Override
        public int compare(String a, String b) {
            String order1 = a + b;
            String order2 = b + a;
            return order2.compareTo(order1);
        }
    }
}
