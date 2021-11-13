package com.example.pdapp

class User {
    var id: Int = 0
    var name: String = ""
    var username: String = ""
    var password: String = ""

    constructor(name:String, username:String, password:String) {
        this.name = name
        this.username = username
        this.password = password
    }

    constructor() {
    }

}