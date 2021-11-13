package com.example.pdapp


import android.content.ContentValues
import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper
import android.widget.Toast

val DATABASE_NAME = "MyDB"
val TABLE_NAME = "Users"
val COL_ID = "id"
val COL_NAME = "name"
val COL_USERNAME = "username"
val COL_PASSWORD = "password"

class DatabaseHandler(var context: Context) : SQLiteOpenHelper(context, DATABASE_NAME,null,1) {
    override fun onCreate(db: SQLiteDatabase?) {
        val createTable = "CREATE TABLE " + TABLE_NAME + " (" +
                COL_ID + " INTEGER PRIMARY KEY AUTOINCREMENT," +
                COL_NAME + " VARCHAR(256), " +
                COL_USERNAME + " VARCHAR(256), " +
                COL_PASSWORD + " VARCHAR(256))";

        db?.execSQL(createTable)
    }

    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
        TODO("Not yet implemented")
    }

    fun InsertData(user : User) {
        val db = this.writableDatabase
        var cv = ContentValues()
        cv.put(COL_NAME,user.name)
        cv.put(COL_USERNAME,user.username)
        cv.put(COL_PASSWORD,user.password)
        var result = db.insert(TABLE_NAME,null,cv)
        if (result == -1.toLong())
            Toast.makeText(context, "Registration Failed", Toast.LENGTH_SHORT).show()
        else
            Toast.makeText(context, "Registration Success", Toast.LENGTH_SHORT).show()
    }

    fun readData(uname : String, pword : String) : MutableList<User>{
        var list : MutableList<User> = ArrayList()
        val db = this.readableDatabase
        val query = "Select * from " + TABLE_NAME + " where " + "username" + " = " + uname + " and " + "password" + " = " + pword;
        val result = db.rawQuery(query, null)
        if (result.moveToFirst()){
            do {
                var user = User()
                user.id = result.getString(0).toInt()
                user.name = result.getString(1).toString()
                user.username = result.getString(2).toString()
                user.password = result.getString(3).toString()
                list.add(user)
            }while (result.moveToNext())
        }

        return list
    }
}
