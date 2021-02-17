package com.vaadin.tutorial.crm.backend.entity;

import javax.persistence.Entity;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

@Entity
//Table of Contacts (sample)
public class Contact extends AbstractEntity implements Cloneable {


  @NotNull
  @NotEmpty
  private String firstName = "";

  @NotNull
  @NotEmpty
  private String lastName = "";


  //getters and setters
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }

  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  @Override
  public String toString() {
    return firstName + " " + lastName;
  }

}