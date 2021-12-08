package com.company;

public class Electr {

    private double countLength(int catheti1, int catheti2) {
        return Math.sqrt(Math.pow(catheti1, 2) + Math.pow(catheti2, 2));
    }

    public double countMaxLength(int distance, int[] heights) {
        double maxLength = 0.0;

        for (int i = 0; i < heights.length - 1; i+=1) {
            for (int j = i + 1; j <= i + 1; j++) {
                int catheti;
                if (heights[i] >= heights[j]) {
                    catheti = heights[i] - heights[j];
                    maxLength += countLength(distance, catheti);
                } else {
                    catheti = heights[j] - heights[i];
                    maxLength += countLength(distance, catheti);
                }
            }
        }
        double scale = Math.pow(10, 2);
        maxLength = Math.round(maxLength * scale) / scale;
        System.out.println(maxLength);
        return maxLength;
    }

    public static void main(String[] args) {
        int [] heights = {100, 2, 100, 2, 100};
        int length = 4;

        Electr electr = new Electr();
        electr.countMaxLength(length, heights);

    }
}