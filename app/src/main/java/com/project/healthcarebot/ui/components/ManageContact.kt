package com.project.healthcarebot.ui.components

import com.project.healthcarebot.database.Contacts

class ManageContact {
    fun manageContacts(contacts: List<Contacts>): String {
        val contactBuilder = StringBuilder()
        contactBuilder.append("Saved Contacts\n")
        contactBuilder.append("--------------\n")

        // Append contacts
        for (contact in contacts) {
            contactBuilder.append("${contact.name}: ${contact.contactNumber}\n")
        }
        contactBuilder.append("\nWhom do you want to contact ?\n")

        return contactBuilder.toString()
    }
}