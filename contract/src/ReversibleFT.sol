// SPDX-License-Identifier: MIT

pragma solidity ^0.8.14;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ReversibleFT is ERC20, Ownable {
    uint256 private constant depositAmmount = 50 * 1000;

    /**
     * URI設定時に誰がどのtokenIdに何のURIを設定したか記録する
     */

    event TokenMint(address indexed sender, uint256 indexed ammount);

    constructor() ERC20("ReversibleFT", "RVSFT") {
        // はじめにオーナーにトークンを発行する
        mint(msg.sender, depositAmmount);
    }

    /**
     * 指定したアドレスにトークンを発行
     */
    function mint(address senderAddress, uint256 amount) private onlyOwner {
        _mint(senderAddress, amount);
        emit TokenMint(senderAddress, amount);
    }

    /**
     * 指定したアドレスのトークンを焼却
     */
    function burn(address senderAddress, uint256 amount) public onlyOwner {
        _burn(senderAddress, amount);
    }

    /**
     * 売買の仲介
     */
    function brokerage(address from, address to, uint256 amount) public onlyOwner {
        _burn(from, amount);

        // プラットフォーム運営者の報酬分
        uint256 revenue = amount * 10 / 100;
        mint(msg.sender, revenue);

        // 販売者に還元
        mint(to, amount - revenue);
    }

    /**
     * @dev
     * テスト用に指定したアドレスにトークンを発行
     */
    function mintDeposit(address targetAddress) public {
        mint(targetAddress, depositAmmount);
    }
}
