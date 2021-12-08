package com.company;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ElectrTest {
    Electr electr = new Electr();
    @Test
    void testElectr() {
        int[] heights = {100, 2, 100, 2, 100};
        int length = 4;
        double expected = 392.33;

        assertEquals(expected, electr.countMaxLength(length, heights));
    }

    @Test
    void testElectr1() {
        int[] heights = {3, 1, 3};
        int length = 2;
        double expected = 5.66;

        assertEquals(expected, electr.countMaxLength(length, heights));
    }
}