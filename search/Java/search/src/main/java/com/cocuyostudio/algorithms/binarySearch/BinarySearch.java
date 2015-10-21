package com.cocuyostudio.algorithms.binarySearch;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

/**
 * Created by robertorojas on 10/20/15.
 */
public class BinarySearch {

    // Brute force
    private boolean contains(Integer[] collection, Integer target) {

        for (int idx =0; idx < collection.length; idx++) {
            if (collection[idx].equals(target)) {
                return true;
            }
        }

        return false;
    }

    private boolean binarySearchContains(Integer[] ordered, Integer target) {

        int low = 0;
        int high = ordered.length - 1;

        while (low <= high) {
            int mid = (low + high) / 2;

            int comparedRet = target.compareTo(ordered[mid]);
            if (comparedRet == 0) {
                return true;
            } else if (comparedRet < 0) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return false;
    }

    /*
        Determine execution performance of contains
    */
    public void performance() {
        int n = 1024;
        int lastNumber = 50000000;

        for (int idx = n; idx <= lastNumber; idx *=2) {

            List<Integer> numbers = new ArrayList<Integer>(idx);

            for (int numCount = 0; numCount <= idx; numCount++) {
                numbers.indexOf(numCount);
            }
            Integer[] ints = numbers.toArray(new Integer[]{});

            long start = System.nanoTime();
            boolean ret = false;
            //ret = contains(ints, -1);
            ret = binarySearchContains(ints, -1);
            long done = System.nanoTime();
            System.out.println(ret + " " + idx + " - " + TimeUnit.NANOSECONDS.toNanos((done - start)));

        }
    }


    public static void main( String[] args ) {
        new BinarySearch().performance();
    }

}
