package com.project.healthcarebot.database

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
