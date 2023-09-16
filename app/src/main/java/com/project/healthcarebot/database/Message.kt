package com.project.healthcarebot.database

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "message")
data class Message(
    val messageText: String,
    val messageTimeStamp: Long,
    val replyText: String? = null,
    val replyTimeStamp: Long? = null,
    @PrimaryKey val id: Int,
)

@Entity(tableName = "contacts")
data class Contacts(
    val name: String,
    @ColumnInfo val contactNumber: Long,
    @PrimaryKey val id: Int? = null
)
