// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Bank {
    
    mapping(address=>uint) private balances;
    
    function getBalance() public view returns (uint) {
        return balances[msg.sender];
    }

    function deposit(uint amount) public payable {
        // require(msg.value == amount);
        balances[msg.sender] += amount;
    }

    function withdraw(uint amount) public payable {
        require(amount <= balances[msg.sender]);
        balances[msg.sender] -= amount;
        // msg.sender.transfer(amount);
    }

}
