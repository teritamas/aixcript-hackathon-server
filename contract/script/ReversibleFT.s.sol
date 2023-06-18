// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Script.sol";
import {ReversibleFT} from "../src/ReversibleFT.sol";

contract Deploy is Script {
    address internal deployer;
    ReversibleFT internal reversibleFT;

    function setUp() public virtual {
        (deployer,) = deriveRememberKey(vm.envString("MNEMONIC"), 0);
    }

    function run() public {
        vm.startBroadcast(deployer);
        reversibleFT = new ReversibleFT();
        vm.stopBroadcast();
    }
}
