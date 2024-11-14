/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    while (b != 0) {
        let carry = (a & b) << 1
        a ^= b;
        b = carry;
    }
    return a
};