// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import "../src/ReversibleFT.sol";

contract CounterTest is Test {
    ReversibleFT public reversibleFT;

    function setUp() public {
        reversibleFT = new ReversibleFT();
        reversibleFT.balanceOfDeposit();
    }

    // function testIncrement() public {
    //     reversibleFT.increment();
    //     assertEq(reversibleFT.number(), 1);
    // }

    // function testSetNumber(uint256 x) public {
    //     reversibleFT.setNumber(x);
    //     assertEq(reversibleFT.number(), x);
    // }
}
