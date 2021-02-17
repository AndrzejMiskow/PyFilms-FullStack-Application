package com.vaadin.tutorial.crm.backend.service;

import com.vaadin.tutorial.crm.backend.entity.Contact;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class ContactServiceTest {
    private Contact contact = new Contact();


    @Before
    public void setupData() {
        contact.setFirstName("testFirstName");
        contact.setLastName("testLastName");
    }


    @Test
    public void testGet() {
        Assert.assertEquals("testFirstName",contact.getFirstName());
        Assert.assertEquals("testLastName",contact.getLastName());
    }


}