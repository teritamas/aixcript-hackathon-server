// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import "../src/ReversibleFT.sol";

contract ReversibleFTTest is Test {
    ReversibleFT public reversibleFT;

    function setUp() public {
        reversibleFT = new ReversibleFT();
    }

    // function testMintDeposit() public {
    //     reversibleFT.mintDeposit(address(this));
    //     uint256 balanceOf = reversibleFT.balanceOf(address(this));
    //     assertEq(balanceOf, 0);
    // }
}
