# 12. Integer to Roman

Roman numerals are represented by seven different symbols: <code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.

<pre>
<b>Symbol</b>   <b>Value</b>
I           1
V           5
X           10
L           50
C           100
D           500
M           1000
</pre>
For example, <code>2</code> is written as <code>II</code> in Roman numeral, just two one's added together. <code>12</code> is written as <code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:

- <code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.
- <code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.
- <code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

## Example 1

    Input: num = 3
    Output: "III"
    Explanation: 3 is represented as 3 ones.

## Example 2

    Input: num = 58
    Output: "LVIII"
    Explanation: L = 50, V = 5, III = 3.

## Constraints

- <code> 1 <= num <= 3999 </code>
